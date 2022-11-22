from PIL import Image

class Img:
    def __init__(self, width, height, color, text):
        self.width = width
        self.heigt = height
        self.color = color 
        self.img = Image.new('RGB', (self.width, self.height), color = self.color)
        self.img.save('linkedin-bg.png')
