import cv2
import natsort
import glob

frameSize = (1280, 720)
frames = 'final_frames/'
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)
frame_list = glob.glob(frames+'*jpg')
frame_list = natsort.natsorted(frame_list)
# for i in frame_list:
#     print(i)

for filename in frame_list:
    img = cv2.imread(filename)
    out.write(img)

out.release()