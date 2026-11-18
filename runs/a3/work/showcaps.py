import sys, yaml
p = sys.argv[1] if len(sys.argv) > 1 else "work/t.events.yaml"
d = yaml.safe_load(open(p))
for k in d:
    if k not in ("events", "talk", "look", "captions"):
        print(k, ":", d[k])
for e in d["events"]:
    if e.get("type") == "podcast":
        line = []
        for w, a, b in e["words"]:
            line.append(f"{w}[{a:.2f}-{b:.2f}]")
            if w.endswith((".", ":")):
                print(" ".join(line)); line = []
        if line:
            print(" ".join(line))
    else:
        print("EV", e.get("t"), e.get("type"), e.get("id"), e.get("dur"))
