from PIL import Image
im = Image.open("horse4.png")
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save("horse5.png")
