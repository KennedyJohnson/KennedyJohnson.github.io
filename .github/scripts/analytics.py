"""Fetch last-7-days Cloudflare Web Analytics for Gopher X Metro -> docs/data/analytics.json."""
import json, os, urllib.request
from datetime import datetime, timedelta, timezone

ACCOUNT = "5e857fec77c88383bf9b2efc4b9d576d"
SITE_TAG = "07cf1456d56a4e649da9b27bb8574631"
OUT = "docs/data/analytics.json"

end = datetime.now(timezone.utc).replace(microsecond=0)
start = end - timedelta(days=7)
query = """
query($acct: String!, $tag: String!, $start: Time!, $end: Time!) {
  viewer { accounts(filter: {accountTag: $acct}) {
    rumPageloadEventsAdaptiveGroups(limit: 1,
      filter: {siteTag: $tag, datetime_geq: $start, datetime_leq: $end, bot: 0}) {
      count
      sum { visits }
    }
  } }
}"""
req = urllib.request.Request(
    "https://api.cloudflare.com/client/v4/graphql",
    data=json.dumps({"query": query, "variables": {
        "acct": ACCOUNT, "tag": SITE_TAG,
        "start": start.isoformat().replace("+00:00", "Z"),
        "end": end.isoformat().replace("+00:00", "Z")}}).encode(),
    headers={"Authorization": f"Bearer {os.environ['CF_API_TOKEN']}",
             "Content-Type": "application/json"})
body = json.load(urllib.request.urlopen(req, timeout=30))
if body.get("errors"):
    raise SystemExit(f"Cloudflare API error: {body['errors']}")
groups = body["data"]["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
g = groups[0] if groups else {"count": 0, "sum": {"visits": 0}}
with open(OUT, "w") as f:
    json.dump({"page_views": g["count"], "visits": g["sum"]["visits"],
               "days": 7, "updated": end.date().isoformat()}, f, indent=2)
    f.write("\n")
print(f"{g['count']} page views, {g['sum']['visits']} visits")
