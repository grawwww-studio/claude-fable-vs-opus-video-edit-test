import os, cv2
d = os.path.dirname(os.path.abspath(__file__))
for name in ("f2_380.png", "f3_400.png"):
    im = cv2.imread(os.path.join(d, name))
    for label, (x, y) in (("cyan bar", (800, 840)), ("magenta bar", (300, 928)), ("paper", (1000, 1040))):
        b, g, r = im[y, x]
        print(name, label, "#%02X%02X%02X" % (r, g, b))
