import argparse
import cv2      # OpenCV library
import os
from matplotlib import pyplot as plt
import imutils
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--photo', required=True)
    return parser.parse_args()

def main(args):
    image = cv2.imread(args.photo)  # Get image from command line

    cv2.imshow('Original', image)  # Display original image
    cv2.waitKey(0)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')

    print('Test Frame Color: ')

    for (chan, color) in zip(chans, colors):
        hist2 = cv2.calcHist([chan], [0], None, [256], [80,150])
        hist3 = cv2.calcHist([chan], [0], None, [256], [151,256])
        hist = cv2.calcHist([chan], [0], None, [256], [0,79])
        if (color == 'g'):
            #print(color+ '  ')
            green1 = np.linalg.norm(hist)
            green2 = np.linalg.norm(hist2)
            green3 = np.linalg.norm(hist3)
            print(color + '   ' + str(green1)+ ' '+str(green2)+ ' '+str(green3))
        if (color == 'b'):
            #print(color+ '  ')
            blue1 = np.linalg.norm(hist)
            blue2 = np.linalg.norm(hist2)
            blue3 = np.linalg.norm(hist3)
            print(color + '   ' + str(blue1)+ ' '+str(blue2)+ ' '+str(blue3))
        if (color == 'r'):
            #print(color + '  ')
            red1 = np.linalg.norm(hist)
            red2 = np.linalg.norm(hist2)
            red3 = np.linalg.norm(hist3)
            print(color + '   ' + str(red1)+ ' '+str(red2)+ ' '+str(red3))
        
    

if __name__ == '__main__':
    main(get_args())