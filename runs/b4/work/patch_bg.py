import os, re
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "make_bg.py")
s = open(p).read()
s = s.replace('''CYAN = (0xE6, 0xA9, 0x12)      # BGR of #12A9E6
MAG = (0x92, 0x2D, 0xFF)       # BGR of #FF2D92
''', '''def comp(r, g, b):
    # the mp4v writer encodes with BT.601 and the editor reads 1080p as BT.709: pre-compensate so the
    # bars come out as the brand colours (measured on a still: uncompensated cyan read #049EEB)
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    cb, cr = (b - y) / 1.8556, (r - y) / 1.5748
    r2, b2 = y + 1.402 * cr, y + 1.772 * cb
    g2 = (y - 0.299 * r2 - 0.114 * b2) / 0.587
    return tuple(int(max(0, min(255, round(v)))) for v in (b2, g2, r2))   # BGR
CYAN = comp(0x12, 0xA9, 0xE6)  # #12A9E6
MAG = comp(0xFF, 0x2D, 0x92)   # #FF2D92
''')
open(p, "w").write(s)
print("patched", "def comp" in s)
