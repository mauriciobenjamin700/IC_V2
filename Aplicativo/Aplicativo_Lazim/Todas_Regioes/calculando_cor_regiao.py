import numpy as np
import cv2
import pandas as pd
from localizando import lista_local_img,lista_nome_img

def dados_gerados(path="imagens"):
    diretorio_imagens = lista_local_img(path=path)
    nome_imagens = lista_nome_img(path=path)

    #criando as estruturas necessárias para o nosso DataFrame
    #lista que armazenará uma lista de valores respectivos a imagem análisada
    lista_dados = []

    # Colunas que irão compor nossa DataFrame
    colunas = ['Nome_Imagem','Vermifuga','Media_Canal_R','Media_Canal_G','Media_Canal_B','Mediana_Canal_R','Mediana_Canal_G','Mediana_Canal_B','Desvio_Canal_R','Desvio_Canal_G','Desvio_Canal_B']

    #Indices do nosso DataFrame (poderia ser em ordem crescente por padrão mas iremos customizar)
    # a ideia de indicies foi abortada neste caso
    #indices = []

    #calculando os valores de cada imagem
    for i in range(0,len(diretorio_imagens)):

        imagem_BGR = cv2.imread(diretorio_imagens[i])

        imagem_RGB = cv2.cvtColor(imagem_BGR,cv2.COLOR_BGR2RGB)



        #Calculando a media dos canais de cor
        media_R = round(np.mean(imagem_RGB[:,:,0]))

        media_G = round(np.mean(imagem_RGB[:,:,1]))

        media_B = round(np.mean(imagem_RGB[:,:,2]))

        #calculando a mediana nos canais de cor
        mediana_R = round(np.median(imagem_RGB[:,:,0]))

        mediana_G = round(np.median(imagem_RGB[:,:,1]))

        mediana_B = round(np.median(imagem_RGB[:,:,2]))

        #calculando o desvio padrão nos canais de cor

        desvio_R = round(np.std(imagem_RGB[:,:,0]))

        desvio_G = round(np.std(imagem_RGB[:,:,1]))

        desvio_B = round(np.std(imagem_RGB[:,:,2]))

        #preenchendo os dados da imagem em uma lista  de listas

        vermifuga_S_N = int((nome_imagens[i])[-5])
        if vermifuga_S_N > 0 and vermifuga_S_N <3:
            resultado = False
        elif vermifuga_S_N > 2 and vermifuga_S_N <6:
            resultado = True
        else:
            resultado = 'Falha'

        lista_dados.append([nome_imagens[i],resultado,media_R,media_G,media_B,mediana_R,mediana_G,mediana_B,desvio_R,desvio_G,desvio_B])


    #criando um DataFrame para guardar os dados coletados

    df = pd.DataFrame(data=lista_dados,columns=colunas)

    return df



def dados_imagem_unica(path):
    """
    Esta função procura uma imagem nas referencias passadas
    se encontrar:
        retorna True e um DataFrame com os dados necessários dessa imagem
    se não encontrar:
        retorna False e uma string "Não encontrado"
    """

    #import warnings
    #warnings.filterwarnings("ignore")
    import os

    possivel_imagem_path = path

    if os.path.isfile(possivel_imagem_path):
       

        arquivo_exite = True
    else:
        arquivo_exite = False
 
    
    if arquivo_exite:
        

        #criando as estruturas necessárias para o nosso DataFrame
        #lista que armazenará uma lista de valores respectivos a imagem análisada

        lista_dados = []

        # Colunas que irão compor nossa DataFrame
        colunas = ['Media_Canal_R','Media_Canal_G','Media_Canal_B','Mediana_Canal_R','Mediana_Canal_G','Mediana_Canal_B','Desvio_Canal_R','Desvio_Canal_G','Desvio_Canal_B']

        #Indices do nosso DataFrame (poderia ser em ordem crescente por padrão mas iremos customizar)
        # a ideia de indicies foi abortada neste caso
        #indices = []

        #calculando os valores de cada imagem


        imagem_BGR = cv2.imread(possivel_imagem_path)

        imagem_RGB = cv2.cvtColor(imagem_BGR,cv2.COLOR_BGR2RGB)

        #Calculando a media dos canais de cor
        media_R = round(np.mean(imagem_RGB[:,:,0]))

        media_G = round(np.mean(imagem_RGB[:,:,1]))

        media_B = round(np.mean(imagem_RGB[:,:,2]))

        #calculando a mediana nos canais de cor
        mediana_R = round(np.median(imagem_RGB[:,:,0]))

        mediana_G = round(np.median(imagem_RGB[:,:,1]))

        mediana_B = round(np.median(imagem_RGB[:,:,2]))

        #calculando o desvio padrão nos canais de cor

        desvio_R = round(np.std(imagem_RGB[:,:,0]))

        desvio_G = round(np.std(imagem_RGB[:,:,1]))

        desvio_B = round(np.std(imagem_RGB[:,:,2]))

        #preenchendo os dados da imagem em uma lista  de listas
        lista_dados.append([media_R,media_G,media_B,mediana_R,mediana_G,mediana_B,desvio_R,desvio_G,desvio_B])


        #criando um DataFrame para guardar os dados coletados

        df = pd.DataFrame(data=lista_dados,columns=colunas)

        return True,df
    else:
        return False,"Não Encontrando"


if __name__ == '__main__':
    dados_imagem_unica('imagens_3','verde_3')