from cv2 import resize
from typing import Tuple,List
from numpy import ndarray

def images(images:List[ndarray], size:Tuple[int,int] = (640,640))-> List[ndarray]:
    """
    Redimensiona uma lista de imagens para a proporção desejada
    
    Args:
        images::List[ndarray]: Lista de imagens no formato ndarray a serem redimensionadas
        size::Tuple[int,int]: Tupla contendo 2 valores usadaos para definir as novas dimensões, sendo eles respectivamente largura e altura
        
    Return:
        resized::List[ndarray]: Lista contendo as imagens redimensionadas
    """
    
    resized = []
    
    for imagem in images:
        resized.append(resize(imagem, size))
        
    return resized


