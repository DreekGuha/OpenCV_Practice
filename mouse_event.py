import cv2

# events= [i for i in dir(cv2) ]   # print all the methods of CV2
events= [i for i in dir(cv2) if 'EVENT' in i] # print all the methods of CV2 where "EVENT" keyword is present
print(events)
