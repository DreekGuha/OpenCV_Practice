import numpy as np
import  cv2

# img=np.zeros([512,512,3],np.uint8)
img=cv2.imread("lena.jpg",1)
img=cv2.line(img,(0,0),(255,255),(0,0,255),10)#To draw a Line
img=cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),10)#To draw a arrowed Line
img=cv2.rectangle(img,(55,55),(310,310),(255,255,255),5 ) #To draw a rectangle
img=cv2.circle(img,(100,100),100,(255,157,219),5,cv2.LINE_AA) #To draw a circle
img=cv2.putText(img,"My OpenCV Project",(10,500),cv2.FONT_ITALIC,1.5,(200,200,200), 3)#To write a text

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()