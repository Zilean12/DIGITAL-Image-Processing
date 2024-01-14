import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 
#this type of processing is suited for displaying image correctly for human eye based on monitor's display settings

# Read an image 
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\sydney.jpeg') 
plt.imshow(image) 

# Trying 4 gamma values. 
for gamma in [0.1, 1.2, 2.2, 3.2, 4.2]:

    # Apply gamma correction. 
    gamma_corrected = np.array(255*(image / 255) ** gamma, dtype = 'uint8') 
    plt.imshow(gamma_corrected) 
    plt.show() 
