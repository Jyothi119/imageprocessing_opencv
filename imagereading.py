import cv2#importing opencv library

#img = cv2.imread ("passpic.jpg",1)#read the image in color format means RGB if it is a colored image it will be a 3d matrix

img = cv2.imread ("passpic.jpg",0)#read image in gray scale image or black and white image. if it is a colored image it will be a 2d matrix

resized=cv2.resize(img,(600,600))#resizing the image into 600x600

#resized=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))#to get half of the size of the image

print(type(resized))#to know the type

print(resized.shape)#to know the shape of the image

cv2.imshow("Image", resized)#to show the image and IMage is a name of the image i given

cv2.waitKey(0)#the moment the user press the any key it will close the window if we mention the time suppose cv2.waitKey(2000) after 2000 milli seconds it will close the window automatically

cv2.destroyAllWindows()#to destroy the windows
