# File 3 -> generate final video
import os
import glob
import cv2
import natsort
import glob
frameSize = (1920, 1080)
frames = 'final_frames/'
out = cv2.VideoWriter('ball_60_FPS_1166.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize) # 120 is FPS value it can be changed to other methods

frame_list = glob.glob(frames+'*jpg')
frame_list = natsort.natsorted(frame_list)
print(len(frame_list))
for filename in frame_list:
    img = cv2.imread(filename)
    out.write(img)
out.release()



