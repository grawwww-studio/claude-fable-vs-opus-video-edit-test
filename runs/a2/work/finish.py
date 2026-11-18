# Take the edit file `ed treat` wrote (work/t.events.yaml) and add the hand-made layer:
# the result clips with the seconds of each setting (light data panels with moving tiles, so no second AI label),
# a hook line at the top for the first seconds, and an end card. Writes work/edit.yaml.
import os
import yaml

job = os.environ.get("ED_JOB") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(job, "work")
R = os.path.join(job, "material", "results")
spec = yaml.safe_load(open(os.path.join(W, "t.events.yaml")))
ev = spec["events"]
words = ev[0]["words"]          # the podcast captions: [text, t0, t1] in piece time


def word_t(text, after=0.0, end=False):
    for w, t0, t1 in words:
        if t0 >= after and w.strip(".,:").lower() == text.lower():
            return t1 if end else t0
    raise SystemExit("word not found: " + text)


for e in ev:
    if e.get("id") == "slam_fewersteps":
        e["kind"] = "sliced"   # T1: at least one title of a special kind


def res(n):
    return os.path.join(R, "result%02d.mp4" % n)


for e in ev:
    if e.get("id") == "slam_checktheface":
        e["kind"] = "sliced"   # T1: at least one title of a special kind

talk_end = max(w[2] for w in words)

# Result clips as GRID shots (dark C card, moving tiles, mono labels). A grid lasts until the next cut, so each one
# starts on a phrase and ends on one of the talk block's own cuts (compiled times from `bin/ed check`):
#   t0_1 2.583 (after "fewer seconds."), t2_1 15.083 (after "MiniMax H3."), t5_1 29.042 (after "all at once."),
#   t6_1 33.5 then t7_0 36.25 ("So I watched them all side by side.").
TOP = [100, 380, 880, 495]     # two stacked 16:9 tiles, clear of the AI tag zone and above the captions
BOT = [100, 925, 880, 495]
SQ = [560, 560, 392, 0]        # square window round the character's head in a 1344x768 result clip
Q = [[60, 400, 470, 470], [550, 400, 470, 470], [60, 920, 470, 470], [550, 920, 470, 470]]


def tile(tid, n, rect, label, window=None, ss=0.3):
    d = {"id": tid, "src": res(n), "ss": ss, "rect": rect, "label": label}
    if window:
        d["window"] = window
    return d


t_same = word_t("Same")
t_so = 33.542                  # one frame after the talk cut t6_1, on "So I watched them all side by side"
add = [
    {"t": 0, "type": "grid", "id": "g_hook", "tiles": [
        tile("h1", 1, TOP, "BASE MODEL · 20 STEPS · 600 S A CLIP"),
        tile("h2", 2, BOT, "4-STEP SPEED LORA · 147 S A CLIP")]},
    {"t": round(word_t("the", after=10.0) + 0.0, 3), "type": "grid", "id": "g_loras", "tiles": [
        tile("l1", 3, TOP, "8-STEP SPEED LORA · 267 S · 2.2x"),
        tile("l2", 4, BOT, "6-STEP SPEED LORA · 208 S · 2.9x")]},
    {"t": round(t_same, 3), "type": "grid", "id": "g_shots", "tiles": [
        tile("s1", 2, TOP, "CLOSE SHOT · 4-STEP · 147 S"),
        tile("s2", 7, BOT, "WIDE SHOT · 4-STEP · 147 S")]},
    {"t": t_so, "type": "grid", "id": "g_side", "tiles": [
        tile("q1", 1, Q[0], "20 STEPS · 600 S", SQ),
        tile("q2", 3, Q[1], "8 STEPS · 267 S", SQ),
        tile("q3", 4, Q[2], "6 STEPS · 208 S", SQ),
        tile("q4", 2, Q[3], "4 STEPS · 147 S", SQ)]},
]

# end card: dark C ground, a short build-in title, after the last word
card_t = round(talk_end + 0.35, 3)
end_t = round(card_t + 2.9, 3)
add += [
    {"t": card_t, "type": "cut", "id": "endcard", "color": "#0E0E0E"},
    {"t": round(card_t + 0.25, 3), "type": "panel", "id": "p_end", "x": 90, "y": 700, "w": 900,
     "label": "FULL EPISODE ON THE CHANNEL",
     "figures": [{"text": "4.1x", "sub": "AS FAST AT 4 STEPS · STILL CHECK HER EYES", "count": 12}],
     "dur": "2.2s"},
]

# identity C: yellow only as a band behind dark text, never as a text colour -> the spoken word is cyan, not yellow
spec["captions"]["style"]["highlight"] = "#00A0DC"

spec["events"] = ev + add
spec["end"] = "%.3fs" % end_t
spec["free_cuts"] = True
yaml.safe_dump(spec, open(os.path.join(W, "edit.yaml"), "w"), sort_keys=False, allow_unicode=True, width=200)
print("same %.2f talk_end %.2f card %.2f end %.2f"
      % (t_same, talk_end, card_t, end_t))
