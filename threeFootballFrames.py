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

    #cv2.imshow('Original', image)  # Display original image
    #cv2.waitKey(0)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0,256])
        print(color+': '+str(np.linalg.norm(hist)))
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()
    
    # Now for the smaller image
    height, width = image.shape[:2]
    image = cv2.resize(image, (width // 60, height // 60))
    #cv2.imshow('Cut', image)  # Display cut image
    #cv2.waitKey(0)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0,256])
        print(color+': '+str(np.linalg.norm(hist)))
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()
    

if __name__ == '__main__':
    main(get_args())