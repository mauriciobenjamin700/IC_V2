from numpy import ndarray, mean, median, std
from typing import List
from pandas import DataFrame
from os.path import basename,splitext

def train(images:List[ndarray],labels:List[str])->DataFrame:
    """
    Extrai as caracteristica () de uma base de dados passada como parâmetro e 
    arquiva os resultados em um DF
    
    Args:
       images::List[ndarray]: Lista de imagens que serão processadas
       Labels::List[str]: Lista com os rotulos de cada imagem (nome contendo grau famacha)
    
    Return:
        df::DataFrame: DataFrame pandas contendo os resultados da extração.
    """

    lista_dados = []

    colunas = ['Name','FAMACHA','Mean_R','Mean_G','Mean_B','Median_R','Median_G','Median_B','Std_R','Std_G','Std_B']


    for i in range(0,len(images),1):
        
        image_RGB = images[i]
        
        # canais de cor com valor zero serão ignorados, pois a segmentação garante que a zona de interesse não tenha valor 0
        
        # Calculando a médianos canais de cor 
        mean_R = round(mean(image_RGB[image_RGB[:,:,0]!= 0, 0]),2)
        mean_G = round(mean(image_RGB[image_RGB[:,:,1]!= 0, 1]),2)
        mean_B = round(mean(image_RGB[image_RGB[:,:,2]!= 0, 2]),2)

        #calculando a mediana nos canais de cor
        median_R = round(median(image_RGB[image_RGB[:,:,0]!= 0, 0]),2)
        median_G = round(median(image_RGB[image_RGB[:,:,1]!= 0, 1]),2)
        median_B = round(median(image_RGB[image_RGB[:,:,2]!= 0, 2]),2)

        #calculando o desvio padrão nos canais de cor
        std_R = round(std(image_RGB[image_RGB[:,:,0]!= 0, 0]),2)
        std_G = round(std(image_RGB[image_RGB[:,:,1]!= 0, 1]),2)
        std_B = round(std(image_RGB[image_RGB[:,:,2]!= 0, 2]),2)

        name = basename(labels[i])
        
        """
        separa o nome do arquivo pela extensão e pega o ultimo caractere do nome
        dessa forma conseguimos obter o número que identifica o grau famacha do animal
        """
        grau = splitext(name)[0][-1]
        # se as imagens estiverem rotuladas corretamente, então vamos capturar o grão
        if grau.isnumeric():
            famacha = int(grau)
        # se não estiver rotulado corretamente, então vamos atribuir a flag -1 para erros
        else:
            famacha = -1

        #se o famacha estiver em 1 ou 2, então animal está saudavel
        if famacha > 0 and famacha <3:
            status = 0
        #sse o famacha estiver entre 2 e 5 então o animal está doente
        elif famacha > 2 and famacha <6:
            status = 1
        #se não for nenhum dos casos então houve uma falha na anotação
        else:
            status = -1
            

        lista_dados.append([name,status,mean_R,mean_G,mean_B,median_R,median_G,median_B,std_R,std_G,std_B])


    df = DataFrame(data=lista_dados,columns=colunas)

    return df


def oneORmore(images:List[ndarray])->DataFrame:
    """
    Extrai as caracteristica de uma lista de imagens contendo uma ou mais imagens 
    e arquiva os resultados em um DataFrame Pandas

    Args:
        images::List[ndarray]: Lista de imagens que serão processadas

    Returns:
        df::DataFrame: DataFrame pandas contendo os resultados da extração.
    """

    lista_dados = []

    colunas = ['Mean_R','Mean_G','Mean_B','Median_R','Median_G','Median_B','Std_R','Std_G','Std_B']


    for image_RGB in images:
        
        # canais de cor com valor zero serão ignorados, pois a segmentação garante que a zona de interesse não tenha valor 0
        
        # Calculando a médianos canais de cor 
        mean_R = round(mean(image_RGB[image_RGB[:,:,0]!= 0, 0]),2)
        mean_G = round(mean(image_RGB[image_RGB[:,:,1]!= 0, 1]),2)
        mean_B = round(mean(image_RGB[image_RGB[:,:,2]!= 0, 2]),2)

        #calculando a mediana nos canais de cor
        median_R = round(median(image_RGB[image_RGB[:,:,0]!= 0, 0]),2)
        median_G = round(median(image_RGB[image_RGB[:,:,1]!= 0, 1]),2)
        median_B = round(median(image_RGB[image_RGB[:,:,2]!= 0, 2]),2)

        #calculando o desvio padrão nos canais de cor
        std_R = round(std(image_RGB[image_RGB[:,:,0]!= 0, 0]),2)
        std_G = round(std(image_RGB[image_RGB[:,:,1]!= 0, 1]),2)
        std_B = round(std(image_RGB[image_RGB[:,:,2]!= 0, 2]),2)

        lista_dados.append([mean_R,mean_G,mean_B,median_R,mean_G,median_B,std_R,std_G,std_B])

    df = DataFrame(data=lista_dados,columns=colunas)

    return df
