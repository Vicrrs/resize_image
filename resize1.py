import os
from PIL import Image

# specify the directory where the images are stored
input_dir = r'/home/vicrrs/PycharmProjects/Redimensionando/B'

# specify the directory where the resized images will be stored
output_dir = r'/home/vicrrs/PycharmProjects/Redimensionando/teste'

# specify the size to which the images should be resized
size = (128, 128)

# loop through all the images in the input directory
for filename in os.listdir(input_dir):
    # only process image files
    if not filename.endswith('.jpg') and not filename.endswith('.jpeg') and not filename.endswith('.png'):
        continue
    with Image.open(os.path.join(input_dir, filename)) as img:
        # resize the image
        img = img.resize(size)
        # save the resized image to the output directory
        img.save(os.path.join(output_dir, filename))
