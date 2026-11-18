# Draws the shapes plate (bars only, no type) for the explainer: one frame per frame of the piece.
# Bar lengths are proportional to the measured seconds: 600 s = 1600 px, 147 s = 392 px.
import os, sys
import numpy as np
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, N = 1920, 1080, 24, 480
PAPER = (14, 14, 14)            # #0E0E0E (BGR)
CYAN = (230, 169, 18)           # #12A9E6
MAGENTA = (146, 45, 255)        # #FF2D92
SLUG = (138, 142, 142)          # #8E8E8A
X0, FULL = 160, 1600
L600, L147 = FULL, int(round(FULL * 147 / 600.0))
RATE = FULL / 1.25              # px per second: both bars fill at the same speed


def mix(c, a):
    return tuple(int(round(PAPER[i] + (c[i] - PAPER[i]) * a)) for i in range(3))


def track(img, y0, y1):
    # hairline track of the full 600-second length, with end ticks
    cv2.line(img, (X0, y1 + 14), (X0 + FULL, y1 + 14), mix(SLUG, 0.6), 2)
    for x in (X0, X0 + L147, X0 + FULL):
        cv2.line(img, (x, y1 + 6), (x, y1 + 22), mix(SLUG, 0.6), 2)


def bar(img, y0, y1, length, col):
    if length > 0:
        cv2.rectangle(img, (X0, y0), (X0 + int(length), y1), col, -1)


def grow(t, t0, target):
    return float(np.clip((t - t0) * RATE, 0, target))


def frame(i):
    t = i / FPS
    img = np.zeros((H, W, 3), np.uint8)
    img[:] = PAPER
    if 4.2 <= t < 8.6:                       # 600 seconds: the long bar fills with the count
        track(img, 840, 900)
        bar(img, 840, 900, grow(t, 5.0, L600), MAGENTA)
    elif 8.6 <= t < 13.0:                    # 147 seconds: the 600 bar stays as a ghost
        track(img, 840, 900)
        bar(img, 840, 900, L600, mix(MAGENTA, 0.22))
        bar(img, 840, 900, grow(t, 9.4, L147), CYAN)
    elif 13.0 <= t < 17.2:                   # both, one over the other
        track(img, 650, 700)
        bar(img, 580, 630, grow(t, 13.3, L600), MAGENTA)
        bar(img, 650, 700, grow(t, 13.3, L147), CYAN)
    return img


def main():
    out = os.path.join(HERE, "plate.mkv")
    vw = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*"FFV1"), FPS, (W, H))
    if not vw.isOpened():
        print("writer failed"); sys.exit(1)
    for i in range(N + 24):                  # one spare second at the end
        vw.write(frame(min(i, N - 1)))
    vw.release()
    for n in (156, 264, 372):
        cv2.imwrite(os.path.join(HERE, "plate_%d.png" % n), frame(n))
    cap = cv2.VideoCapture(out)
    print("frames", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), "fps", cap.get(cv2.CAP_PROP_FPS), os.path.getsize(out))


main()
