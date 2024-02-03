import sys
from pathlib import Path
"""
file = Path(__file__).resolve(): Cria um objeto Path representando o caminho absoluto do arquivo atual (__file__ representa o caminho do arquivo do script atual). O método .resolve() retorna o caminho absoluto, resolvendo quaisquer links simbólicos ou caminhos relativos.
"""
file = Path(__file__).resolve()
root = file.parents[1] #parents[0] retorna o diretório pai, parents[1] o avo e assim por diante

#ROOT = dirname(realpath(__file__))

sys.path.append(str(root))

from models.msg import ola
def testar_ola():
    print(ola("mauricio"))
    
testar_ola()
    