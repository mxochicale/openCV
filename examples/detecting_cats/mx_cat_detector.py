# import the necessary packages
#import argparse
import cv2
 
## construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to the input image")
#ap.add_argument("-c", "--cascade",
#	default="haarcascade_frontalcatface.xml",
#	help="path to cat detector haar cascade")
#args = vars(ap.parse_args())

# load the input image and convert it to grayscale

i = '/home/map479-admin/mxochicale/github/openCV/examples/detecting_cats/images/cat-03.jpg'
c = '/home/map479-admin/mxochicale/github/openCV/examples/detecting_cats/haarcascade_frontalcatface.xml'


image = cv2.imread(i)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray', gray) 

# in the input image
detector = cv2.CascadeClassifier(c)
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=10, minSize=(75, 75))


print(rects)

# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
	cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

 
## show the detected cat faces
cv2.imshow("Cat Faces", image)
cv2.waitKey(0)




