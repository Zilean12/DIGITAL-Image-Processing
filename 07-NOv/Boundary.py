import cv2
import numpy as np

def boundary_extraction(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)  # You can adjust the thresholds

    return edges

image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example3.png")
boundary = boundary_extraction(image)

cv2.imshow("Boundary", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
