from  os.path import dirname,abspath
import sys
# Obtém o diretório atual do script em execução
current_dir = dirname(abspath(__file__))
sys.path.append(current_dir)