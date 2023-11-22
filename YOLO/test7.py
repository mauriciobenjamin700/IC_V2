from famacha import Famacha
import cv2
import numpy as np

f = Famacha()

dados = f.predict_image('1,1.jpg')

xy = dados["masks"]


print(f'\nMascara-> {xy}\n')

img = cv2.imread("1,1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
segment = np.zeros(img.shape, np.uint8)

posicoes = [tuple(map(int, ponto)) for array in xy for ponto in array]
print(posicoes)



for pixel in posicoes:
    segment[pixel[0],pixel[1]] = 255
    #img[pixel[0],pixel[1]]
    
    
cv2.imshow('teste',segment)
cv2.waitKey(0)
cv2.destroyAllWindows()

