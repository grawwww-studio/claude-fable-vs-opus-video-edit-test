"""crop.py MP4 OUT.jpg y0 y1 t1 t2 ...: the band y0..y1 of the rendered frames at those seconds, stacked (full width)."""
import sys, json, os, cv2, numpy as np

mp4, out, y0, y1 = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
cap = cv2.VideoCapture(mp4)
fps = cap.get(cv2.CAP_PROP_FPS)
rows = []
for t in [float(x) for x in sys.argv[5:]]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps)))
    ok, fr = cap.read()
    band = fr[y0:y1].copy()
    cv2.putText(band, "%.2fs" % t, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    rows.append(band)
cv2.imwrite(out, np.vstack(rows))
rep = mp4 + ".render_report.json"
if os.path.exists(rep):
    r = json.load(open(rep))
    print("report keys:", list(r.keys()))
    for k in ("audio", "loudness", "mix", "voice", "checks", "gate"):
        if k in r:
            print(k, json.dumps(r[k])[:900])
