import cv2

cap = cv2.VideoCapture("video/sample.mp4")
i = 0
Frame_Path = 'Frames'
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(Frame_Path+"/frame"+str(i)+'.jpg', frame)
    i+=1
cap.release()
cv2.destroyAllWindows()
