import cv2
import matplotlib.pyplot as plt
import time
"""
def mostrar(img):
  fig = plt.gcf()
  fig.set_size_inches(16, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
"""
def alturaXlargura(img):
    
    H, W = img.shape[:2]
    
    print("\nAltura: " + str(H) + "\nLargura: " + str(W))
    return H,W

def calcProporcao(img):
    proporcao = img.shape[1] / img.shape[0]
    return proporcao

def redimensionar(img, largura_maxima = 600):
    #largura maxima garante que a imagem não vai ficar deformada
  if img.shape[1] > largura_maxima:
    proporcao = calcProporcao(img)
    imagem_largura = largura_maxima
    imagem_altura = int(imagem_largura / proporcao)
  else:
    imagem_largura = img.shape[1]
    imagem_altura = img.shape[0]

  img = cv2.resize(img, (imagem_largura, imagem_altura))
  return img


def blob_imagem(net, imagem, ln,mostrar_texto=True):
  inicio = time.time()

  blob = cv2.dnn.blobFromImage(imagem, 1 / 255.0, (416, 416), swapRB=True, crop=False)
  net.setInput(blob)
  layerOutputs = net.forward(ln)

  termino = time.time()

  if mostrar_texto:
    print("\nYOLO levou {:.2f} segundos\n".format(termino - inicio))

  return net, imagem, layerOutputs