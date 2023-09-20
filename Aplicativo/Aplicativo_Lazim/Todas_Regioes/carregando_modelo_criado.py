import pickle
from calculando_cor_regiao import dados_imagem_unica


def modelo_famacha(path):
    posi = len(path)
    extensao = path[posi-4:posi]
    #print(extensao)

    if extensao == '.jpg' or extensao == '.JPG' or extensao == '.jpeg' or extensao == '.JPEG':

        with open('Modelo.pkl', 'rb') as arquivo:
            modelo = pickle.load(arquivo)

        sinal, novo_dado = dados_imagem_unica(path)

        if sinal:


            # Obter a previsão do modelo para o novo dado
            previsao = modelo.predict(novo_dado)

            # Imprimir a previsão
            resultado = bool(previsao)
            if resultado:
                return('\nPrecisa de Vermifugação\n')
            else:
                return('\nNão Precisa de vermifugação\n')

        else:
            return('\nImagem não encontrada!\nTente Novamente!\n\n')
        
    else:
        return 'Extenção Invalida\n Use JPG'

 