import numpy as np
import cv2

#................................ program 1...............................................

# events= [i for i in dir(cv2) ]   # print all the methods of CV2
# events= [i for i in dir(cv2) if 'EVENT' in i] # print all the methods of CV2 where "EVENT" keyword is present
# print(events)

#................................ program 2...............................................

 # this program will print the axis value of the clicked portion
# def click_event(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDOWN: # It will print the x and y axis when Left mouse button is clicked
#         # print(x,', ',y) # to print the (x,y) co-ordinate in console
#         font=cv2.FONT_ITALIC
#         strXY= "("+str(x)+","+ str(y)+")"
#         cv2.putText(img,strXY,(x,y),font,1,(0,0,0),2)
#         cv2.imshow("Image",img)
#     if event==cv2.EVENT_RBUTTONDOWN: # It will print the pixel value of the image when right mouse button is clicked
#         blue=img[y,x,0]
#         green=img[y,x,1]
#         red=img[y,x,2]
#         font = cv2.FONT_ITALIC
#         strBGR= "("+str(blue)+","+ str(green)+","+str(red)+")"
#         cv2.putText(img, strBGR, (x, y), font, 1, (255, 255, 255), 2)
#         cv2.imshow("Image", img)
# img=cv2.imread("lena.jpg",1)
# cv2.imshow("Image",img)
# cv2.setMouseCallback("Image",click_event)  # Call the mouseclick function
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#................................ program 3...............................................

# this program will draw a pattern on left mouse click

# def click_event(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),4,(255,255,255),-1) # to draw a point (circle) on click
#         points.append((x,y))
#         if len(points)>= 2:
#             cv2.line(img,points[-1],points[-2],(255,255,255),5) # to draw a line between last two points(circles)
#         cv2.imshow("Image",img)
#
# # img=cv2.imread("lena.jpg",1)
# img=np.zeros([512,512,3],np.uint8)
# cv2.imshow("Image",img)
# points=[]
# cv2.setMouseCallback("Image",click_event)  # Call the mouseclick function
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#................................ program 4...............................................

# This program will display the colour of the clicked point on a different window


def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green=img[y,x,1]
        red=img[y,x,2]
        colorwindow=np.zeros([512,512,3],np.uint8)
        colorwindow[:]=[blue,green,red] # assign the new colour into the new window
        cv2.imshow("color",colorwindow)

img=cv2.imread("lena.jpg",1)
# img=np.zeros([512,512,3],np.uint8)
cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_event)  # Call the mouseclick function

cv2.waitKey(0)
cv2.destroyAllWindows()