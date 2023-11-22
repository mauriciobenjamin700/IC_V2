from famacha import Famacha
from glob import glob
from cv2 import imwrite
from os.path import basename,exists
from os import makedirs

DIR = '../Dados/'
DATASET = 'teste'
OUTPUT = 'segmentation/'

if not exists(DIR+OUTPUT):
    makedirs(DIR+OUTPUT)



fnames = glob(DIR + DATASET)
f = Famacha()

image = None

for file in fnames:
    image = f.segment_img(file)
    if image != None:
        imwrite(DIR+OUTPUT+basename(file),image)
        print("\nTerminei ",file)
    else:
        print("\nFalhei ",file)
