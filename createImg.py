from PIL import Image

def createImg(width, height, color, text):

    img = Image.new('RGB', (width, height), color)
    img.save('linkedin-bg.png')

