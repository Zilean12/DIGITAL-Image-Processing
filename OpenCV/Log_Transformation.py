import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 
#this type of processing is suited for expanding dark pixels while compressing higher pixels

# Read an image 
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\fourierspectrum.jpg') 
plt.imshow(image) 
plt.show()

# Apply log transformation method 
c = 255 / np.log(1 + np.max(image)) 
log_image = c * (np.log(image + 1)) 
   
# Specify the data type so that 
# float value will be converted to int 
log_image = np.array(log_image, dtype = np.uint8) 
   
# Display both images 
plt.imshow(image) 
plt.show() 
plt.imshow(log_image) 
plt.show() 
