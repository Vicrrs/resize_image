import os
import cv2

# especifique o diretório onde as imagens são armazenadas
input_dir = r'/media/vicrrs/5C38425238422B7A/PC_NOVO/dataset_mercosul/A'

# especifique o diretório onde as imagens redimensionadas serão armazenadas
output_dir = r'/media/vicrrs/5C38425238422B7A/PC_NOVO/dataset_mercosul/Alfabeto'

# especifique o tamanho para o qual as imagens devem ser redimensionadas
size = (128, 128)

# percorrer todas as imagens no diretório de entrada
for filename in os.listdir(input_dir):
    # processar apenas arquivos de imagem
    if not filename.endswith('.jpg') and not filename.endswith('.jpeg') and not filename.endswith('.png'):
        continue
    # lendo a imagem usando o OpenCV
    img = cv2.imread(os.path.join(input_dir, filename))
    # redimensionando a imagem
    img = cv2.resize(img, size)
    # salvando a imagem redimensionada no diretório de saída
    cv2.imwrite(os.path.join(output_dir, filename), img)
