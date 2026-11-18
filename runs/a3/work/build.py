"""Build work/e.yaml: the edit file `ed treat` wrote (work/t.events.yaml) plus the hand-placed events
(hook comparison, the test character, the side-by-side grid of results, the end card)."""
import yaml

JOB = "."
R = JOB + "/material/results/"
d = yaml.safe_load(open(JOB + "/work/t.events.yaml"))
ev = d["events"]

# Brand: yellow is a band colour, never a text colour -> active caption word and card kicker in cyan.
d["captions"]["style"]["highlight"] = "#00A0DC"
d["look"]["card"]["accent"] = "#00A0DC"

SPEECH_END = 48.0
CARD_END = 51.5
WIDE = [1344, 640, 0, 40]          # 2.1:1 window of a 1344x768 result clip, head and shoulders
SQ = [768, 768, 288, 0]            # square window on the face


def tile(id_, clip, rect, label, window, ss=0.0):
    return {"id": id_, "src": R + clip, "ss": round(ss % 5.0, 3), "rect": rect, "window": window,
            "label": label, "loop": True}


def grids(name, frames, make):
    """One grid event per talk cut inside the span (a grid lasts until the next cut); the clips run on."""
    for f in frames:
        ss = (f - frames[0]) / 24.0
        ev.append({"t": f"f{f}", "type": "grid", "id": f"{name}_{f}", "tiles": make(ss)})


# 1. Hook (0 - 2.58 s, "Fewer steps should mean fewer seconds."): the same clip at two settings, timed.
grids("hook", [0], lambda ss: [
    tile("h1", "result01.mp4", [90, 440, 900, 429], "BASE · 20 STEPS · 600 S", WIDE, ss),
    tile("h2", "result02.mp4", [90, 890, 900, 429], "4-STEP LORA · 147 S", WIDE, ss),
])
# (a "SPEED-UP TEST" title here hid the hook's captions: dropped, the captions carry the hook line)
# "It's not that simple": the one special title the channel defaults ask for (T1) -> sliced type.
for e in ev:
    if e.get("id") == "slam_notsimple":
        e["kind"] = "sliced"
        e["color"] = "#F4F4F1"

# 2. take03 ("You might know her. Last time, a refiner redrew her face..."): show the test character.
grids("her", [407, 433], lambda ss: [
    tile("c1", "result01.mp4", [60, 320, 960, 960], "THE TEST CHARACTER", SQ, ss),
])

# 3. "So I watched them all side by side ... Watch her eyes and freckles": four settings in a 2x2 grid.
S = 492
X0, X1 = 36, 36 + S + 24
Y0, Y1 = 300, 300 + S + 56
grids("side", [670, 736, 848], lambda ss: [
    tile("g1", "result01.mp4", [X0, Y0, S, S], "BASE · 600 S", SQ, ss),
    tile("g2", "result03.mp4", [X1, Y0, S, S], "8-STEP · 267 S", SQ, ss),
    tile("g3", "result04.mp4", [X0, Y1, S, S], "6-STEP · 208 S", SQ, ss),
    tile("g4", "result02.mp4", [X1, Y1, S, S], "4-STEP · 147 S", SQ, ss),
])
ev.append({"t": 35.55, "type": "tile", "tile": "g4", "punch": 0.12, "d": 0.3, "state": "highlight"})

# 4. End card after the last line.
ev.append({"t": SPEECH_END, "type": "cut", "id": "endcard", "color": "#0E0E0E"})
ev.append({"t": SPEECH_END + 0.15, "type": "titlecard", "kicker": "THE FULL TEST",
           "lines": ["SPEED-UPS", "VS HER FACE"], "sub": "LAST WEEK'S EPISODE", "cap": 44,
           "dur": f"{CARD_END - SPEECH_END - 0.45:.2f}s"})
d["end"] = f"{CARD_END}s"

yaml.safe_dump(d, open(JOB + "/work/e.yaml", "w"), sort_keys=False, allow_unicode=True, width=200)
print("wrote work/e.yaml", len(ev), "events")
