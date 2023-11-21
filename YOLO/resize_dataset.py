import os
from glob import glob
import cv2


DIR_DATASET = '../Dados/'
DATA = 'dados'
OUTPUT = 'redimensionados'

if not os.path.exists(DIR_DATASET+OUTPUT):
    os.makedirs(DIR_DATASET+OUTPUT)
    


data = glob(DIR_DATASET+DATA+'/*.jpg') + glob(DIR_DATASET+DATA+'/*.jpeg') + glob(DIR_DATASET+DATA+'/*.JPG')


for fname in data: 
    img_name = os.path.basename(fname).split('.')[0]

    cv2.imwrite(DIR_DATASET+OUTPUT+'/640x640'+img_name+'.jpg',cv2.resize(cv2.imread(fname),(640,640),interpolation=cv2.INTER_AREA))

    
    

    
