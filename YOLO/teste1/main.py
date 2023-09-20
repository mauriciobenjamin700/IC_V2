import cv2
import numpy as np
import os
from show import mostrar, blob_imagem,alturaXlargura
from work import deteccoes, funcoes_imagem



cfgPath = os.path.sep.join(['modelo', "cfg"])

labelsPath = os.path.sep.join([cfgPath, "coco.names"])

LABELS = open(labelsPath).read().strip().split("\n")

configPath = os.path.sep.join([cfgPath, "yolov4.cfg"])

weightsPath = os.path.sep.join(['modelo', "yolov4.weights"])

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