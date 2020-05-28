import cv2#importing opencv library

#step1:create a cascadeclassifier object and this xml haarcascade_frontalface_default.xml file contains the face features
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread ("passpic.jpg")
resized = cv2.resize(img, (600,600))

# cvtColor ---reading the image as black and white
#Using cv2.COLOR_BGR2GRAY color space
#Syntax: cv2.cvtColor(src, code): src It is the image whose color space is to be changed and code is the color space conversion code.
gray_img=cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

#step2:search for the coordinates of the image
#detectMultiScale---method to search for the face rectangle coordinates
#scaleFactor decrease the shape value by 5% until the face is found. smaller this value greater is the accuracy.
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)
#faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)

#rectangle--method to create a rectangle
#x,y,whh are the coordinates of the image
for x,y,w,h in faces:
    img1=cv2.rectangle(resized, (x,y), (x+w, y + h), (0,255,0), 3)
    
cv2.imshow('grayimage', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


