"""montage.py OUT.jpg A.png B.png ...: stills side by side at 540 px wide each, to look at several at once."""
import sys, cv2, numpy as np

out, files = sys.argv[1], sys.argv[2:]
tiles = []
for f in files:
    im = cv2.imread(f)
    h, w = im.shape[:2]
    tiles.append(cv2.resize(im, (540, int(h * 540 / w)), interpolation=cv2.INTER_AREA))
cv2.imwrite(out, np.hstack(tiles))
print(out)
