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
    cuts = 0
    frames = []
    local = []
    current_frame = 0
    plays = 0

    with open('/Users/averyvoss/Desktop/SummerJob/Football/uscPlays.txt', 'r') as f:
        for line in f:
            play_details = line.split()
            current_cut = int(play_details[0])
            frames.append(current_cut)

    path = '/Users/averyvoss/Desktop/SummerJob/Football/uscGame'  # Locate the folder

    while True:  
        
        if (i == 0): # get 5 frames concatenated for the first cut
            blank_image = np.ones((72,644,3), dtype = np.uint8)
            blank_image = 255*blank_image
            for j in range(5):
                is_ok, frame = vc.read()
                frame = cv2.resize(frame, (width // 10, height // 10))
                blank_image[0:72,j*129:j*129+128]=frame
                if (i == 0):
                    blank_image = cv2.rectangle(blank_image,(0,0),(128,71),(0,0,255),2)
                #local.append(frame)
            i += 4
            cuts += 1
            #create_image(current_frame, cuts, local)
            #local = []
            cv2.imwrite(os.path.join(path, str(0)+'|'+str(0)+'|board.jpg'), blank_image)
            current_frame = int(frames[1])
           


        elif (i == current_frame - 4): # get 5 previous and 5 next frames concatenated for the other cuts
            blank_image = np.ones((72,1289,3), dtype = np.uint8)
            blank_image = 255*blank_image
            for j in range(10):
                is_ok, frame = vc.read()
                frame = cv2.resize(frame, (width // 10, height // 10))
                blank_image[0:72,j*129:j*129+128]=frame
                if (j == 4):
                    blank_image = cv2.rectangle(blank_image,(129*j,0),(129*j+128,71),(0,0,255),2)
                #local.append(frame)
            i += 9
            cuts += 1
            #create_image(current_frame, cuts, local)
            #local = []

            plays = (cuts - 1) // 3

            if ((cuts - 1) % 3 == 0): # scoreboard
                cv2.imwrite(os.path.join(path, str(current_frame)+'|'+str(plays)+'|board.jpg'), blank_image)

            if ((cuts - 1) % 3 == 1): # sideline
                cv2.imwrite(os.path.join(path, str(current_frame)+'|'+str(plays)+'|side.jpg'), blank_image)

            if ((cuts - 1) % 3 == 2): # endzone
                cv2.imwrite(os.path.join(path, str(current_frame)+'|'+str(plays)+'|end.jpg'), blank_image)
            
            #overall = []

            if (cuts != len(frames)):
                current_frame = int(frames[cuts])

        
        else:
            is_ok, frame = vc.read()
            if not is_ok:   
                break
        
        i += 1
        

    f.close()
    vc.release()

#def create_image(current_cut, cuts, local):
#    blank_image = np.ones((180,3209,3), dtype = np.uint8)
##    blank_image = 255*blank_image
#    path = '/Users/averyvoss/Desktop/SummerJob/Football/cgGame'  # Locate the folder
#    overall = cv2.hconcat(local)
#    plays = (cuts - 1) // 3

#    if ((cuts - 1) % 3 == 0): # scoreboard
#        cv2.imwrite(os.path.join(path, 'blank.jpg'), blank_image)
#        cv2.imwrite(os.path.join(path, str(current_cut)+'|'+str(plays)+'|board.jpg'), overall)

#    if ((cuts - 1) % 3 == 1): # sideline
#        cv2.imwrite(os.path.join(path, str(current_cut)+'|'+str(plays)+'|side.jpg'), overall)

#    if ((cuts - 1) % 3 == 2): # endzone
#        cv2.imwrite(os.path.join(path, str(current_cut)+'|'+str(plays)+'|end.jpg'), overall)
    
#    overall = []


if __name__ == '__main__':
    main(get_args())