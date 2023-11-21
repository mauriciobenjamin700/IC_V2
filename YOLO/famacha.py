from ultralytics import YOLO
import os
from shutil import rmtree
from glob import glob
import cv2

class Famacha:

    
    def __init__(self, path_model='model_segment/weights/best.pt') -> None:
        self.model = YOLO(path_model)
        
    def predict_dir_image(self, list_fname,conf=0.5):
        results = self.model.predict(list_fname,conf=conf,boxes=False,max_det=2)
        
        json = {}
        
        for idx,result in enumerate(results):
            
            dic = dict()
            boxes = result.boxes.cpu().numpy()
    
            dic['xyxys'] = boxes.xyxy
            dic['confidences'] = boxes.conf
            dic['class_id'] = boxes.cls
            dic['masks'] = result.masks
            dic['probs'] = result.probs
            
            json[list_fname[idx]] = dic
            
        
        return json
            

    def predict_image(self, fname:str,conf:float=0.5):
        """
        Processa uma imagem e retorna um dicionário com os dados obtidos.
        O dicionário possui as seguintes chaves -> xyxys,confidences,class_id,masks,probs
        
        Parâmetros:
            fname::str: Nome de uma imagem processada para o recorte
            confiance::float: Grau de confiança que a rede usará para decidir as zonas de recorte,
            o valor de confiança pode varia entre 0 e 1.
            
        Retorno:
            dic::dict: Dicionário Contendos os dados obtidos no processamento
        """
        results = self.model.predict(fname,conf=conf,boxes=False,max_det=2)

        dic = dict()
        result = results[0]
        boxes = result.boxes.cpu().numpy()
        
        dic['xyxys'] = boxes.xyxy
        dic['confidences'] = boxes.conf
        dic['class_id'] = boxes.cls
        dic['masks'] = result.masks
        dic['probs'] = result.probs
        
        return dic
            
            
    def mark_image(self,fname, confiance=0.5):
        if os.path.exists('runs'):
            rmtree('runs')
        results = self.model.predict(fname,save=True,conf=confiance,max_det=2,show_conf=True,show_labels=True)
        del results
    
    def mark_dir_image(self,path, confiance=0.5):
        list_path = glob(os.path.join(path,'*.jpg'))
        if os.path.exists('runs'):
            rmtree('runs')
        results = self.model.predict(list_path,save=True,conf=confiance,max_det=2,show_conf=True,show_labels=True)
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
        result = self.model.predict(fname,conf=confiance,boxes=False,max_det=2,show_conf=False,show_labels=False)
        
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
    
    
    def resize(self,fname,width=640,height=640):
        img = cv2.resize(cv2.imread(fname),(width,height),interpolation=cv2.INTER_AREA)
        return img
    
    def rotate(self,fname)->tuple:
        
        img = cv2.imread(fname)

        (h, w) = img.shape[:2]

        center = (w / 2, h / 2)
        
        angle90 = 90
        angle180 = 180
        angle270 = 270
        
        scale = 1.0
        
        M = cv2.getRotationMatrix2D(center, angle90, scale)
        rotated90 = cv2.warpAffine(img, M, (h, w))
        
        M = cv2.getRotationMatrix2D(center, angle180, scale)
        rotated180 = cv2.warpAffine(img, M, (w, h))
        
        M = cv2.getRotationMatrix2D(center, angle270, scale)
        rotated270 = cv2.warpAffine(img, M, (h, w))
        
        return (rotated90,rotated180,rotated270)