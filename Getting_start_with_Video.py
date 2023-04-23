import  cv2

cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    #GRAY= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #To convert the video in Gray
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord("q"): #press q to exit the video
        break

cap.release()
cv2.destroyAllWindows()