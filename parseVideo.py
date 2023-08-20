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
    scoreboard = False
    plays = 0
    previous_hist = 0
    previous_blue = 0
    previous_red = 0
    previous_play = 0
    previous_cut = 0
    while True:
        is_ok, frame = vc.read()
        
        if not is_ok:   
            # Probably done reading the video
            break

        chans = cv2.split(frame)
        colors = ('b', 'g', 'r')
        green = 0
        

        for (chan, color) in zip(chans, colors):
            hist = cv2.calcHist([chan], [0], None, [256], [80,150])
            hist2 = cv2.calcHist([chan], [0], None, [256], [0,79])
            hist3 = cv2.calcHist([chan], [0], None, [256], [151,256])
            if (color == 'g'):
                green = np.linalg.norm(hist)
            if (color == 'b'):
                blue = np.linalg.norm(hist2)
            if (color == 'r'):
                red = np.linalg.norm(hist3)



        if (scoreboard == False and (i == 0 or # First frame will be scoreboard
        ((previous_hist - green > 6000) and 
        (green < 60000) and # previously less green < 60000
        (green > 10000) and 
        #(previous_hist - green < 30000) and
        (i - previous_play > 1300) #and # Error to deal with spontaneous random frames, if i < 1500, CG game works 99%
        #(red - previous_red > 4000) #and #previously 4000
        #(previous_blue - blue > 5000)
        ))): # First frame of scoreboard
            plays += 1
            scoreboard = True
            previous_play = i
            path = '/Users/averyvoss/Desktop/SummerJob/Football/game2'  # Locate the folder
            cv2.imwrite(os.path.join(path, 'frame'+str(i)+'.jpg'), frame)  # Assign individual frames to that folder



        if (scoreboard == True and (green - previous_hist > 10000)): # Change to field
            scoreboard = False



        previous_hist = green
        previous_red = red
        #previous_blue = blue


        i += 1

    print(plays)
    vc.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(get_args())