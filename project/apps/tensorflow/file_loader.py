from PIL import Image


class ImageLoader():

    def __call__(self, filename,):
        
        img = Image.open(filename[0])
        img = img.convert('L')

        return img