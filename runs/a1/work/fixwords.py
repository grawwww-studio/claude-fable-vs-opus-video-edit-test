"""Copy the word files to work/words/ and correct what the recogniser misheard (TAKES.md is the truth).
Times are kept; only the spelling of words changes, and two tokens are merged / split on their own times."""
import json, os

JOB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(JOB, "material", "words")
DST = os.path.join(JOB, "work", "words")
os.makedirs(DST, exist_ok=True)


def w(word, start, end, p=0.99):
    return {"word": word, "start": round(start, 2), "end": round(end, 2), "p": p}


for i in range(1, 11):
    name = "take%02d.json" % i
    d = json.load(open(os.path.join(SRC, name)))
    words = d["words"]
    out = []
    k = 0
    while k < len(words):
        x = dict(words[k])
        t = x["word"]
        if i == 1 and t == "May.":
            x["word"] = "Mae."
        if i == 1 and t == "1RTX":
            mid = x["start"] + 0.32
            out.append(w("one", x["start"], mid))
            out.append(w("RTX", mid, x["end"]))
            k += 1
            continue
        if i == 1 and t == "4090":
            x["word"] = "4090,"
        if i == 2 and t == "Today,":
            x["word"] = "Today:"
        if i == 2 and t == "speed":
            nxt = words[k + 1]
            out.append(w("speed-ups", x["start"], nxt["end"]))
            k += 2
            continue
        if i == 2 and t == "Minimax":
            x["word"] = "MiniMax"
        if i == 2 and t == "AH":
            nxt = words[k + 1]
            out.append(w("H3.", x["start"], nxt["end"]))
            k += 2
            continue
        if i == 2 and t == "seconds":
            x["word"] = "Seconds,"
        if i == 3 and t == "you":
            x["word"] = "You"
        if i == 5 and t == "one.":
            x["word"] = "one:"
        if i == 7 and t == "a" and k == 0:
            x["word"] = "A"
        if i == 10 and t == "measure.":
            x["word"] = "measure:"
        if i == 10 and t == "Lip":
            nxt = words[k + 1]
            out.append(w("lip-sync,", x["start"], nxt["end"]))
            k += 2
            continue
        out.append(x)
        k += 1
    d["words"] = out
    json.dump(d, open(os.path.join(DST, name), "w"), indent=1)
    print(name, " ".join(o["word"] for o in out))
