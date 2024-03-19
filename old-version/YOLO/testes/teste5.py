from famacha import Famacha
from glob import glob

DIR_DATASET = '../Dados/'
DATA = 'redimensionados'

data = glob(DIR_DATASET+DATA+'/*.jpg')

tam = len(data)

p1 = [data[i] for i in range(0, round(tam/2))]
p2 = [data[i] for i in range(round(tam/2), tam)]

f = Famacha()

f.mark_image(p1)
f.mark_image(p2)
