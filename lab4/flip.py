from PIL import Image
im = Image.open("horse1.png")
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save("horse2.png")
