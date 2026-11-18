import json, os, sys
job = os.environ.get("ED_JOB") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for i in range(1, 11):
    p = os.path.join(job, "material", "words", "take%02d.json" % i)
    d = json.load(open(p))
    print("take%02d dur=%s" % (i, d.get("duration")), " ".join("%s[%.2f-%.2f]" % (w["word"], w["start"], w["end"]) for w in d["words"]))
