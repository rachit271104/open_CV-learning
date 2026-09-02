#
import cv2

# gaussinan filter 
image=cv2.imread("photo.png",)

blurred=cv2.GaussianBlur(image,(7,7),0)

cv2.imshow("1",image)
cv2.imshow("2",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -------------------------------------

# median blur 
