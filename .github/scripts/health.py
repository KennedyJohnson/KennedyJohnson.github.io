"""Weekly check that every live project is up and its data is fresh. Exits 1 with a report if not."""
import json
import sys
import urllib.request
from datetime import datetime, timezone

GH = "https://kennedyjohnson.github.io"
# (name, url that must load, freshness json url or None, json key holding a date, max age in days)
CHECKS = [
    ("Portfolio", f"{GH}/", None, None, None),
    ("Living Quality Map", "https://twin-cities-living-quality-map.vercel.app/",
     "https://twin-cities-living-quality-map.vercel.app/data/last_updated.json", "updated", 45),
    ("Property Assessment", f"{GH}/twin-cities-property-assessment/",
     f"{GH}/twin-cities-property-assessment/data/summary.json", "built", 60),
    ("Flight Delays", f"{GH}/will-my-flight-be-delayed/",
     f"{GH}/will-my-flight-be-delayed/data/metrics.json", "schedule_through", 150),
    ("Movie Recommender", f"{GH}/movie-recommender/",
     f"{GH}/movie-recommender/data/last_updated.json", "updated", 45),
    ("Gopher X Metro", "https://gopher-x-metro.github.io/Gopher-X-Metro/",
     "https://gopher-x-metro.github.io/Gopher-X-Metro/data/last_updated.json", "updated", 14),
    ("Metro Transit Delays", f"{GH}/metro-transit-delays/",
     f"{GH}/metro-transit-delays/data/meta.json", "updated", 3),
    ("Social Media Analysis", f"{GH}/social-media-analysis/", None, None, None),
    ("Creekside", f"{GH}/creekside/", None, None, None),
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "portfolio-health-check"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


problems = []
for name, page, fresh_url, key, max_days in CHECKS:
    try:
        get(page)
    except Exception as e:
        problems.append(f"**{name}** is down: {page} ({e})")
        continue
    if not fresh_url:
        print(f"ok   {name}")
        continue
    try:
        when = datetime.fromisoformat(json.loads(get(fresh_url))[key].replace("Z", "+00:00"))
        when = when if when.tzinfo else when.replace(tzinfo=timezone.utc)
        age = (datetime.now(timezone.utc) - when).days
    except Exception as e:
        problems.append(f"**{name}**: couldn't read freshness from {fresh_url} ({e})")
        continue
    status = "ok" if age <= max_days else "STALE"
    print(f"{status:<5}{name}: data {age} days old (limit {max_days})")
    if age > max_days:
        problems.append(f"**{name}** data is {age} days old (limit {max_days}). Check its refresh workflow.")

if problems:
    with open("health_report.md", "w") as f:
        f.write("\n".join(f"- {p}" for p in problems) + "\n")
    print("\n".join(problems))
    sys.exit(1)
