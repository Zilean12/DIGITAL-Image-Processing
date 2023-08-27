import cv2
img = cv2.imread(filename="03.jpg", flags=0)
print(img)
cv2.imshow('03', img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite(filename='output.png', img=img)
    cv2.destroyAllWindows()
