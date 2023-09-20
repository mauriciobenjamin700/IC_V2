import glob
import cv2
#import matplotlib.pyplot as plt

#retorna uma lista com matrizes (imagens)  lidar com opencv (BGR)
def lista_img(path="imagens"):
    string_imagens = glob.glob(f"{path}/*.jpg")

    imagens = []

    for img in string_imagens:
        imagens.append(cv2.imread(filename=img))

        return imagens

#retorna uma lista de strings onde cada string é formada por nome e extenção da respectiva imagem
def lista_nome_img(path="imagens"):
    string_full_imagens = glob.glob(f"{path}/*.jpg")

    string_imagens = []

    for full_string in string_full_imagens:
        string_imagens.append(full_string[(len(path)+1):])

    return string_imagens

#retorna uma lista de string, onde cada string é formada por diretorio, nome e extenção da imagem
def lista_local_img(path="imagens"):
    return glob.glob(f"{path}/*.jpg")
