import argparse
import cv2      # OpenCV library
import os
from matplotlib import pyplot as plt
import imutils

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--photo', required=True)
    return parser.parse_args()

def main(args):
    image = cv2.imread(args.photo)  # Get image from command line

    cv2.imshow('Original', image)  # Display original image
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert image to gray
    cv2.imshow('Gray Picture', gray_image)  # Display gray image
    cv2.waitKey(0)

    hist = cv2.calcHist([gray_image], [0], None, [256], [0,256])  #Grayscale histogram
    plt.figure()
    plt.title('Gray Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()
    cv2.waitKey(0)

    cv2.destroyAllWindows()


    #photo = args.photo
    #image = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)

    #plt.axis("off")
    #plt.imshow(image, cmap = 'gray')
    #plt.show()

    #cv2.imshow("", image)

if __name__ == '__main__':
    main(get_args())


