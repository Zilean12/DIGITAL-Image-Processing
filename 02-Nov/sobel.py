import numpy as np
import cv2

input_image = cv2.imread('cards.png', cv2.IMREAD_GRAYSCALE)

sobel_x_filter = [
    [-1, -2, -1], 
    [0, 0, 0], 
    [1, 2, 1]]

sobel_y_filter = [
    [-1, 0, 1], 
    [-2, 0, 2], 
    [-1, 0, 1]]



grad_x = np.zeros_like(input_image)
grad_y = np.zeros_like(input_image)
sobel_result = np.zeros_like(input_image)

height,width = input_image.shape
sobel_result = np.zeros_like(input_image, dtype=np.uint8)

for x in range(1, width-1):
    for y in range(1, height -1):

        
        grad_x[x, y] = np.sum(input_image[x - 1: x + 2, y - 1: y + 2] * sobel_x_filter)
        grad_y[x, y] = np.sum(input_image[x - 1: x + 2, y - 1: y + 2] * sobel_y_filter)
        sobel_result[x,y] =int( np.sqrt(grad_x[x, y] ** 2 + grad_y[x, y] ** 2)) 

grad_x = np.uint8(grad_x)
grad_y = np.uint8(grad_y)
sobel_result = np.uint8(sobel_result)

sobel_res = cv2.Sobel(input_image, cv2.CV_32F, 1, 0, ksize=3)

cv2.imshow('Input', input_image)
cv2.imshow('GRAD_Y', grad_y)

cv2.imshow('Sobel res', sobel_res)
cv2.waitKey(0)
cv2.destroyAllWindows()


