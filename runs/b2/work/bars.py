import numpy as np, cv2
# solid colour plates for bar tiles (BGR)
cyan = (0xE6, 0xA9, 0x12)      # #12A9E6
magenta = (0x92, 0x2D, 0xFF)   # #FF2D92
for name, c in (("bar_cyan", cyan), ("bar_magenta", magenta)):
    img = np.zeros((90, 1500, 3), np.uint8); img[:] = c
    cv2.imwrite(f"work/{name}.png", img)
print("ok")
