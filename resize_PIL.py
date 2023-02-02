import os
from PIL import Image


input_dir = r'/home/vicrrs/PycharmProjects/Redimensionando/B'


output_dir = r'/home/vicrrs/PycharmProjects/Redimensionando/teste'


size = (128, 128)


for filename in os.listdir(input_dir):
    
    if not filename.endswith('.jpg') and not filename.endswith('.jpeg') and not filename.endswith('.png'):
        continue
    with Image.open(os.path.join(input_dir, filename)) as img:
        
        img = img.resize(size)
        
        img.save(os.path.join(output_dir, filename))
