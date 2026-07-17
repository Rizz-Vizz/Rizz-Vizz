import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# ── Config ──────────────────────────────────────────────────────────────────
GITHUB_USERNAME = "Rizz-Vizz"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
STATE_FILE = "pet-state.json"
SVG_OUTPUT = "pet.svg"

# ── Fetch contribution count for the last 7 days via GraphQL ────────────────
def get_contributions():
    today = datetime.now(timezone.utc)
    week_ago = today - timedelta(days=7)
    query = """
    {
      user(login: "%s") {
        contributionsCollection(from: "%s", to: "%s") {
          totalCommitContributions
          totalPullRequestContributions
          totalIssueContributions
        }
      }
    }
    """ % (GITHUB_USERNAME, week_ago.isoformat(), today.isoformat())

    data = json.dumps({"query": query}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=data,
        headers={
            "Authorization": f"bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "commitchi-custom",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            c = result["data"]["user"]["contributionsCollection"]
            return (
                c["totalCommitContributions"]
                + c["totalPullRequestContributions"]
                + c["totalIssueContributions"]
            )
    except Exception as e:
        print(f"[warn] Could not fetch contributions: {e}")
        return 0

# ── Load / update persistent state ──────────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"days_alive": 0, "last_run": None, "streak": 0, "high_streak": 0}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def update_state(state, contributions):
    today_str = datetime.now(timezone.utc).date().isoformat()
    if state["last_run"] != today_str:
        state["days_alive"] += 1
        state["last_run"] = today_str
        if contributions > 0:
            state["streak"] = state.get("streak", 0) + 1
        else:
            state["streak"] = 0
        state["high_streak"] = max(state.get("high_streak", 0), state["streak"])
    return state

# ── Determine pet stage & mood ───────────────────────────────────────────────
def get_stage(days):
    if days < 1:   return "Egg"
    if days < 3:   return "Baby"
    if days < 7:   return "Child"
    if days < 14:  return "Teen"
    return "Adult"

def get_mood(contributions, streak):
    if contributions >= 5 or streak >= 3:  return "happy"
    if contributions == 0:                  return "sad"
    return "neutral"

# ── Pet pixel art (SVG paths) ─────────────────────────────────────────────────
# A clean, simple pixel cat sprite per mood, drawn with SVG rects.
# Each cell is 6px. Grid origin: (0,0). Colours: outline #1a1a2e, body #c9a96e
# eyes #1a1a2e, blush #e57373, bg transparent.

PIXEL_CATS = {
    # 13-wide × 12-tall grids  (1=outline, 2=body, 3=blush, 4=eye, 5=mouth-happy, 6=mouth-sad)
    "happy": [
        "0001100110000",
        "0011111111000",
        "0122212221200",
        "1222222222210",
        "1224224422210",
        "1222222222210",
        "1223242232210",
        "1222352532210",
        "0122222222100",
        "0012222221000",
        "0001122110000",
        "0000100010000",
    ],
    "neutral": [
        "0001100110000",
        "0011111111000",
        "0122212221200",
        "1222222222210",
        "1224224422210",
        "1222222222210",
        "1222252522210",
        "1222232322210",
        "0122222222100",
        "0012222221000",
        "0001122110000",
        "0000100010000",
    ],
    "sad": [
        "0001100110000",
        "0011111111000",
        "0122212221200",
        "1222222222210",
        "1224224422210",
        "1222222222210",
        "1222252522210",
        "1222362632210",
        "0122222222100",
        "0012222221000",
        "0001122110000",
        "0000100010000",
    ],
}

COLOURS = {
    "0": None,          # transparent
    "1": "#1a1a2e",     # dark outline
    "2": "#d4a96a",     # warm body
    "3": "#e08888",     # blush
    "4": "#1a1a2e",     # eye dot
    "5": "#5a3e28",     # happy mouth curve
    "6": "#5a3e28",     # sad mouth curve
}

def render_cat_svg(mood, cell=7, ox=30, oy=20):
    """Render pixel cat rects for given mood. Returns list of SVG rect strings."""
    grid = PIXEL_CATS.get(mood, PIXEL_CATS["neutral"])
    rects = []
    for r, row in enumerate(grid):
        for c, code in enumerate(row):
            col = COLOURS.get(code)
            if col is None:
                continue
            x = ox + c * cell
            y = oy + r * cell
            rects.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{col}"/>')
    return rects


# ── Build full SVG card ───────────────────────────────────────────────────────
MOOD_LABEL = {"happy": "Happy & Well-Fed", "neutral": "Doing Okay", "sad": "Hungry — Commit Soon!"}
MOOD_ACCENT = {"happy": "#4ade80", "neutral": "#facc15", "sad": "#f87171"}
MOOD_GLOW   = {"happy": "#4ade8044", "neutral": "#facc1544", "sad": "#f8717144"}

def build_svg(state, contributions, mood):
    stage = get_stage(state["days_alive"])
    streak = state.get("streak", 0)
    high = state.get("high_streak", 0)
    days = state["days_alive"]

    accent = MOOD_ACCENT[mood]
    glow   = MOOD_GLOW[mood]
    label  = MOOD_LABEL[mood]

    cat_rects = "\n    ".join(render_cat_svg(mood))

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="460" height="175" viewBox="0 0 460 175">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f0f1a"/>
      <stop offset="100%" stop-color="#1a1a2e"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Card background -->
  <rect width="460" height="175" rx="14" fill="url(#bg)" stroke="{accent}" stroke-width="1.5" stroke-opacity="0.6"/>

  <!-- Glow halo behind pet -->
  <ellipse cx="121" cy="90" rx="62" ry="55" fill="{glow}"/>

  <!-- Pixel cat -->
  {cat_rects}

  <!-- Divider -->
  <line x1="200" y1="20" x2="200" y2="155" stroke="{accent}" stroke-width="0.8" stroke-opacity="0.25"/>

  <!-- Pet name & stage -->
  <text x="224" y="42" font-family="'Courier New', monospace" font-size="19" font-weight="bold" fill="#f0f0f0">Ritviz's Pet</text>
  <text x="224" y="62" font-family="'Courier New', monospace" font-size="11" fill="{accent}">Stage: {stage}  ·  Day {days}</text>

  <!-- Mood -->
  <text x="224" y="88" font-family="'Courier New', monospace" font-size="12" fill="#aaaacc">Mood</text>
  <rect x="224" y="95" width="200" height="10" rx="5" fill="#2a2a3e"/>
  <rect x="224" y="95" width="{min(200, contributions * 20)}" height="10" rx="5" fill="{accent}"/>
  <text x="430" y="104" font-family="'Courier New', monospace" font-size="9" fill="#888" text-anchor="end">{label}</text>

  <!-- Streak -->
  <text x="224" y="126" font-family="'Courier New', monospace" font-size="12" fill="#aaaacc">Streak</text>
  <text x="368" y="126" font-family="'Courier New', monospace" font-size="12" fill="{accent}" text-anchor="end">{streak} days  (best: {high})</text>

  <!-- Commits this week -->
  <text x="224" y="148" font-family="'Courier New', monospace" font-size="12" fill="#aaaacc">Contributions (7d)</text>
  <text x="430" y="148" font-family="'Courier New', monospace" font-size="12" fill="#f0f0f0" text-anchor="end">{contributions}</text>
</svg>"""
    return svg


# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Fetching contributions…")
    contributions = get_contributions()
    print(f"  → {contributions} contributions in last 7 days")

    state = load_state()
    state = update_state(state, contributions)
    mood  = get_mood(contributions, state.get("streak", 0))
    save_state(state)

    svg = build_svg(state, contributions, mood)
    with open(SVG_OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"  → Pet is '{mood}', stage '{get_stage(state['days_alive'])}', day {state['days_alive']}")
    print(f"  → Wrote {SVG_OUTPUT}")
