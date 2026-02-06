// Small helpers: theme toggle and year
const yearEl = document.getElementById('year');
if(yearEl) yearEl.textContent = new Date().getFullYear();

const toggle = document.getElementById('theme-toggle');
toggle && toggle.addEventListener('click', ()=>{
  document.documentElement.classList.toggle('dark');
  const isDark = document.documentElement.classList.contains('dark');
  try{localStorage.setItem('theme', isDark? 'dark' : 'light')}catch(e){}
});

// load saved preference
try{
  const saved = localStorage.getItem('theme');
  if(saved === 'dark') document.documentElement.classList.add('dark');
}catch(e){}
