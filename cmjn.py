from PIL import Image

image = Image.open("moon.jpg").convert("CMYK")
c, m, y, k = image.split()

c.save("cyan_layer.png")
m.save("magenta_layer.png")
y.save("yellow_layer.png")
k.save("black_layer.png")