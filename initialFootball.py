import argparse
import cv2      # OpenCV library
import os
import numpy as np
import matplotlib.pyplot as plt


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
    while i < 5000:
        is_ok, frame = vc.read()

        if (i == 4647 or i == 4870):
            cv2.imshow(str(i), frame)
            print(vc.get(cv2.CAP_PROP_POS_FRAMES))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        i += 1
    vc.release()
    cv2.destroyAllWindows()
    video_file = args.video_file
    vc = cv2.VideoCapture(video_file)

    vc.set(cv2.CAP_PROP_POS_FRAMES, 4647)
    is_ok, frame = vc.read()
    
    cv2.imshow(str(4647), frame)
    print(vc.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.waitKey(0)

    vc.set(cv2.CAP_PROP_POS_FRAMES, 4870)
    is_ok, frame = vc.read()
    
    cv2.imshow(str(4870), frame)
    print(vc.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.waitKey(0)

    vc.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(get_args())