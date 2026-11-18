# Draws the shape layer of the insert: two time bars on the dark C card (cyan = 600 s, magenta = 147 s),
# both growing at the same speed, so the short one finishes 4.1 times sooner. Shapes only, no text.
import os, cv2, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1920, 1080, 24, 20.5
PAPER = (0x0E, 0x0E, 0x0E)
def comp(r, g, b):
    # the mp4v writer encodes with BT.601 and the editor reads 1080p as BT.709: pre-compensate so the
    # bars come out as the brand colours (measured on a still: uncompensated cyan read #049EEB)
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    cb, cr = (b - y) / 1.8556, (r - y) / 1.5748
    r2, b2 = y + 1.402 * cr, y + 1.772 * cb
    g2 = (y - 0.299 * r2 - 0.114 * b2) / 0.587
    return tuple(int(max(0, min(255, round(v)))) for v in (b2, g2, r2))   # BGR
CYAN = comp(0x12, 0xA9, 0xE6)  # #12A9E6
MAG = comp(0xFF, 0x2D, 0x92)   # #FF2D92
SLUG = (0x8A, 0x8E, 0x8E)      # BGR of #8E8E8A
X0, X1 = 144, 1776
FULL = X1 - X0                 # 600 seconds
SHORT = int(round(FULL * 147 / 600.0))
ROW_A, ROW_B, BAR_H = 812, 900, 56
T_SHOW = 3.6                   # tracks appear with shot 2
T_A, GROW_A = 4.3, 3.0         # cyan grows over 3 s
RATE = FULL / GROW_A
T_B = 9.0                      # magenta starts, same rate
out = os.path.join(HERE, "bg.mp4")
vw = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
assert vw.isOpened(), "writer did not open"
n = int(round(DUR * FPS))
for f in range(n):
    t = f / FPS
    img = np.zeros((H, W, 3), np.uint8); img[:] = PAPER
    if t >= T_SHOW:
        for y in (ROW_A, ROW_B):
            cv2.rectangle(img, (X0, y + BAR_H + 6), (X1, y + BAR_H + 7), SLUG, -1)   # baseline hairline
            for k in range(7):                                                        # ticks, no numerals
                x = X0 + int(round(FULL * k / 6.0))
                cv2.rectangle(img, (x - 1, y + BAR_H + 6), (x, y + BAR_H + 18), SLUG, -1)
        wa = int(max(0.0, min(FULL, (t - T_A) * RATE)))
        if wa > 0:
            cv2.rectangle(img, (X0, ROW_A), (X0 + wa, ROW_A + BAR_H), CYAN, -1)
        wb = int(max(0.0, min(SHORT, (t - T_B) * RATE)))
        if wb > 0:
            cv2.rectangle(img, (X0, ROW_B), (X0 + wb, ROW_B + BAR_H), MAG, -1)
    vw.write(img)
vw.release()
print("wrote", out, n, "frames", os.path.getsize(out), "bytes; short bar px", SHORT)
