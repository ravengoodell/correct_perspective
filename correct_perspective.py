# Author: Raven Goodell
# Some of the code in this project is based on the following tutorial: 
# https://github.com/spmallick/learnopencv/blob/master/Homography/perspective-correction.py
# I made the following modifications and improvements to the tutorial code: 1) Allow user to select image input from their system's file explorer
# using the filedialog module in the tkinter library, 2) Automatically fit the source image to the user's screen using OpenCV's namedWindow function, 
# 3) Initialize the variable "size" to match the dimensions of the source image, 4) Write my own get_four_points function instead of importing the 
# get_four_points function from the tutorial code 

import cv2
import numpy as np
from tkinter import filedialog

# Function that allows user to select the four points from the source image
# Returns a numpy array of the four points
def get_four_points():
    points = []
    def mouse_handler(event, x, y, flags, data):
        # Mouse callback that gets four points
        if event == cv2.EVENT_LBUTTONDOWN:
            # Left click means storing a point
            points.append((x, y))
            cv2.circle(im_src, (x, y), 3, (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow("output", im_src)

    # Set up handler for mouse
    cv2.imshow("output", im_src)
    cv2.setMouseCallback("output", mouse_handler, points)

    # Wait until 4 points have been selected
    while len(points) < 4:
        cv2.waitKey(100)

    # Convert to numpy array
    points = np.vstack(points).astype(float)

    return points

if __name__ == '__main__' :

    # Read in the image.
    im_src = cv2.imread(filedialog.askopenfilename())
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)

    # Destination image
    size = im_src.shape

    im_dst = np.zeros(size, np.uint8)

    
    pts_dst = np.array(
                       [
                        [0,0],
                        [size[0] - 1, 0],
                        [size[0] - 1, size[1] -1],
                        [0, size[1] - 1 ]
                        ], dtype=float
                       )
    
    
    print("Click on the four corners of the book -- top left first and bottom left last")

    # Show image and wait for 4 clicks.
    cv2.imshow("output", im_src)
    pts_src = get_four_points() 
    
    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show output
    cv2.imshow("output", im_dst)
    cv2.waitKey(0)
