import cv2
img = cv2.imread(filename=r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png", flags=0)
print(img)
cv2.imshow('03', img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite(filename='output.png', img=img)
    cv2.destroyAllWindows()
