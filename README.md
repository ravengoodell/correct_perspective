# correct_perspective
A program to correct the perspective of an image using homography

Some of the code in this project is based on the following tutorial: https://github.com/spmallick/learnopencv/blob/master/Homography/perspective-correction.py

I made the following modifications and improvements to the tutorial code: 1) Alow user to select image input from their system's file explorer using the filedialog module in the tkinter library, 2) Automatically fit the source image to the user's screen using OpenCV's namedWindow function, 3) Initialize the variable "size" to match the dimensions of the source image, 4) Write my own get_four_points function instead of importing the get_four_points function used in the tutorial code
