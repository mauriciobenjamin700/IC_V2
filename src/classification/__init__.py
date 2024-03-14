from  os.path import dirname,abspath
import sys
# Obtém o diretório atual do script em execução
current_dir = dirname(abspath(__file__))
sys.path.append(current_dir)

from train_models import *
from use_models import *
from validat_models import *