from ultralytics import YOLO
import os
from shutil import rmtree
from glob import glob
import cv2

class Famacha:

    
    def __init__(self, path_model='model_segment/weights/best.pt') -> None:
        self.model = result = YOLO(path_model)
        
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

        dic = dict()
        result = results[0]
        
        boxes = result.boxes.cpu().numpy()
        
        xyxys = boxes.xyxy
        dic['confidences'] = boxes.conf
        dic['class_id'] = boxes.cls
        dic['masks'] = result.masks
        dic['probs'] = result.probs
        
        return (xyxys, confidences, classes_id, masks, probs)
            
            
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
        
    def axis_image(self,fname,confiance=0.5)->list:
        """
        Processa uma imagem e retorna os eixos x1,y1,x2,y2 que compõe os boxs que contem a zona de interesse da imagem.
        
        Parâmetros:
            fname::str: Nome de uma imagem processada para o recorte
            confiance::float: Grau de confiança que a rede usará para decidir as zonas de recorte,
            o valor de confiança pode varia entre 0 e 1.
        
        Retorno:
            xyxys::list: Lista contendo tuplas com os eixos da imagem que estão nossa zona de interesse ou
            lista vazia caso não encontre nada
    
        """
        xyxys = []
        result = self.model.predict(fname,conf=confiance)
        
        boxes = result[0].boxes.cpu().numpy()
        
        for xyxy in boxes.xyxy:
        
            xyxys.append((int(xyxy[0]),int(xyxy[1]),int(xyxy[2]),int(xyxy[3])))
        
        return xyxys
    
    #recorta a imagem
    def snip_img(self,fname:str, confiance:float=0.5):
        """
        Processa uma imagem e retorna os pixels recortados da imagem.
        Onde os pixels compõe zonas de interesse que a imagem pode vir a possuir
        
        Parâmetros:
            fname::str: Nome de uma imagem processada para o recorte
            confiance::float: Grau de confiança que a rede usará para decidir as zonas de recorte,
            o valor de confiança pode varia entre 0 e 1.
        
        Retorno:
            interest_region::list: Lista contendo as partes da imagem que estão nossa zona de interesse ou
            lista vazia caso não encontre nada
    
        """
        image = cv2.imread(fname)
        
        interest_region = []
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
         
        xyxys = self.axis_image(fname=fname,confiance=confiance)
        if len(xyxys) > 0:
            for xyxy in xyxys:
                x1,y1,x2,y2 = xyxy
                interest_region.append(image[y1:y2, x1:x2])
        
        return interest_region
    