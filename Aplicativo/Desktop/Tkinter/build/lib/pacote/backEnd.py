import pickle
from .extrac_features_03 import extract_one

def loadModel(name_model='Modelo_Teste.pkl'):
    # carregar o modelo salvo em um arquivo pkl
    with open(name_model, 'rb') as arquivo:
        modelo = pickle.load(arquivo)
        return modelo

def useModel(modelo, path):
    # Criar um novo DataFrame com o novo dado atraves de um imput do usuário
    while True:

        sinal, novo_dado = extract_one(path=path)

        if sinal:


            # Obter a previsão do modelo para o novo dado
            previsao = modelo.predict(novo_dado)

            # Imprimir a previsão
            resultado = bool(previsao)
            if resultado:
                return [True, True]
                #print('\nPrecisa de Vermifugação\n')
            else:
                return [True, False]
                #print('\nNão Precisa de vermifugação\n')

        else:
            return [False, False]
            #print('\nImagem não encontrada!\nTente Novamente!\n\n')
