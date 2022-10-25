import cv2

cap = cv2.VideoCapture("video/sample.mp4")
i = 0
Frame_Path = 'Frames'
ctr = 0


# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        ctr+=1
    if cv2.waitKey(0)  == ord('q'):
        break
print(ctr)
    # if ret == False:
    #     break
    # cv2.imwrite(Frame_Path+"/frame"+str(i)+'.jpg', frame)
    # i+=1
cap.release()
cv2.destroyAllWindows()
