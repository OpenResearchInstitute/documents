# Julia fractal
# FB - 201003151
from PIL import Image
import random
# drawing area (xa < xb and ya < yb)
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 256 # iterations
# image size
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
# Julia set to draw
c = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)

for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1)  + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            if abs(z) > 2.0: break 
            z = z * z + c 
        r = i % 4 * 64
        g = i % 8 * 32
        b = i % 16 * 16
        image.putpixel((x, y), b * 65536 + g * 256 + r)

image.save("QSLjulia.png", "PNG")