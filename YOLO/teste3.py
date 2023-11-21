from famacha import Famacha
import os
from glob import glob
dados = '../Dados/Dedos'
import cv2

saida = "segmentacao"

if not os.path.exists(saida):
    os.makedirs(saida)
    
f = Famacha()

"""
1 - Ir na pasta onde tem as fotos
2 - Pegar o nome de todas as fotos que eu preciso
3 - Cortar as fotos
4 - Anoto o nome
5 - Salvo a foto
"""
names = glob(os.path.join(dados,'*.jpg'))

for name in names:
    print(f"Imagem: {name}\nBoxes -> {f.snip_img(name,0.5)}")
"""
for name in names:
    cv2.imwrite(os.path.join(saida,os.path.basename(name)) ,f.segmen_img(name,0.5))
    print(os.path.basename(name))
"""