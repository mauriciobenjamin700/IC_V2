from famacha import Famacha
import cv2

PATH_MODEL = 'model_segment/weights/best.pt'

f = Famacha(path_model=PATH_MODEL)

x1,y1,x2,y2 = f.axis_image('1.jpg',0.8)

img = f.segmen_img('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
print(img.shape)
print(f"{x1} -> {y1}\n{x2} | {y2}")
new = cv2.rectangle(img=img,pt1=(x1,y1),pt2=(x2,y2),color=(0,255,0))
cv2.imshow("teste", new)
cv2.waitKey(0)
cv2.destroyAllWindows()

