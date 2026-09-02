# in this file we learn edge detection and thresholding
import cv2

#canny edge detection
img=cv2.imread("photo.png",cv2.IMREAD_GRAYSCALE)

# edges=cv2.Canny(img,50,150)
# cv2.imshow("original",img)
# cv2.imshow("cannyed photo",edges)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# -------------------------------------

# thresholding
ret,thresh_img=cv2.threshold(img,150,255,cv2.THRESH_BINARY)

cv2.imshow("original",img)
cv2.imshow("thresholded photo",thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()