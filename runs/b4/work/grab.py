import os, cv2
d = os.path.dirname(os.path.abspath(__file__))
cap = cv2.VideoCapture(os.path.join(d, "..", "out", "insert.mp4"))
tiles = []
for n in (40, 130, 222, 330, 380, 460):
    cap.set(cv2.CAP_PROP_POS_FRAMES, n)
    ok, im = cap.read()
    assert ok, n
    tiles.append(cv2.resize(im, (640, 360)))
sheet = cv2.vconcat([cv2.hconcat(tiles[:3]), cv2.hconcat(tiles[3:])])
cv2.imwrite(os.path.join(d, "sheet.png"), sheet)
print("ok", sheet.shape)
