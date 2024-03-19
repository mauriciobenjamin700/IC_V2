import gdown

def driveFile(urlFile, outputName):
    gdown.download(urlFile, outputName, quiet=False)

if __name__ == '__main__':  
    # URL do arquivo no Google Drive
    url = "https://drive.google.com/u/0/uc?id=1kPKs0ZlEK5O_WbbTGSbiI1A3JI8C6UHc&export=download"

    # Nome do arquivo de saída
    output = 'Teste.zip'

    # Faça o download do arquivo
    gdown.download(url, output, quiet=False)
