import os, json
from datetime import datetime, timezone

STATE_FILE = 'pet-state.json'
SVG_OUTPUT = 'pet.svg'

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, encoding='utf-8') as f:
            return json.load(f)
    return {'days_alive': 0, 'last_run': None, 'streak': 0, 'high_streak': 0}

state = load_state()
today_str = datetime.now(timezone.utc).date().isoformat()
if state['last_run'] != today_str:
    state['days_alive'] += 1
    state['last_run'] = today_str
state.setdefault('streak', 0)
state.setdefault('high_streak', 0)

contributions = 3
accent = '#4ade80'
glow = '#4ade8022'
label = 'Happy'
days = state['days_alive']

if days < 1:   stage = 'Egg'
elif days < 3: stage = 'Baby'
elif days < 7: stage = 'Child'
elif days < 14: stage = 'Teen'
else:          stage = 'Adult'

CAT = [
  '0001100110000',
  '0011111111000',
  '0122212221200',
  '1222222222210',
  '1224224422210',
  '1222222222210',
  '1222352532210',
  '1223252532210',
  '0122222222100',
  '0012222221000',
  '0001122110000',
  '0000100010000',
]
COLS = {'0': None, '1': '#1a1a2e', '2': '#d4a96a', '3': '#e08888', '4': '#1a1a2e', '5': '#5a3e28'}
cell = 7; ox = 20; oy = 16
rects = []
for r, row in enumerate(CAT):
    for c, code in enumerate(row):
        col = COLS.get(code)
        if col:
            x = ox + c * cell
            y = oy + r * cell
            rects.append('<rect x="{}" y="{}" width="{}" height="{}" fill="{}"/>'.format(x, y, cell, cell, col))
cat_svg = '\n    '.join(rects)

bar_w = min(180, contributions * 25)
streak = state['streak']
high = state['high_streak']

lines = [
'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="160" viewBox="0 0 440 160">',
'  <defs>',
'    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">',
'      <stop offset="0%" stop-color="#0d1117"/>',
'      <stop offset="100%" stop-color="#161b22"/>',
'    </linearGradient>',
'  </defs>',
'  <rect width="440" height="160" rx="12" fill="url(#bg)" stroke="{}" stroke-width="1" stroke-opacity="0.5"/>'.format(accent),
'  <ellipse cx="105" cy="80" rx="58" ry="50" fill="{}"/>'.format(glow),
'  ' + cat_svg,
'  <line x1="185" y1="18" x2="185" y2="142" stroke="{}" stroke-width="0.6" stroke-opacity="0.2"/>'.format(accent),
'  <text x="205" y="40" font-family="ui-monospace,Menlo,monospace" font-size="13" font-weight="600" fill="#e6edf3">Stage:  {}</text>'.format(stage),
'  <text x="205" y="58" font-family="ui-monospace,Menlo,monospace" font-size="11" fill="{}">Day {}  |  Streak: {} days</text>'.format(accent, days, streak),
'  <text x="205" y="84" font-family="ui-monospace,Menlo,monospace" font-size="10" fill="#8b949e">Mood</text>',
'  <rect x="205" y="90" width="180" height="8" rx="4" fill="#21262d"/>',
'  <rect x="205" y="90" width="{}" height="8" rx="4" fill="{}"/>'.format(bar_w, accent),
'  <text x="391" y="97" font-family="ui-monospace,Menlo,monospace" font-size="9" fill="{}" text-anchor="end">{}</text>'.format(accent, label),
'  <text x="205" y="118" font-family="ui-monospace,Menlo,monospace" font-size="10" fill="#8b949e">Contributions (7d)</text>',
'  <text x="391" y="118" font-family="ui-monospace,Menlo,monospace" font-size="12" font-weight="600" fill="#e6edf3" text-anchor="end">{}</text>'.format(contributions),
'  <text x="205" y="140" font-family="ui-monospace,Menlo,monospace" font-size="10" fill="#8b949e">Best streak</text>',
'  <text x="391" y="140" font-family="ui-monospace,Menlo,monospace" font-size="10" fill="{}" text-anchor="end">{} days</text>'.format(accent, high),
'</svg>',
]

svg = '\n'.join(lines)
with open(SVG_OUTPUT, 'w', encoding='utf-8') as f:
    f.write(svg)
with open(STATE_FILE, 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2)
print('Done')
