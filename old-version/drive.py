import gdown

# URL do arquivo no Google Drive
url = 'https://drive.google.com/uc?id=SEU_ID_DO_ARQUIVO'

# Nome do arquivo de saída
output = 'arquivo_de_saida.ext'

# Faça o download do arquivo
gdown.download(url, output, quiet=False)
