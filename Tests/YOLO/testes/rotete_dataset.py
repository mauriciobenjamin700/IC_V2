from famacha import Famacha
import os
from glob import glob
import cv2

DIR_DATASET = '../Dados/'
DATA = 'redimensionados'
OUTPUT = 'rotacionados'

if not os.path.exists(DIR_DATASET+OUTPUT):
    os.makedirs(DIR_DATASET+OUTPUT)
    
data = glob(DIR_DATASET+DATA+'/*.jpg')

f = Famacha()


for fname in data: 
    
    img_name = os.path.basename(fname).split('.')[0]
    img_90,img_180,img_270 = f.rotate(fname)
    
    cv2.imwrite(filename=DIR_DATASET+OUTPUT+'/90_'+img_name + '.jpg',img=img_90)
    cv2.imwrite(filename=DIR_DATASET+OUTPUT+'/180_'+img_name + '.jpg',img=img_180)
    cv2.imwrite(filename=DIR_DATASET+OUTPUT+'/270_'+img_name + '.jpg',img=img_270)