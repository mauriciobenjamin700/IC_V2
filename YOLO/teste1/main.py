import cv2
import numpy as np
import os
import zipfile
from show import mostrar, blob_imagem,alturaXlargura
from work import deteccoes, funcoes_imagem
from drive import driveFile

yolov4URL = "https://drive.google.com/u/0/uc?id=1kPKs0ZlEK5O_WbbTGSbiI1A3JI8C6UHc&export=download"

driveFile(yolov4URL,"modelo.zip")

zip_object = zipfile.ZipFile(file="modelo.zip", mode='r')
zip_object.extractall('./')
zip_object.close()

print("Terminei de extrair")

try:

  

  labelsPath = os.path.sep.join(["cfg", "coco.names"])

  LABELS = open(labelsPath).read().strip().split("\n")

  configPath = os.path.sep.join(["cfg", "yolov4.cfg"])

  weightsPath = "yolov4.weights"

  net = cv2.dnn.readNet(configPath, weightsPath)

  np.random.seed(42)
  COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

  ln = net.getLayerNames()
  #print("Todas as camadas (layers):")
  #print(ln)
  #print("Total: "+ str(len(ln)))
  #print("Camadas de saída: ")
  #print(net.getUnconnectedOutLayers())
  ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]
  #print(ln)

  imagePath = os.path.sep.join(['imagens', "cachorros02.jpg"])

  imagem = cv2.imread(imagePath)
  mostrar(imagem)


  net, imagem, layerOutputs = blob_imagem(net, imagem,ln)

  threshold = 0.5
  threshold_NMS = 0.3
  caixas = []
  confiancas = []
  IDclasses = []

  H,W = alturaXlargura(imagem)

  for output in layerOutputs:
      for detection in output:
          caixas, confiancas, IDclasses = deteccoes(detection, threshold, caixas, confiancas, IDclasses,H,W)
          
  objs = cv2.dnn.NMSBoxes(caixas, confiancas, threshold, threshold_NMS)

  print("Objetos detectados: " + str(len(objs)))

  if len(objs) > 0:
    for i in objs.flatten():
      imagem, x, y, w, h = funcoes_imagem(imagem, i, confiancas, caixas, COLORS, LABELS,IDclasses)
      objeto = imagem[y:y + h, x:x + w]
      cv2.imshow('Teste',objeto)
      cv2.destroyAllWindows()
      
  mostrar(imagem)

except:
  print("Deu erro")