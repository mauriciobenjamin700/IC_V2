from ultralytics import YOLO
import os
from shutil import rmtree
from glob import glob
import cv2

class Famacha:

    
    def __init__(self, path_model='model_segment/weights/best.pt') -> None:

        self.model = None
        self.load_model(path_model)
        
    def load_model(self, path_model)->bool:
        sinal = True
        try:
            self.model = YOLO('model_segment/weights/best.pt')
        except:
            sinal = False
            
        return sinal
    
    def predict_dir_image(self, list_fname,conf=0.5):
        results = self.model.predict(list_fname,conf=conf)

        xyxys = []
        confidences = []
        classes_id = []
        for result in results:
            boxes = result.boxes.cpu().numpy()
            
            xyxys.append(boxes.xyxy)
            confidences.append(boxes.conf)
            classes_id.append(boxes.cls)
            
        
        return (xyxys, confidences, classes_id)
    
    def predict_image(self, list_fname,conf=0.5):
        results = self.model.predict(list_fname,conf=conf)

        result = results[0]
        
        boxes = result.boxes.cpu().numpy()
        
        xyxys = boxes.xyxy
        confidences = boxes.conf
        classes_id = boxes.cls
        
    
        return (xyxys, confidences, classes_id)
            
            
    
    def mark_image(self,fname, confiance=0.5):
        if os.path.exists('runs'):
            rmtree('runs')
        results = self.model.predict(fname,save=True,conf=confiance)
        del results
    
    def mark_dir_image(self,path, confiance=0.5):
        list_path = glob(os.path.join(path,'*.jpg'))
        if os.path.exists('runs'):
            rmtree('runs')
        results = self.model.predict(list_path,save=True,conf=confiance)
        del results
        
    def axis_image(self,fname,confiance=0.5)->tuple:
        if os.path.exists('runs'):
            rmtree('runs')
        
        result = self.model.predict(fname,conf=confiance)
        
        boxes = result[0].boxes.cpu().numpy()
        
        xyxys = boxes.xyxy
        
        xyxy = xyxys[0]
        
        return (int(xyxy[0]),int(xyxy[1]),int(xyxy[2]),int(xyxy[3]))
    
    
    def segmen_img(self,fname, confiance=0.5):
        image = cv2.imread(fname)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        x1,y1,x2,y2 = self.axis_image(fname=fname,confiance=confiance)
        regiao_interesse = image[y1:y2, x1:x2]
        
        return regiao_interesse
    