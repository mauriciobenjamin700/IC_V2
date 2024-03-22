from pickle import load
from pandas import DataFrame

def Load_model(name_model='Modelo.pkl'):
    """
    Carregar o modelo RandomForestClassifer salvo em um arquivo pkl e o retorna.
    
    Args:
        model_name::str: Nome do arquivo que será gerado
        
    Return:
        model::RF: Modelo RandomForestClassifer já treinado.
    """ 
    # 
    with open(name_model, 'rb') as arquivo:
        model = load(arquivo)
        return model

def useModel(modelo, df:DataFrame):
    
    predicts = []
    
    for _,row in df.iterrows():
        predicts.append(modelo.predict([row]))

    return predicts