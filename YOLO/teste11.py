from famacha import Famacha
from os.path import exists
from os import makedirs

DIR = '..\\Dados\\'
DATASET = 'teste'
OUTPUT = 'segmentation'

if not exists(DIR+OUTPUT):
    makedirs(DIR+OUTPUT)


f = Famacha()

f.segment_dir_image(DIR + DATASET+'\\*.jpg',DIR+OUTPUT)
