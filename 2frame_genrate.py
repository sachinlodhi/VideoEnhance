# 2nd File -> Genrate average weighted frome in a video
import cv2
import glob
import natsort
frame_dir = 'Frames'
all_frames = glob.glob(frame_dir+'/*')

i = 0
ctr = 1
final_frames = 'final_frames/'
# sorting the filename
all_frames = natsort.natsorted(all_frames)

for i in range(len(all_frames)):
    frame1 = cv2.imread(all_frames[i])
    frame2 = cv2.imread(all_frames[i+1])
    avg_frame = cv2.addWeighted(frame1, 0.5, frame2, 0.5,0)
    cv2.imwrite(final_frames+'frame_' + str(ctr)+ '.jpg', frame1)
    ctr+=1
    # print(ctr, end=' ')
    cv2.imwrite(final_frames + 'frame_' + str(ctr) + '.jpg', avg_frame)
    ctr+=1
    print(ctr)