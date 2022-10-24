import cv2
import numpy as np
import glob

frameSize = (1280, 720)
frames = 'final_frames/'
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

for filename in glob.glob(frames+'*jpg'):
    img = cv2.imread(filename)
    out.write(img)

out.release()