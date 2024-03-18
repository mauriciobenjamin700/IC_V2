from os.path import exists, join
from pandas import DataFrame

def List2Best(models_list, export: str = "", name: str = "modelos.csv", reverse: bool = False):
    """
    Recebe uma lista de tupas vindas das funções geradoras dos modelos
    retorna o melhor modelo e suas métricas
    
    Args:
        models_list::list: lista de tuplas, onde o primeiro elemento da lista é um modelo e os demais campos são suas métricas
        export::str: caso receba um diretório valido, exporta os resultados dos modelos para uma arquivo .csv
        name::str: nome do arquivo de saida do CSV
       
    Return:
        best::model: Melhor modelo gerado
    """
    
    best_value = 0
    best = None
    
    results = []
    
    for model_info in models_list:
        value = sum(model_info[2:])
        if value > best_value:
            best_value = value
            best = model_info[0]
            
        aux = list(model_info)
        aux.append(value)
        results.append(aux)
    
    if len(export) > 0 and exists(export):
        columns = ['Modelo', 'Versão', 'Accuracy', 'Precision', 'Recall', 'F1', 'Kappa', 'Total']
        df = DataFrame(sorted(results, key=lambda x: x[-1], reverse=reverse), columns=columns)
        df.to_csv(join(export, name), index=False)
    
    return best
