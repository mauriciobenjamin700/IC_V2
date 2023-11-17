from ultralytics import YOLO
import os
import cv2
import matplotlib.pyplot as plt
from newYaml import yaml_file


RAIZ = "datasets"
DATASET = "object_detect"
DIRETORIO_RAIZ = os.path.sep.join([RAIZ,DATASET])
OUTPUT = "model"
YAML_NAME = "dados.yaml"
TRAIN = os.path.sep.join(["train",''])
TEST = os.path.sep.join(["test/",''])
VALID= os.path.sep.join(["valid/",''])

#yaml_file(DIRETORIO_RAIZ,TRAIN, VALID, TEST,1,["EYE_MEMBRANE"],YAML_NAME)

#config_file = os.path.sep.join([DIRETORIO_RAIZ, YAML_NAME])

#load model
model = YOLO('yolov8s.yaml')

#train model
resultados = model.train(data=YAML_NAME, epochs=10, imgsz=640, name='yolov8s_modelo')

#output model
