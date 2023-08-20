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
    #curr_frame = 0
    i = 0
    scoreboard = False
    plays = 0
    previous_hist = 0
    previous_blue = 0
    previous_red = 0
    previous_play = 0
    previous_cut = 0
    previous_hist2 = 0
    previous_blue2 = 0
    previous_red2 = 0
    previous_hist3 = 0
    previous_blue3 = 0
    previous_red3 = 0
    cuts = 0
    arr = []
    while True:
        is_ok, frame = vc.read()
        
        if not is_ok:   
            # Probably done reading the video
            break

        #curr_frame = int(vc.get(cv2.CAP_PROP_POS_FRAMES))

        chans = cv2.split(frame)
        colors = ('b', 'g', 'r')
        #green = 0
        total_diff = 0

        for (chan, color) in zip(chans, colors):
            hist2 = cv2.calcHist([chan], [0], None, [256], [80,150])
            hist = cv2.calcHist([chan], [0], None, [256], [0,79])
            hist3 = cv2.calcHist([chan], [0], None, [256], [151,256])
            if (color == 'g'):
                green1 = np.linalg.norm(hist)
                green2 = np.linalg.norm(hist2)
                green3 = np.linalg.norm(hist3)
            if (color == 'b'):
                blue1 = np.linalg.norm(hist)
                blue2 = np.linalg.norm(hist2)
                blue3 = np.linalg.norm(hist3)
            if (color == 'r'):
                red1 = np.linalg.norm(hist)
                red2 = np.linalg.norm(hist2)
                red3 = np.linalg.norm(hist3)


        total_diff1 = abs(red1 - previous_red) + abs(green1 - previous_hist) + abs(blue1 - previous_blue)
        total_diff2 = abs(red2 - previous_red2) + abs(green2 - previous_hist2) + abs(blue2 - previous_blue2)
        total_diff3 = abs(red3 - previous_red3) + abs(green3 - previous_hist3) + abs(blue3 - previous_blue3)


        if (i == 0 or ((total_diff1 > 30000 # Same for both (30000)
        or total_diff2 > 24200 # Same for both (24200)
        or abs(green1 - previous_hist) > 6542 # 6542 for USC game/
        or total_diff3 > 16300) # Use for the USC Game/Not CG
        and i - previous_cut > 110 # Same for both (110)
        and total_diff3 > 4000)): # 4000 for the USC Game/5100 CG
        #or i == 217969 # One of the frame that fails (not in USC)
        #or i == 45792
        #or i == 215763
        #or i == 265788
        #or i == 279212
        #or i == 297112
        #or i == 302871
        #or i == 322009): # One of frame that fails (not in USC)
            previous_cut = i
            arr.append(i)

        previous_hist = green1
        previous_red = red1
        previous_blue = blue1
        previous_hist2 = green2
        previous_red2 = red2
        previous_blue2 = blue2
        previous_hist3 = green3
        previous_red3 = red3
        previous_blue3 = blue3

        i += 1

    with open('/Users/averyvoss/Desktop/SummerJob/Football/uscGame/uscPlays.txt', 'w') as f:
        for element in arr:
            f.write(str(element))
            f.write('   Time of Cut: ')
            f.write(str(element/fps*1000))
            f.write('\n')

    f.close()


if __name__ == '__main__':
    main(get_args())