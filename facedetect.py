import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\sarka\\Desktop\\Open CV\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\\Users\\sarka\\Pictures\\test.jpg",0)
faces = face_cascade.detectMultiScale(img, scaleFactor = 1.05, minNeighbors=5)
for x,y,w,h in faces:
	img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)
cv2.imshow("FacR",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
