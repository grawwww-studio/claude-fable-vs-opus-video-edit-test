import cv2, os, numpy as np
job = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for i in range(1, 9):
    p = os.path.join(job, "material", "results", "result%02d.mp4" % i)
    c = cv2.VideoCapture(p)
    n = int(c.get(cv2.CAP_PROP_FRAME_COUNT))
    fr = []
    for k in (0, n // 2, n - 2):
        c.set(cv2.CAP_PROP_POS_FRAMES, k)
        ok, f = c.read()
        if not ok:
            f = np.zeros((768, 1344, 3), np.uint8)
        f = cv2.resize(f, (448, 256))
        cv2.putText(f, "r%02d f%d" % (i, k), (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        fr.append(f)
    rows.append(np.hstack(fr))
cv2.imwrite(os.path.join(job, "work", "sheet_results.jpg"), np.vstack(rows))
rows = []
for i in range(1, 11):
    p = os.path.join(job, "material", "takes", "take%02d.mp4" % i)
    c = cv2.VideoCapture(p)
    n = int(c.get(cv2.CAP_PROP_FRAME_COUNT))
    fr = []
    for k in (0, n // 2):
        c.set(cv2.CAP_PROP_POS_FRAMES, k)
        ok, f = c.read()
        f = cv2.resize(f, (480, 270))
        cv2.putText(f, "t%02d f%d" % (i, k), (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        fr.append(f)
    rows.append(np.hstack(fr))
cv2.imwrite(os.path.join(job, "work", "sheet_takes.jpg"), np.vstack(rows))
print("ok")
