import pickle
from calculando_cor_regiao import dados_imagem_unica
"""
Para carregar o modelo salvo em um arquivo, você pode usar o método load do módulo pickle. O método load recebe como argumento o arquivo que você deseja desserializar.

Aqui está um exemplo de como carregar o modelo salvo em um arquivo pkl:

"""

# carregar o modelo salvo em um arquivo pkl
with open('modelo3_salvo.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

# Criar um novo DataFrame com o novo dado atraves de um imput do usuário
diretorio = input('Diretório da Imagem: ')
nome = input('Nome da Imagem: ')

novo_dado = dados_imagem_unica(diretorio, nome)



# Obter a previsão do modelo para o novo dado
previsao = modelo.predict(novo_dado)

# Imprimir a previsão
print(previsao)
