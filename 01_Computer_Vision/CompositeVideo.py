# importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
import os
from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import VideoClip, ColorClip
from moviepy.audio.AudioClip import CompositeAudioClip

white_output = 'test_videos_output/solidWhiteRight_output.mp4'
#clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4")
imageInputFolder = "D:\\"
imageOutputFolder = "D:\\\"

fileLists = os.listdir(imageInputFolder)

for n in fileLists:
    #image_ori = mpimg.imread(imageInputFolder + n)
    # printing out some stats and plotting
    print('This image is:',imageInputFolder + n)
    clips = VideoFileClip(imageInputFolder + n)
    #image_ori = process_image(image_ori)
    #plt.imsave(imageOutputFolder + n + '-final.jpg', image_ori)

white_clip.write_videofile(whiteclips_output, audio=False)
#

# white_clip = clip1.fl_image(process_image)  # NOTE: this function expects color images!!
# white_clip.write_videofile(white_output, audio=False)
