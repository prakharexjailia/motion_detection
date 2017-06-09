import cv2
import time
import numpy as num
camrea = cv2.VideoCapture(0) #camera init

#user preferances threshold value will change with different camera.
thres = 80                                       #lower value motion detection will be more sensitive
motionSnapshot = False                           #detected motion image will be capture if this is true.

def timeStamp():
        return time.strftime(" %Y-%m-%d--%H-%M-%S")

def takeSnapshot():
        cv2.imwrite("image"+timeStamp()+".png",frame2)
        print("Image saved")
        
time.sleep(1)
        
while True:
        
        ret,frame1 = camrea.read()
	
        cv2.imshow("show",frame1)
        time.sleep(0.2)
        ret,frame2 = camrea.read()
        diff_img = cv2.subtract(frame1,frame2)
        # cv2.imshow('diff_img',diff_img)
        max_val = num.amax(diff_img)
        #print(max_val)
        if(max_val>=thres):
                print("motion happedned")
                                
                if(motionSnapshot == True):
                        takeSnapshot()
                        #time.sleep(1)
                #else:
                       # time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord("c"):
                takeSnapshot()
        if cv2.waitKey(2) & 0xFF == ord("q"):
                break

camrea.release()
cv2.destroyAllWindows()
