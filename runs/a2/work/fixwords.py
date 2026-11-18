# Copy the word files to work/words/ and correct what the recogniser misheard (TAKES.md is the truth).
import json, os
job = os.environ.get("ED_JOB") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(job, "material", "words")
dst = os.path.join(job, "work", "words")
os.makedirs(dst, exist_ok=True)


def W(word, s, e, p=0.99):
    return {"word": word, "start": s, "end": e, "p": p}


def fix(n, words):
    out = []
    i = 0
    while i < len(words):
        w = dict(words[i])
        t = w["word"]
        if n == 1 and t == "May.":
            w["word"] = "Mae."
        elif n == 1 and t == "1RTX":
            out.append(W("one", w["start"], 3.50))
            out.append(W("RTX", 3.50, w["end"]))
            i += 1
            continue
        elif n == 1 and t == "4090":
            w["word"] = "4090,"
        elif n == 2 and t == "Today,":
            w["word"] = "Today:"
        elif n == 2 and t == "speed" and words[i + 1]["word"] == "-ups":
            out.append(W("speed-ups", w["start"], words[i + 1]["end"]))
            i += 2
            continue
        elif n == 2 and t == "Minimax":
            w["word"] = "MiniMax"
        elif n == 2 and t == "AH" and words[i + 1]["word"] == "-3,":
            out.append(W("H3.", w["start"], words[i + 1]["end"]))
            i += 2
            continue
        elif n == 2 and t == "seconds":
            w["word"] = "Seconds,"
        elif n == 3 and t == "you":
            w["word"] = "You"
        elif n == 5 and t == "one.":
            w["word"] = "one:"
        elif n == 7 and t == "a" and i == 0:
            w["word"] = "A"
        elif n == 10 and t == "measure.":
            w["word"] = "measure:"
        elif n == 10 and t == "Lip" and words[i + 1]["word"] == "sync,":
            out.append(W("lip-sync,", w["start"], words[i + 1]["end"]))
            i += 2
            continue
        elif n == 10 and t in ("motion,", "other", "longer"):
            pass
        out.append(w)
        i += 1
    return out


for n in range(1, 11):
    d = json.load(open(os.path.join(src, "take%02d.json" % n)))
    d["words"] = fix(n, d["words"])
    d["audio"] = os.path.join(job, "material", "takes", "take%02d.mp4" % n)
    json.dump(d, open(os.path.join(dst, "take%02d.json" % n), "w"), indent=1)
    print("take%02d" % n, " ".join(w["word"] for w in d["words"]))
