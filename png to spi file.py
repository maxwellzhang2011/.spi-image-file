from PIL import Image
import dectolec as dtl

filename = input("the file name: ")
mfname = input("the file name that got maked: ")

image = Image.open(filename)


image = image.convert("RGBA")


width, height = image.size


rgb_values = []


with open(mfname + ".spi", "w") as f:
    for y in range(height):
        for x in range(width):
            r, g, b, a = image.getpixel((x, y))
            r = dtl.detolecnovo(r)
            g = dtl.detolecnovo(g)
            b = dtl.detolecnovo(b)
            a = dtl.detolecnovo(a)
            f.write(str(r))
            f.write(str(g))
            f.write(str(b))
            f.write(str(a))
        f.write("\n")