import numpy as np
import cv2

#................................ program 1...............................................

# events= [i for i in dir(cv2) ]   # print all the methods of CV2
# events= [i for i in dir(cv2) if 'EVENT' in i] # print all the methods of CV2 where "EVENT" keyword is present
# print(events)

#................................ program 2...............................................

 # this program will print the axis value of the clicked portion
def click_event(event,x,y,flags,param):     # A function to print the x and  y axis when Left mouse button is clicked
    if event==cv2.EVENT_LBUTTONDOWN:
        # print(x,', ',y) # to print the co-ordinate in console
        font=cv2.FONT_ITALIC
        strXY= "("+str(x)+","+ str(y)+")"
        cv2.putText(img,strXY,(x,y),font,1,(0,0,0),2)
        cv2.imshow("Image",img)
img=cv2.imread("lena.jpg",1)
cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_event)  # Call the mouseclick function

cv2.waitKey(0)
cv2.destroyAllWindows()