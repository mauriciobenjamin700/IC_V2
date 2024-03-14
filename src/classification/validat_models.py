from os.path import exists
from pandas import DataFrame
def List2Best(models_list,export:str = "",ascended: bool = False):
    """
    Recebe uma lista de tupas vindas das funções geradoras dos modelos
    retorna o melhor modelo e suas métricas
    
    Args:
        models_list::list: lista de tuplas, onde o primeiro elemento da lista é um modelo e os demas campos são suas métricas
        export::str: caso receba um diretório valido, exporta os resultados dos modelos para uma arquivo .csv
        ascended::bool: Caso seja verdadeiro a ordem dos modelos será crescente, caso contrario decrescente
        
    Return:
        best::model: Melhor modelo gerado
    """
    
    best_value = 0
    best = None
    
    not_best = []
    
    for model_info in models_list:
        if sum(model_info[1:]) > best_value:
            best_value = sum(model_info[1:])
            best = model_info[0]
        else:
            not_best.append(model_info)
    
    print(exists(export))
    if exists(export):
        df = DataFrame(not_best)
        df.to_csv(export)
        print("exportei")
    
    return best

