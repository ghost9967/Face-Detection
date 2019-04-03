import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\sarka\\Desktop\\Open CV\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
cv2.waitKey(10000)
if (cam.isOpened()== False): 
  print("Error opening video stream or file")
 
while(cam.isOpened()):
  
  ret, frame = cam.read()
  if ret == True:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=5)

    for x,y,w,h in faces:
          img = cv2.rectangle(gray, (x,y), (x+w,y+h), (0,255,0),3)

    cv2.imshow('Frame',gray)
 
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
    
cam.release()
cv2.destroyAllWindows()
