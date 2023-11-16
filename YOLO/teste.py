from ultralytics import YOLO
import os
import shutil

#model = YOLO('yolov8s.yaml')

try:
    model = YOLO('model_test/weights/best.pt',task='segment')
    if os.path.exists('runs'):
        shutil.rmtree('runs')
    
    model.predict('1.jpg',save=True,conf=0.5)
except:
    print("falhei")


