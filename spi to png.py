from PIL import Image
import lectodec

spi_file = input("the spi file: ")
output_file = input("Output png: ")
if not output_file.lower().endswith(".png"):
    output_file += ".png"

pixels = []

with open(spi_file + ".spi", "r") as f:
    lines = f.readlines()

height = len(lines)
width = len(lines[0].strip()) // 8

for line in lines:
    line = line.strip()
    for i in range(0, len(line), 8):
        r = lectodec.lectodec(line[i:i+2])
        g = lectodec.lectodec(line[i+2:i+4])
        b = lectodec.lectodec(line[i+4:i+6])
        a = lectodec.lectodec(line[i+6:i+8])
        pixels.append((r, g, b, a))

image = Image.new("RGBA", (width, height))
image.putdata(pixels)
image.save(output_file)

print("end")