from ultralytics import YOLO
import os
import shutil
import cv2

#model = YOLO('yolov8s.yaml')

#try:
model = YOLO('model_segment/weights/best.pt')
if os.path.exists('runs'):
    shutil.rmtree('runs')

results = model.predict('1.jpg',save=True,conf=0.5)

xyxys = []
confidences = []
classes_id = []
for result in results:
    boxes = result.boxes.cpu().numpy()
    
    xyxys.append(boxes.xyxy)
    confidences.append(boxes.conf)
    classes_id.append(boxes.cls)
    
    print('dados: ',xyxys, confidences, classes_id)
    
    
    """ Pega os eixos xy, largura e algura para desenhar uma box
    xyxys = boxes.xyxy
    print(xyxys)
    
    for xyxy in xyxys:
        img = cv2.imread('1.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        new = cv2.rectangle(img=img,pt1=(int(xyxy[0]),int(xyxy[1])),pt2=(int(xyxy[2]),int(xyxy[3])),color=(0,255,0))
        cv2.imshow("teste", new)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    """        
#except:
#    print("falhei")


