"""build.py: work/t.events.yaml (written by `ed treat` from work/t.yaml) -> work/short.events.yaml.

Hand additions on top of the treatment's edit file (every number is one in material/TAKES.md):
  - hook: the first words play over two labelled result clips (base 600 s, 4-step 147 s) on the dark card
  - the dark-on-dark kicker ONE RTX 4090 becomes light kinetic type (the piece's special title)
  - the result clips become plain shots (no second AI-GENERATED tag: the editor's AI tag is on every frame),
    starting on the frame of the talk's own cut so no stray frames of the presenter sit before them
  - the numbers: tile labels while she speaks (captions stay on), data panels only in the pauses after a line
    (the editor takes the captions off while a panel is up)
  - "side by side" is a 2x2 grid of the four settings, each labelled with its seconds
  - a closing pointer to the full episode
"""
import os, sys, yaml

JOB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(JOB, "work", "t.events.yaml")
DST = os.path.join(JOB, "work", sys.argv[1] if len(sys.argv) > 1 else "short.events.yaml")
RES = os.path.join(JOB, "material", "results")
FPS = 24.0
LIGHT = "#F4F4F1"
PX, PY, PW = 110, 1165, 860            # the data panel: under the face, above the captions

d = yaml.safe_load(open(SRC))
ev = d["events"]
by_id = {e.get("id"): e for e in ev}


def res(n):
    return os.path.join(RES, "result%02d.mp4" % n)


def f2t(frame):
    return round(frame / FPS, 4)


def grid(gid, t, tiles):
    return {"t": t, "type": "grid", "id": gid, "tiles": tiles}


def stack2(prefix, a, b, ss):
    """two wide tiles, one over the other, above the captions"""
    out = []
    for n, (clip, label) in enumerate((a, b)):
        out.append({"id": "%s%d" % (prefix, n), "src": res(clip), "ss": ss, "rect": [60, 330 + n * 565, 960, 545],
                    "window": [1344, 763, 0, 0], "label": label})
    return out


def one(clip, tid, label):
    """one big tile on the dark card; the data panel goes under it (never on the face)"""
    return [{"id": tid, "src": res(clip), "ss": 0.4, "rect": [60, 330, 960, 800], "window": [922, 768, 211, 0],
             "label": label}]


def panel(pid, t0, t1, label, fig, sub, count=12):
    f = {"text": fig, "sub": sub}
    if count:
        f["count"] = count
    ev.append({"t": round(t0, 3), "type": "panel", "id": pid, "x": PX, "y": PY, "w": PW, "label": label,
               "figures": [f], "dur": "%.2fs" % (t1 - t0)})


# Frames below are the talk's own cuts, read from `ed check work/t.events.yaml`.

# --- hook (frames 0-62, "Fewer steps should mean fewer seconds"): two labelled clips, captions on
ev.append(grid("hook", 0, stack2("h", (1, "BASE · 20 STEPS · 600 S A CLIP"), (2, "4-STEP LORA · 147 S A CLIP"), 0.4)))

# --- the kicker that is dark on a dark wall -> light kinetic type (also the piece's special title)
k = by_id["kick_onertx4090"]
ev[ev.index(k)] = {"t": k["t"], "type": "kin", "kind": os.environ.get("KIND", "jump"), "id": "kin_onertx4090",
                   "text": "ONE RTX 4090", "color": LIGHT, "cap": 56, "place": "auto", "dur": "1.5s"}

# --- "Seconds, against her face" (cut at frame 365, next cut 446; the line ends at 16.88 s): the base clip
a = by_id["ai1"]
ev[ev.index(a)] = grid("res_base", f2t(365), one(1, "b0", "BASE MODEL · 20 STEPS"))
panel("p_base", 16.98, 18.38, "BASE MODEL · 20 STEPS", "600", "SECONDS A CLIP")

# --- "Same three seeds, both shots, all at once" (23.25 s to the cut at frame 637): 8-step and 6-step
a = by_id["ai2"]
ev[ev.index(a)] = grid("mid", a["t"], stack2("m", (3, "8-STEP LORA · 267 S · 2.2× AS FAST"),
                                             (4, "6-STEP LORA · 208 S · 2.9× AS FAST"), 0.4))

# --- "Watch her eyes and freckles" (cut at frame 637, next cut 726; the line ends at 28.39 s): the 4-step clip
a = by_id["ai3"]
ev[ev.index(a)] = grid("res_4step", f2t(637), one(2, "f0", "4-STEP SPEED LORA"))
panel("p_4", 28.5, 30.0, "4-STEP SPEED LORA", "147", "SECONDS A CLIP · 4.1 TIMES AS FAST")

# --- "So I watched them all side by side" (cut at frame 784, next cut 876): the four settings
a = by_id["ai4"]
TW, TH = 470, 555
tiles = []
for n, (clip, label) in enumerate([(1, "BASE 600 S"), (3, "8-STEP 267 S"), (4, "6-STEP 208 S"), (2, "4-STEP 147 S")]):
    tiles.append({"id": "g%d" % n, "src": res(clip), "ss": 0.3,
                  "rect": [60 + (n % 2) * (TW + 20), 330 + (n // 2) * (TH + 20), TW, TH],
                  "window": [478, 564, 433, 0], "label": label})
ev[ev.index(a)] = grid("sidebyside", f2t(784), tiles)

# --- ending: the slam a little shorter, then (after "not just the clock", 46.97 s) the pointer to the episode
by_id["slam_checktheface"]["dur"] = "1.2s"
panel("p_end", 47.08, 48.55, "THE FULL EPISODE", "5 SETTINGS", "TIMED AND FACE-CHECKED", count=0)

ev.sort(key=lambda e: float(e["t"]))
yaml.safe_dump(d, open(DST, "w"), sort_keys=False, allow_unicode=True, width=200)
print("wrote", DST, len(ev), "events")
