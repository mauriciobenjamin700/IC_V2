#import sys
#from pathlib import Path
"""
file = Path(__file__).resolve(): Cria um objeto Path representando o caminho absoluto do arquivo atual (__file__ representa o caminho do arquivo do script atual). O método .resolve() retorna o caminho absoluto, resolvendo quaisquer links simbólicos ou caminhos relativos.
"""
#file = Path(__file__).resolve()
# root = file.parent,file.parents[2] #parents[0] retorna o diretório pai, parents[1] o avo e assim por diante

#ROOT = dirname(realpath(__file__))

#sys.path.append(str(file))

#o ponto significa que está importando de um arquivo na mesma pasta que o atual, só assim funciona no init
from .contas import *
from .msg import *