import numpy as np
import cv2

def deteccoes(detection, threshold, caixas, confiancas, IDclasses,H,W):
  scores = detection[5:]
  classeID = np.argmax(scores)
  confianca = scores[classeID]

  if confianca > threshold:
      caixa = detection[0:4] * np.array([W, H, W, H])
      (centerX, centerY, width, height) = caixa.astype("int")
      x = int(centerX - (width / 2))
      y = int(centerY - (height / 2))

      caixas.append([x, y, int(width), int(height)])
      confiancas.append(float(confianca))
      IDclasses.append(classeID)

  return caixas, confiancas, IDclasses

def check_negativo(n):
  if (n < 0):
    return 0
  else:
    return n

def funcoes_imagem(imagem, i, confiancas, caixas, COLORS, LABELS, IDclasses,mostrar_texto=True):
  (x, y) = (caixas[i][0], caixas[i][1])
  (w, h) = (caixas[i][2], caixas[i][3])
  cor = [int(c) for c in COLORS[IDclasses[i]]]
  cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
  texto = "{}: {:.4f}".format(LABELS[IDclasses[i]], confiancas[i])
  if mostrar_texto:
    print("> " + texto)
    print(x,y,w,h)
  cv2.putText(imagem, texto, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

  return imagem,x,y,w,h