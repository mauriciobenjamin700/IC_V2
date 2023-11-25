from glob import glob
from cv2 import imwrite, imread
from os.path import basename

# Obter lista de arquivos de sucesso e total
sucesso = set(glob("..\\Dados\\segmentation\\*.jpg"))
total = set(glob("..\\Dados\\teste\\*.jpg"))

# Encontrar falhas (arquivos presentes em total, mas não em sucesso)
falhas = total - sucesso

# Copiar falhas para a pasta de falhas
for f in falhas:
    imwrite(f"..\\Dados\\falhas\\{basename(f)}", imread(f))
