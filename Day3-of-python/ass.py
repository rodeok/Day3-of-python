from PIL import Image,ImageFilter
before = Image.open("operator.jpg")
after = before.filter(ImageFilter.BoxBlur(9))
after.save("out.png")