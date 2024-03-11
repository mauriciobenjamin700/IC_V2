from os.path import basename,splitext,join
from numpy import ndarray, mean, median, std
from typing import List
from pandas import DataFrame

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




def save_results(
    df: DataFrame, 
    path: str = r"docs\classification\results", 
    name: str = "result",
    mode: str = ".csv" 
    ):
    
    """
    Salva um DataFrame no diretório escolhido com a formatação solicitada em mode, onde mode pode ser:
        ".csv"
        ".json"
        
    Args:
        df::DataFrame: DataFrame pandas como os dados resultados da extração de caracteristias
        path::str: Diretório de saida do arquivo que será gerado
        name::str: Nome do arquivo de saida
        mode::str: extensão do arquivo de saida
        
    Return:
        None
    """
    
    extensions = [".csv",".json"]
    
    if mode.lower() in extensions:
        match mode.lower():
            
            case  ".csv":
                df.to_csv(join(path,name+mode))
                
            case ".json":
                df.to_json(join(path,name+mode),indent=4)
                
    else:
        raise ValueError("Extensão invalida!\n Use algumas das possiveis na lista",extensions)