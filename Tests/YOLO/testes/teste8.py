from famacha import Famacha
import cv2
import numpy as np

f = Famacha()

dados = f.predict_image('1,1.jpg')

xy = dados["masks"]


img = cv2.imread("1,1.jpg")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Converter a lista de tuplas em um array numpy
pts = np.array([tuple(map(int, ponto)) for array in xy for ponto in array], dtype=np.int32)

# Desenhar a região de interesse na máscara
cv2.fillPoly(mask, [pts], (255))  # Preenche a região da máscara com branco

# Aplicar a máscara na imagem original
imagem_interesse = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Zona de Interesse', imagem_interesse)
cv2.waitKey(0)
cv2.destroyAllWindows()
