import glob
import cv2


def lista_img(path="imagens"):
    """
    retorna uma lista com matrizes (imagens)  lidar com opencv (BGR)
    """
    string_imagens = glob.glob(f"{path}/*.jpg")

    imagens = []

    for img in string_imagens:
        bgr = cv2.imread(filename=img)
        rgb = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
        imagens.append(rgb)

    return imagens


def lista_nome_img(path="imagens"):
    #retorna uma lista de strings onde cada string é formada por nome e extenção da de uma imagem
    string_full_imagens = glob.glob(f"{path}/*.jpg")

    string_imagens = []

    for full_string in string_full_imagens:
        string_imagens.append(full_string[(len(path)+1):])

    return string_imagens


if __name__ == '__main__':
    print(lista_nome_img('imagens'))
