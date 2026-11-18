"""Draw the timing bars as a shapes-only plate (no text): 1920x1080, 24 fps, 9.6 s.
Magenta bar = 20 steps / 600 s, grows from 0.4 s to full over 2.5 s (time runs at one rate).
Cyan bar = 4-step LoRA / 147 s, grows from 4.9 s at the same rate, stops at 147/600 of the length."""
import os
import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1920, 1080, 24, 9.6
PAPER = (0x0E, 0x0E, 0x0E)
MAG = (0x92, 0x2D, 0xFF)   # BGR of #FF2D92
CYAN = (0xE6, 0xA9, 0x12)  # BGR of #12A9E6
SLUG = (0x8A, 0x8E, 0x8E)  # BGR of #8E8E8A

X0, FULL = 150, 960
BAR_H = 84
Y_MAG = 392          # aligned with the first figure row of the panel at y=300
Y_CYAN = 616         # aligned with the second figure row
RATE = FULL / 2.5    # px per second of "clock"


def ease(u):
    u = max(0.0, min(1.0, u))
    return 1 - (1 - u) ** 3


out = cv2.VideoWriter(os.path.join(HERE, "bars.mp4"), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
n = int(round(DUR * FPS))
for i in range(n):
    t = i / FPS
    img = np.full((H, W, 3), PAPER, np.uint8)
    # axis: a slug hairline at the start of the bars + faint tick marks along the full length
    cv2.line(img, (X0 - 14, Y_MAG - 40), (X0 - 14, Y_CYAN + BAR_H + 40), SLUG, 2)
    for k in range(0, 11):
        x = X0 + int(FULL * k / 10)
        cv2.line(img, (x, Y_CYAN + BAR_H + 30), (x, Y_CYAN + BAR_H + 40), SLUG, 2)
    # magenta: 600 s, full length
    lm = int(FULL * ease((t - 0.4) / 2.5))
    if lm > 0:
        cv2.rectangle(img, (X0, Y_MAG), (X0 + lm, Y_MAG + BAR_H), MAG, -1)
    # cyan: 147 s, same clock, stops at 147/600
    target = FULL * 147 / 600
    lc = int(target * ease((t - 4.9) / (2.5 * 147 / 600 + 0.25)))
    if lc > 0:
        cv2.rectangle(img, (X0, Y_CYAN), (X0 + lc, Y_CYAN + BAR_H), CYAN, -1)
    out.write(img)
out.release()
print("wrote", os.path.join(HERE, "bars.mp4"), n, "frames")
