"""Copy the word files into work/words/ with the recogniser's mishearings fixed (TAKES.md is the truth)."""
import json, os

JOB = "."
SRC = os.path.join(JOB, "material", "words")
DST = os.path.join(JOB, "work", "words")
os.makedirs(DST, exist_ok=True)


def w(word, s, e, p=0.99):
    return {"word": word, "start": round(s, 3), "end": round(e, 3), "p": p}


def fix(name, words):
    out = []
    i = 0
    while i < len(words):
        x = words[i]
        t = x["word"]
        if name == "take01" and t == "May.":
            out.append(dict(x, word="Mae."))
        elif name == "take01" and t == "1RTX":
            mid = x["start"] + 0.3
            out.append(w("one", x["start"], mid))
            out.append(w("RTX", mid, x["end"]))
        elif name == "take01" and t == "4090":
            out.append(dict(x, word="4090,"))
        elif name == "take02" and t == "Today,":
            out.append(dict(x, word="Today:"))
        elif name == "take02" and t == "speed" and words[i + 1]["word"] == "-ups":
            out.append(w("speed-ups", x["start"], words[i + 1]["end"]))
            i += 1
        elif name == "take02" and t == "Minimax":
            out.append(dict(x, word="MiniMax"))
        elif name == "take02" and t == "AH" and words[i + 1]["word"] == "-3,":
            out.append(w("H3.", x["start"], words[i + 1]["end"]))
            i += 1
        elif name == "take02" and t == "seconds":
            out.append(dict(x, word="Seconds,"))
        elif name == "take03" and t == "you":
            out.append(dict(x, word="You"))
        elif name == "take05" and t == "one.":
            out.append(dict(x, word="one:"))
        elif name == "take07" and t == "a":
            out.append(dict(x, word="A"))
        elif name == "take10" and t == "measure.":
            out.append(dict(x, word="measure:"))
        elif name == "take10" and t == "Lip" and words[i + 1]["word"].startswith("sync"):
            out.append(w("lip-sync,", x["start"], words[i + 1]["end"]))
            i += 1
        else:
            out.append(x)
        i += 1
    return out


for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".json"):
        continue
    name = fn[:-5]
    d = json.load(open(os.path.join(SRC, fn)))
    d["words"] = fix(name, d["words"])
    json.dump(d, open(os.path.join(DST, fn), "w"), indent=1)
    print(name, " ".join(x["word"] for x in d["words"]))
