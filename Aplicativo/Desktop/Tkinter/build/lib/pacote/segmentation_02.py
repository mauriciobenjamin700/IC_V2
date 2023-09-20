import cv2
import numpy as np
def segmentation(rgb_image, limite_inferior = 5, limite_superior = 170):
    ''' 
    rgb_image: imagem RGB
    limite_inferior: limite inferior para considerar vermelho no canal H do HSV
    limite_superior: limite superior para considerar vermelho no canal H do HSV
    Retorna a imagem RGB com o pixels foram da região segmentada zerados
    '''
    
    #Convertendo a imagem para HSV
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    #Pegando canal H
    h_image = hsv_image[:,:,0]
    
    #Pegando valores menores que 10 e maiores que 170 do canal H, que representa vermelho o restante é serado
    mascara_binaria = np.zeros((h_image.shape[0],h_image.shape[1]),np.uint8)
    mascara_binaria[(h_image[:,:] <= limite_inferior) | (h_image[:,:] >= limite_superior)] = 1
    
    # Converte a máscara binária para o formato RGB
    mascara_binaria_rgb = cv2.cvtColor(mascara_binaria, cv2.COLOR_GRAY2RGB)
    
    return mascara_binaria_rgb*rgb_image

def save_img(rbg_img, name_img):
    
    cv2.imwrite(name_img,rbg_img)