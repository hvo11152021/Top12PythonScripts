from PIL import Image

def jpg_to_png(IMG_PATH):
    img = Image.open(IMG_PATH).convert('RGB')
    img.save("Image_1.png", "PNG")

def png_to_img(PNG_PATH):
    img = Image.open(PNG_PATH).convert('RGB')
    img.save("Image_1.jpg", "JPEG")

png_to_img("file.png")
jpg_to_png("Image.jpg")