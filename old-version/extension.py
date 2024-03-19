import os

nome_do_arquivo = "abcsaxasdadadas2.jpeg"
nome_só = os.path.splitext(os.path.basename(nome_do_arquivo))[0]
último_caractere = nome_só[-1]

print(último_caractere)
