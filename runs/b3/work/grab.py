import os, cv2
here = os.path.dirname(os.path.abspath(__file__))
cap = cv2.VideoCapture(os.path.join(here, "..", "out", "b-explainer.mp4"))
for n in (300, 440):
    cap.set(cv2.CAP_PROP_POS_FRAMES, n)
    ok, img = cap.read()
    if ok:
        cv2.imwrite(os.path.join(here, "out%d.png" % n), cv2.resize(img, (960, 540)))
    print(n, ok)
