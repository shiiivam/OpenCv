import cv2
cap = cv2.VideoCapture("Resources/vid.mp4")
while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break