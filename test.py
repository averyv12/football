import argparse
import cv2      # OpenCV library
import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('video_file')
    return parser.parse_args()


def main(args):
    video_file = args.video_file

    vc = cv2.VideoCapture(video_file)   # Open the video file
    height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Get height of video
    width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get width of video
    fps = vc.get(cv2.CAP_PROP_FPS)  # Get fps of video
    num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT)) # Get number of frames of video
    i = 0
    arr = []
    while i < 222:
        is_ok, frame = vc.read()
        
        if not is_ok:   
            # Probably done reading the video
            break

        arr.append(i)
        i += 1


    with open('/Users/averyvoss/Desktop/SummerJob/Football/cgGame/cgPlays.txt', 'w') as f:
        for element in arr:
            f.write(str(element))
            f.write('   Time of Cut: ')
            seconds = element//fps
            minutes = 0
            hours = 0
            if seconds >= 60:
                minutes = seconds//60
                seconds = seconds - (minutes * 60)
            if minutes >= 60:
                hours = minutes//60
                minutes = minutes - (hours * 60)
            f.write(str(int(hours))+':'+str(int(minutes))+':'+str(int(seconds)))
            f.write('\n')
    f.close()


    vc.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(get_args())