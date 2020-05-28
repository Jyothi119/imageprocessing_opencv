Opencv
1.Opencv-python is a library of python used to solve computer vision problems.
2.All the opencv array structures are converted to and from numpy arrays.
3.Any image is first converted into numpy array or numpy matrix.	

How we can read an image :
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
output:
<class 'numpy.ndarray'>
(600, 600, 3)
It will display the image

Face detection using open cv:
step1.create a cascade amplifier it will contain the features of the face: the code will determine where is the face
step2: OpenCV will read an image and the features file: it will convert into numpy array and it will search for the rows and columns of the face numpy ndarray(The face rectangle coordinates)
step3: Display the image with the rectangular face box.
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
output:
<class 'numpy.ndarray'>
[[227  70 187 187]#coordinates of the image
 [154 255  62  62]]

Capturing video: capturing video with computer webcam
I am using loops to build a window where images will appear really fast, so that we can see it is a video.
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
output:
True
[[[175 177 150]
  [177 179 152]
  [179 181 153]
  ...
  [207 197 159]
  [206 196 158]
  [202 192 155]]

 [[186 180 148]
  [186 179 149]
  [185 178 149]
  ...
  [208 199 159]
  [209 200 160]
  [210 201 161]]

 [[177 178 146]
  [179 178 146]
  [182 178 146]
  ...
  [206 199 158]
  [208 201 161]
  [208 201 161]]

 ...

 [[ 73  77  63]
  [ 73  76  63]
  [ 71  74  62]
  ...
  [108 102 101]
  [106 101 100]
  [103  99  97]]

 [[ 82  73  60]
  [ 78  71  62]
  [ 74  69  62]
  ...
  [109 106  90]
  [106 104  86]
  [105 103  84]]

 [[ 76  72  59]
  [ 74  71  60]
  [ 71  68  59]
  ...
  [106  98  99]
  [102  95  95]
  [101  94  94]]]

Process finished with exit code -1
It will capture the picture in the video

Capturing the video, instead of first image/frame of the video:
import cv2,time

video = cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('capture', gray)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
ouput:
C:\Users\Daddy\anaconda3\python.exe C:/Users/Daddy/PycharmProjects/speech_recog/capturingthevideo.py
[[[177 192 177]
  [180 194 179]
  [181 194 179]
  ...
  [202 184 165]
  [202 183 164]
  [203 184 165]]

 [[184 190 185]
  [188 193 186]
  [190 194 185]
  ...
  [195 186 167]
  [192 183 163]
  [192 183 163]]

 [[186 189 177]
  [181 184 173]
  [179 182 170]
  ...
  [200 189 165]
  [201 191 165]
  [200 190 163]]

 ...

 [[136 132 118]
  [136 132 122]
  [135 132 125]
  ...
  [ 50  45  49]
  [ 53  48  51]
  [ 56  50  53]]

 [[144 131 118]
  [143 130 118]
  [143 129 119]
  ...
  [ 48  52  51]
  [ 49  54  54]
  [ 50  55  55]]

 [[135 122 119]
  [139 125 123]
  [143 127 126]
  ...
  [ 48  52  55]
  [ 55  57  59]
  [ 56  58  60]]]
[[[185 188 176]
  [185 188 176]
  [189 191 180]
  ...
  [197 190 159]
  [199 192 161]
  [199 192 161]]

 [[193 189 174]
  [192 190 178]
  [192 192 183]
  ...
  [201 189 162]
  [201 189 162]
  [200 187 161]]

 [[185 184 168]
  [185 185 169]
  [190 191 175]
  ...
  [205 189 161]
  [207 189 161]
  [205 186 158]]

 ...

 [[132 132 130]
  [134 132 130]
  [135 131 129]
  ...
  [ 45  43  49]
  [ 49  45  50]
  [ 55  51  56]]

 [[135 133 133]
  [135 133 131]
  [131 130 126]
  ...
  [ 45  45  47]
  [ 50  50  52]
  [ 56  55  58]]

 [[128 128 119]
  [126 125 116]
  [127 127 117]
  ...
  [ 49  49  50]
  [ 54  54  54]
  [ 58  58  58]]]
[[[195 192 153]
  [196 191 151]
  [196 189 151]
  ...
  [192 192 171]
  [193 193 172]
  [193 193 172]]

 [[192 189 182]
  [192 188 178]
  [194 190 177]
  ...
  [199 190 170]
  [195 186 167]
  [198 189 169]]

 [[194 187 186]
  [196 189 183]
  [197 190 180]
  ...
  [201 190 159]
  [201 190 159]
  [201 190 159]]

 ...

 [[136 130 108]
  [135 129 106]
  [134 128 105]
  ...
  [ 45  44  51]
  [ 47  45  52]
  [ 49  47  54]]

 [[147 123 118]
  [145 122 117]
  [145 123 118]
  ...
  [ 45  44  49]
  [ 49  48  53]
  [ 52  51  56]]

 [[142 129 116]
  [138 125 113]
  [139 126 114]
  ...
  [ 49  47  56]
  [ 54  51  61]
  [ 56  54  63]]]
[[[187 189 182]
  [187 190 179]
  [187 191 177]
  ...
  [203 192 160]
  [206 195 162]
  [207 196 163]]

 [[187 187 178]
  [190 190 178]
  [197 196 183]
  ...
  [204 193 159]
  [206 194 161]
  [205 192 159]]

 [[191 185 174]
  [191 185 172]
  [191 186 170]
  ...
  [199 193 161]
  [200 194 162]
  [200 194 162]]

 ...

 [[138 134 121]
  [139 135 122]
  [140 136 123]
  ...
  [ 42  47  57]
  [ 45  50  57]
  [ 49  54  60]]

 [[143 135 122]
  [143 135 123]
  [144 136 125]
  ...
  [ 48  49  55]
  [ 50  51  58]
  [ 54  55  61]]

 [[135 139 121]
  [135 137 123]
  [135 135 126]
  ...
  [ 53  46  59]
  [ 60  50  64]
  [ 66  56  70]]]
[[[180 183 171]
  [185 188 176]
  [191 194 182]
  ...
  [200 191 161]
  [200 190 164]
  [200 190 164]]

 [[187 188 186]
  [189 189 186]
  [192 193 189]
  ...
  [201 191 164]
  [202 192 166]
  [202 192 166]]

 [[190 192 181]
  [190 191 181]
  [190 189 180]
  ...
  [212 198 170]
  [209 195 166]
  [206 192 164]]

 ...

 [[137 133 131]
  [138 134 132]
  [138 134 132]
  ...
  [ 49  47  56]
  [ 51  50  57]
  [ 56  54  61]]

 [[142 135 129]
  [139 136 131]
  [133 134 129]
  ...
  [ 44  49  55]
  [ 45  53  59]
  [ 48  56  62]]

 [[123 122 116]
  [133 132 125]
  [140 137 131]
  ...
  [ 53  46  64]
  [ 57  50  69]
  [ 61  55  74]]]
[[[189 192 178]
  [187 191 177]
  [186 189 176]
  ...
  [206 189 158]
  [206 188 156]
  [206 188 156]]

 [[192 192 181]
  [193 193 182]
  [194 195 183]
  ...
  [203 192 161]
  [206 195 162]
  [207 196 163]]

 [[187 189 182]
  [187 189 182]
  [187 190 180]
  ...
  [205 196 164]
  [207 199 165]
  [206 197 164]]

 ...

 [[142 136 114]
  [141 135 112]
  [142 136 114]
  ...
  [ 57  45  58]
  [ 61  49  61]
  [ 64  52  65]]

 [[148 135 115]
  [151 137 118]
  [153 139 120]
  ...
  [ 57  46  61]
  [ 63  51  66]
  [ 66  53  68]]

 [[145 131 112]
  [146 132 113]
  [147 134 114]
  ...
  [ 52  55  65]
  [ 51  58  68]
  [ 52  59  70]]]
[[[189 192 178]
  [187 191 177]
  [186 189 176]
  ...
  [206 189 158]
  [206 188 156]
  [206 188 156]]

 [[192 192 181]
  [193 193 182]
  [194 195 183]
  ...
  [203 192 161]
  [206 195 162]
  [207 196 163]]

 [[187 189 182]
  [187 189 182]
  [187 190 180]
  ...
  [205 196 164]
  [207 199 165]
  [206 197 164]]

 ...

 [[142 136 114]
  [141 135 112]
  [142 136 114]
  ...
  [ 57  45  58]
  [ 61  49  61]
  [ 64  52  65]]

 [[148 135 115]
  [151 137 118]
  [153 139 120]
  ...
  [ 57  46  61]
  [ 63  51  66]
  [ 66  53  68]]

 [[145 131 112]
  [146 132 113]
  [147 134 114]
  ...
  [ 52  55  65]
  [ 51  58  68]
  [ 52  59  70]]]
[[[189 193 186]
  [189 193 185]
  [189 193 184]
  ...
  [198 190 168]
  [199 193 171]
  [198 192 170]]

 [[187 190 180]
  [188 191 181]
  [190 192 183]
  ...
  [198 194 168]
  [197 194 169]
  [197 194 169]]

 [[186 191 181]
  [185 189 179]
  [185 187 178]
  ...
  [202 193 162]
  [203 195 164]
  [203 195 164]]

 ...

 [[136 132 130]
  [138 134 133]
  [139 135 135]
  ...
  [ 47  47  51]
  [ 51  50  55]
  [ 57  56  61]]

 [[141 129 121]
  [142 130 123]
  [145 133 127]
  ...
  [ 50  46  58]
  [ 55  50  61]
  [ 57  52  64]]

 [[122 124 117]
  [129 130 123]
  [134 133 126]
  ...
  [ 54  53  55]
  [ 56  55  58]
  [ 59  59  61]]]
[[[175 184 174]
  [181 187 175]
  [186 189 176]
  ...
  [203 194 160]
  [203 193 159]
  [203 193 159]]

 [[185 197 184]
  [194 201 188]
  [196 199 183]
  ...
  [196 193 159]
  [195 193 159]
  [195 193 159]]

 [[183 196 186]
  [182 196 181]
  [182 197 175]
  ...
  [206 192 159]
  [204 191 158]
  [204 191 158]]

 ...

 [[144 137 121]
  [144 135 123]
  [142 133 124]
  ...
  [ 44  47  53]
  [ 42  49  55]
  [ 45  53  59]]

 [[144 133 121]
  [143 134 121]
  [143 135 122]
  ...
  [ 48  45  57]
  [ 50  47  59]
  [ 54  51  63]]

 [[130 129 124]
  [136 135 130]
  [137 136 130]
  ...
  [ 50  48  57]
  [ 54  51  61]
  [ 56  54  63]]]
[[[184 187 184]
  [185 189 184]
  [186 190 183]
  ...
  [196 196 162]
  [194 195 161]
  [192 194 159]]

 [[190 192 183]
  [187 190 180]
  [187 190 180]
  ...
  [195 194 167]
  [192 193 168]
  [193 194 169]]

 [[191 191 180]
  [187 188 176]
  [187 188 176]
  ...
  [202 194 165]
  [201 194 167]
  [202 195 168]]

 ...

 [[142 131 118]
  [142 130 121]
  [142 130 124]
  ...
  [ 48  49  54]
  [ 51  53  57]
  [ 55  56  61]]

 [[147 134 112]
  [144 134 113]
  [142 135 115]
  ...
  [ 46  53  54]
  [ 48  55  57]
  [ 52  58  60]]

 [[136 133 115]
  [136 134 116]
  [137 137 118]
  ...
  [ 52  51  57]
  [ 55  53  60]
  [ 57  55  63]]]
[[[184 187 184]
  [185 189 184]
  [186 190 183]
  ...
  [196 196 162]
  [194 195 161]
  [192 194 159]]

 [[190 192 183]
  [187 190 180]
  [187 190 180]
  ...
  [195 194 167]
  [192 193 168]
  [193 194 169]]

 [[191 191 180]
  [187 188 176]
  [187 188 176]
  ...
  [202 194 165]
  [201 194 167]
  [202 195 168]]

 ...

 [[142 131 118]
  [142 130 121]
  [142 130 124]
  ...
  [ 48  49  54]
  [ 51  53  57]
  [ 55  56  61]]

 [[147 134 112]
  [144 134 113]
  [142 135 115]
  ...
  [ 46  53  54]
  [ 48  55  57]
  [ 52  58  60]]

 [[136 133 115]
  [136 134 116]
  [137 137 118]
  ...
  [ 52  51  57]
  [ 55  53  60]
  [ 57  55  63]]]
[[[189 191 180]
  [190 192 181]
  [191 194 182]
  ...
  [203 192 163]
  [203 192 163]
  [202 190 162]]

 [[192 194 174]
  [191 193 172]
  [190 192 171]
  ...
  [200 191 162]
  [201 192 163]
  [201 192 163]]

 [[190 191 184]
  [190 191 184]
  [189 190 183]
  ...
  [204 193 163]
  [204 193 164]
  [203 191 163]]

 ...

 [[121 129 122]
  [124 130 123]
  [128 132 125]
  ...
  [ 53  51  58]
  [ 55  53  60]
  [ 57  55  62]]

 [[127 130 118]
  [132 134 122]
  [132 134 123]
  ...
  [ 53  51  63]
  [ 54  53  65]
  [ 56  56  67]]

 [[126 128 119]
  [129 132 121]
  [133 135 124]
  ...
  [ 54  52  59]
  [ 56  54  61]
  [ 59  58  65]]]
[[[189 191 180]
  [190 192 181]
  [191 194 182]
  ...
  [203 192 163]
  [203 192 163]
  [202 190 162]]

 [[192 194 174]
  [191 193 172]
  [190 192 171]
  ...
  [200 191 162]
  [201 192 163]
  [201 192 163]]

 [[190 191 184]
  [190 191 184]
  [189 190 183]
  ...
  [204 193 163]
  [204 193 164]
  [203 191 163]]

 ...

 [[121 129 122]
  [124 130 123]
  [128 132 125]
  ...
  [ 53  51  58]
  [ 55  53  60]
  [ 57  55  62]]

 [[127 130 118]
  [132 134 122]
  [132 134 123]
  ...
  [ 53  51  63]
  [ 54  53  65]
  [ 56  56  67]]

 [[126 128 119]
  [129 132 121]
  [133 135 124]
  ...
  [ 54  52  59]
  [ 56  54  61]
  [ 59  58  65]]]
[[[189 188 173]
  [192 191 175]
  [195 194 178]
  ...
  [201 190 158]
  [202 191 158]
  [201 190 157]]

 [[190 192 181]
  [189 191 180]
  [191 194 182]
  ...
  [201 192 161]
  [202 193 162]
  [201 192 161]]

 [[186 190 174]
  [187 191 175]
  [189 192 176]
  ...
  [204 195 164]
  [203 195 164]
  [201 192 161]]

 ...

 [[119 129 107]
  [127 134 113]
  [133 138 117]
  ...
  [ 50  56  57]
  [ 52  58  60]
  [ 53  60  61]]

 [[124 129 115]
  [129 133 117]
  [134 135 119]
  ...
  [ 46  55  68]
  [ 50  58  71]
  [ 52  61  74]]

 [[124 122 122]
  [129 125 126]
  [132 128 128]
  ...
  [ 54  57  64]
  [ 56  59  66]
  [ 58  61  67]]]
[[[180 193 176]
  [183 194 177]
  [186 194 177]
  ...
  [202 192 166]
  [202 192 166]
  [202 192 166]]

 [[179 192 175]
  [180 193 176]
  [181 194 177]
  ...
  [204 193 164]
  [203 192 163]
  [203 192 163]]

 [[186 189 176]
  [187 191 177]
  [192 195 181]
  ...
  [205 194 170]
  [203 192 171]
  [202 191 170]]

 ...

 [[135 134 118]
  [137 138 123]
  [139 142 128]
  ...
  [ 56  56  56]
  [ 57  57  57]
  [ 59  59  59]]

 [[142 136 114]
  [144 138 116]
  [145 141 118]
  ...
  [ 53  58  61]
  [ 53  60  61]
  [ 54  61  62]]

 [[144 134 119]
  [144 134 119]
  [148 138 123]
  ...
  [ 60  59  60]
  [ 63  60  61]
  [ 64  62  62]]]
[[[189 190 183]
  [191 193 186]
  [192 194 187]
  ...
  [201 194 162]
  [200 194 162]
  [200 194 162]]

 [[197 197 181]
  [196 195 180]
  [196 195 180]
  ...
  [196 193 161]
  [192 191 159]
  [193 192 160]]

 [[192 194 185]
  [187 190 179]
  [184 187 175]
  ...
  [189 192 159]
  [187 190 156]
  [188 192 157]]

 ...

 [[140 134 121]
  [139 133 120]
  [139 133 120]
  ...
  [ 48  55  55]
  [ 51  58  57]
  [ 54  61  61]]

 [[144 132 124]
  [146 136 129]
  [145 138 129]
  ...
  [ 52  55  62]
  [ 54  57  64]
  [ 58  61  67]]

 [[129 131 122]
  [131 132 123]
  [133 132 123]
  ...
  [ 58  58  60]
  [ 61  61  61]
  [ 62  62  62]]]
17

Motion Detector:
Our task is to give them a webcam, that can detect the motion or any movement in front of it. This should return a graph, this graph should contain for how long the human/object was in front of the camera.


