import cv2 
import matplotlib.pyplot as plt 

# Read an image 
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\forest.jpg') 
plt.show()

# Apply contrast stretching method 
maxiI = 250
miniI = 3

maxoI = 155 
minoI = 0

stretched_image = image.copy()
# get height and width of the image 
height, width, _ = image.shape 
  
for i in range(0, height - 1): 
    for j in range(0, width - 1): 
          
        # Get the pixel value 
        pixel = stretched_image[i, j] 
          
        # 1st index contains red pixel 
        pixel[0] = (pixel[0] - miniI) * ((maxoI-minoI) / (maxiI-miniI)) + minoI  
          
        # 2nd index contains green pixel 
        pixel[1] = (pixel[1] - miniI) * ((maxoI-minoI) / (maxiI-miniI)) + minoI 
          
        # 3rd index contains blue pixel 
        pixel[2] = (pixel[2] - miniI) * ((maxoI-minoI) / (maxiI-miniI)) + minoI 
          
        # Store new values in the pixel 
        stretched_image[i, j] = pixel 
  

#original image
plt.imshow(image) 
plt.show()

#stretched image
plt.imshow(stretched_image) 
plt.show() 