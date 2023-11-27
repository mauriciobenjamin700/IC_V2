from famacha import Famacha
from glob import glob
from cv2 import imwrite,imread
from os.path import basename, exists
from os import makedirs

DIR = '../Dados/'
DATASET = 'teste'
OUTPUT = DIR + 'segmentation'
FAIL = OUTPUT + '/fail'

if not exists(OUTPUT):
    makedirs(OUTPUT)
    
if not exists(FAIL):
    makedirs(FAIL)

fnames = glob(DIR + DATASET+'/*.jpg')

f = Famacha()

for file in fnames:
    image = f.segment_img(file)
    try:
        imwrite(OUTPUT+'/'+basename(file), image)
        print("\nTerminei ", file)
    except:
        print("\nFalhei ", file)
        imwrite(FAIL+'/'+basename(file), imread(file))
