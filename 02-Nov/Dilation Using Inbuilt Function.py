# dilation of images. 
import cv2 
import numpy as np 

# Reading the input image 
img = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example1.jpeg", 0)

kernel = np.ones((3, 3), np.uint8) 

# The first parameter is the original image, 
# kernel is the matrix with which image is 
# convolved and third parameter is the number 
# of iterations, which will determine how much 
# you want to erode a given image. 
img_dilation = cv2.dilate(img, kernel, iterations=1) 

cv2.imshow('Input', img) 
cv2.imshow('Dilation', img_dilation) 

cv2.waitKey(0) 
