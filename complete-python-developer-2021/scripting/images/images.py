from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

filtered_img.save("blur.png", "png")
filtered_img_2 = img.convert('L')
filtered_img_2.save("grey.png", 'png')


box = (100, 100, 400, 400)
region = filtered_img_2.crop(box)
region.save("grey_crop.png", "png")

img = Image.open('./pokedex/astro.jpg')
new_img = img.resize((400, 400))
new_img.show()