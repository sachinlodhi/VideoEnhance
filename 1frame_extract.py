# First file -> Extract Frames from the video
import cv2

cap = cv2.VideoCapture("video/ball.webm")
i = 0
Frame_Path = 'Frames'
ctr = 0

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(Frame_Path+"/frame"+str(i)+'.jpg', frame)
    i+=1
cap.release()
cv2.destroyAllWindows()
print(i)