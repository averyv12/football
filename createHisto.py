import argparse
import cv2      # OpenCV library
import os
from matplotlib import pyplot as plt
import imutils
import numpy as np

#def get_args():
#    parser = argparse.ArgumentParser()
#    parser.add_argument('video_file')
#    return parser.parse_args()


def main():
    previous_cut = 0
    current_cut = 0
    sideline = []
    scoreboard = []
    endzone = []
    play_diff = []
    save_sideline = 0
    i = 0
    scoreboard_bins = [0,50,100,150,200,250,300]
    sideline_bins = [0,200,400,600,800,1000,1200,1400,1600,1800,2000,2500,3000]
    endzone_bins = [0,200,400,600,800,1000,1200,1400,1600,1800,2000,2500,3000]
    play_diff_bins = [0,100,200,300,400,500,600,700,800]

    with open('/Users/averyvoss/Desktop/SummerJob/Football/uscGame/uscPlays.txt', 'r') as f:
        for line in f:
            play_details = line.split()
            current_cut = int(play_details[0])
            if (current_cut != 0):
                difference = current_cut - previous_cut

                if (i % 3 == 0): # scoreboard
                    scoreboard.append(difference)

                if (i % 3 == 1): # sideline
                    sideline.append(difference)
                    save_sideline = difference

                if (i % 3 == 2): # endzone
                    endzone.append(difference)
                    play_diff.append(abs(difference - save_sideline))

                    #if (abs(difference - save_sideline) > 500):
                    #    print(line)

                i += 1
            previous_cut = current_cut


    plt.hist(scoreboard, scoreboard_bins)
    plt.title("Scoreboard Histogram")
    plt.show()

    plt.hist(sideline, sideline_bins)
    plt.title("Sideline Histogram")
    plt.show()

    plt.hist(endzone, endzone_bins)
    plt.title("Endzone Histogram")
    plt.show()

    plt.hist(play_diff, play_diff_bins)
    plt.title("Play Difference Histogram")
    plt.show()

    f.close()


if __name__ == '__main__':
    main()