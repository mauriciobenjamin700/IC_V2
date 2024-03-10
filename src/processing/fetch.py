from cv2 import imread,cvtColor,COLOR_BGR2RGB
from numpy import ndarray
from typing import List
from os.path import exists,join,basename
from glob import glob


def image(filename:str="image.jpg")->ndarray:
    """
    Retorna uma imagem RGB em formato ndarray com base no item passado
    
    Args:
        filename::str: Caminho para a imagem que será carregada
        
    Return:
        file::ndarray: Imagem RGB carregada
    """
    
    file = imread(filename)
    
    if file is not None:
        if file.shape[2] == 4: #se for RGBA vamos dercartar o canal A para economizar memória
            file = file[:,:,:3]
        file = cvtColor(file,COLOR_BGR2RGB)
        
    return file


def folder(foldername:str="images")->List[ndarray]:
    """
    Retorna uma lista de imagens ou uma lista vazia com base na pasta passada 
    
    Args:
        foldername::str: Caminho para a pasta que será acessada
        
    Return:
        images::List[ndarray]: Lista de imagens validas lida ou lista vazia caso não consiga ler
    """
    images = []
    labels = []
    
    if exists(foldername):
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff', '*.tif']
        
        files = []
            
        for e in extensions:
            files.extend(glob(join(foldername,e)))

        for file in files:
            images.append(image(file))
            labels.append(basename(file))
    return images,labels


if __name__ == "__main__":
    print(folder(r"Dados\dados")[1][300])