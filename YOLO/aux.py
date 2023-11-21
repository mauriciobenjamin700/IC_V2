import cv2
def resize(fname,width=640,height=640):
        img = cv2.resize(cv2.imread(fname),(width,height),interpolation=cv2.INTER_AREA)
        return img
    

cv2.imwrite('1,1.jpg',resize('1.jpg'))
cv2.imwrite('1,2.jpg',cv2.resize(cv2.imread('1.jpg'),(640,640),interpolation=cv2.INTER_AREA))