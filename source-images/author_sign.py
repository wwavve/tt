import os
from PIL import Image, ImageDraw, ImageFont

# path = '/Users/nick/opt/source-images/'

files = []


def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    white = (255, 255, 255)
    font = ImageFont.truetype(
        f'{os.getcwd()}/arial/ArialRegular/ArialRegular.ttf',
        40)
    drawing.text(pos, text, fill=white, font=font)
    photo.show()
    photo.save(output_image_path)


if __name__ == '__main__':
    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            if '.jpg' in file:
                f1 = file.replace('-', ' ')
                text = ('\u00a9 ' + f1.replace('.jpg', ''))

                watermark_text(file, f'output-images/as_{file}',
                               text=text.title(),
                               pos=(0, 0))
