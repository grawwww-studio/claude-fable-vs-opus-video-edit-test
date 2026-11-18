"""Hand edits on top of the treatment's edit file: t4.events.yaml -> short.yaml
run: bin/ed treat work/t4.yaml --out work/t4.events.yaml ; bin/ed py work/build.py
Frame numbers below are the talk's own cuts (bin/ed check work/t4.events.yaml -> work/t4.check.txt)."""
import os, sys, yaml

here = os.path.dirname(os.path.abspath(__file__))
job = os.path.dirname(here)
opts = set(sys.argv[1:])
spec = yaml.safe_load(open(os.path.join(here, "t4.events.yaml")))
ev = spec["events"]
FPS = 24.0
F = lambda n: round(n / FPS, 4)

# 1. captions: the recogniser misheard names; TAKES.md is the truth
caps = next(e for e in ev if e.get("type") == "podcast")
out = []
words = caps["words"]
i = 0
while i < len(words):
    w, a, b = words[i]
    if w == "1RTX":
        mid = round(a + (b - a) * 0.4, 3)
        out += [["one", a, mid], ["RTX", mid, b]]
    elif w == "speed" and i + 1 < len(words) and words[i + 1][0] == "-ups":
        out.append(["speed-ups", a, words[i + 1][2]]); i += 1
    elif w == "Minimax":
        out.append(["MiniMax", a, b])
    elif w == "AH" and i + 1 < len(words) and words[i + 1][0].startswith("-3"):
        out.append(["H3,", a, words[i + 1][2]]); i += 1
    elif w == "Lip" and i + 1 < len(words) and words[i + 1][0].startswith("sync"):
        out.append(["Lip-sync,", a, words[i + 1][2]]); i += 1
    else:
        out.append([w, a, b])
    i += 1
caps["words"] = out

# 2. caption look: yellow is never a text colour in identity C
if "plate" in opts:
    spec.pop("captions", None)            # the editor's own podcast captions: light plate, yellow band, K text
else:
    spec["captions"]["style"]["highlight"] = "#00A0DC"

# 3. result clips as shots of their own (9:16 window on the face), ending on the talk's own cuts
R = os.path.join(job, "material", "results")
W = {"aspect": "9:16", "zoom": 1.0}
ev.append({"t": F(21), "type": "cut", "id": "r_hook", "src": R + "/result08.mp4", "ss": 0.4, "window": W})      # until f62
ev.append({"t": F(282), "type": "cut", "id": "r_base", "src": R + "/result01.mp4", "ss": 0.4, "window": W})     # until f337
ev.append({"t": F(677), "type": "cut", "id": "r_4step", "src": R + "/result02.mp4", "ss": 0.4, "window": W})    # until f727
PX, PW, PY = 140, 800, 1245
ev.append({"t": F(29), "type": "panel", "id": "p_hook", "x": PX, "y": PY, "w": PW, "label": "4-STEP SPEED LORA",
           "figures": [{"text": "4.1X", "sub": "AS FAST", "size": 76}], "dur": "1.15s"})
ev.append({"t": F(290), "type": "panel", "id": "p_base", "x": PX, "y": PY, "w": PW, "label": "BASE MODEL / 20 STEPS",
           "figures": [{"text": "600", "sub": "SECONDS A CLIP", "count": 14, "size": 76}], "dur": "1.75s"})
ev.append({"t": F(685), "type": "panel", "id": "p_4step", "x": PX, "y": PY, "w": PW, "label": "4-STEP SPEED LORA",
           "figures": [{"text": "147", "sub": "SECONDS A CLIP / 4.1X AS FAST", "count": 12, "size": 76}],
           "dur": "1.5s"})

# 4. side by side: four settings, same seed, native-size crops on the face
GW = [540, 560, 396, 20]
gy = 330
ev.append({"t": F(785), "type": "grid", "id": "g_side", "tiles": [
    {"id": "g1", "src": R + "/result01.mp4", "ss": 0.4, "rect": [0, gy, 540, 560], "window": GW, "label": "BASE 600 S"},
    {"id": "g2", "src": R + "/result03.mp4", "ss": 0.4, "rect": [540, gy, 540, 560], "window": GW, "label": "8-STEP 267 S"},
    {"id": "g3", "src": R + "/result04.mp4", "ss": 0.4, "rect": [0, gy + 560, 540, 560], "window": GW, "label": "6-STEP 208 S"},
    {"id": "g4", "src": R + "/result02.mp4", "ss": 0.4, "rect": [540, gy + 560, 540, 560], "window": GW, "label": "4-STEP 147 S"},
]})                                                                                                               # until f875

# 5. the hook line at the top of the first seconds, one special title, the end card
if "header" in opts:
    ev.append({"t": F(8), "type": "panel", "id": "p_top", "x": 230, "y": 104, "w": 700, "label": "AI VIDEO ON ONE GPU", "figures": [{"text": "SPEED VS FACE", "size": 50}], "dur": "2.05s"})
ev.append({"t": F(881), "type": "kin", "kind": "whisper", "id": "w_notmeasured", "text": "NOT MEASURED", "cap": 40, "color": "#F4F4F1",
           "place": "auto", "place_opts": {"prefer": ["uc", "c", "lc"]}, "dur": "1.3s"})
END = 1133
ev.append({"t": F(END), "type": "cut", "id": "endcard", "color": "#0E0E0E"})
ev.append({"t": F(END + 6), "type": "titlecard", "id": "tc_end", "kicker": "THE FULL TEST", "lines": ["FIVE", "SETTINGS", "ONE FACE"],
           "sub": "FULL EPISODE ON THE CHANNEL", "cap": 60, "dur": "2.0s"})
spec["look"]["card"]["accent"] = "#00A0DC"      # yellow is never a text colour: the card kicker goes cyan
spec["end"] = "%.4fs" % F(END + 62)

name = "short.yaml"
yaml.safe_dump(spec, open(os.path.join(here, name), "w"), sort_keys=False, allow_unicode=True, width=200)
print("wrote", name, len(ev), "events")
