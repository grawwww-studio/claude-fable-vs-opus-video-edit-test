"""review.py MP4 OUT.jpg t1 t2 ...: frames of the rendered video at those seconds, side by side (360 px wide each)."""
import sys, cv2, numpy as np

mp4, out, times = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]]
cap = cv2.VideoCapture(mp4)
n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print("frames", n, "fps", fps, "seconds", round(n / fps, 3))
tiles = []
for t in times:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps)))
    ok, fr = cap.read()
    if not ok:
        print("no frame at", t)
        continue
    h, w = fr.shape[:2]
    fr = cv2.resize(fr, (360, int(h * 360 / w)), interpolation=cv2.INTER_AREA)
    cv2.putText(fr, "%.2fs" % t, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    tiles.append(fr)
cv2.imwrite(out, np.hstack(tiles))
print(out)
