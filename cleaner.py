# run this file to clean intermediate files created
import os
import glob
import  shutil
folders = ['final_frames','extracted_frames']
[(shutil.rmtree(i), os.mkdir(i)) for i in folders]

