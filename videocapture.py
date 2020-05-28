import cv2,time

#method VideoCapture() to create a video capture object
video=cv2.VideoCapture(0)#either give the path to the video file or numbers. 0 means use the built in camera , 1 for external camera.
#if i have 2 external camers and i want use the 2nd one use 2

#frame is an numpy array it represents the first image that video captures
#check is booleantype, it returns true if python is able to read the  videocapture object
check,frame=video.read()
print(check)
print(frame)

time.sleep(3)#when we excute the code the, we will notice thatour cam light switches on for split seconds  and then it turns off .lets go ahead and add time using time module

cv2.imshow('image', frame)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()
