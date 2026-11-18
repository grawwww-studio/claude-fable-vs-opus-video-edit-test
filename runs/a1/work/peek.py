"""Contact sheets of the material: one frame of each take and each result clip, to choose crops."""
import os, cv2, numpy as np

JOB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(JOB, "work", "stills")
os.makedirs(OUT, exist_ok=True)


def grab(path, sec):
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    ok, fr = cap.read()
    cap.release()
    return fr


def sheet(names, sec, cols, tw, out):
    tiles = []
    for n in names:
        fr = grab(os.path.join(JOB, "material", n), sec)
        h, w = fr.shape[:2]
        fr = cv2.resize(fr, (tw, int(h * tw / w)))
        cv2.putText(fr, os.path.basename(n), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
        tiles.append(fr)
    while len(tiles) % cols:
        tiles.append(np.zeros_like(tiles[0]))
    rows = [np.hstack(tiles[i:i + cols]) for i in range(0, len(tiles), cols)]
    cv2.imwrite(os.path.join(OUT, out), np.vstack(rows))


sheet(["takes/take%02d.mp4" % i for i in range(1, 11)], 1.0, 4, 480, "takes.jpg")
sheet(["results/result%02d.mp4" % i for i in range(1, 9)], 1.0, 4, 480, "results_1s.jpg")
sheet(["results/result%02d.mp4" % i for i in range(1, 9)], 4.5, 4, 480, "results_4s.jpg")
print("ok")
