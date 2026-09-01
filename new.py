import cv2

img = cv2.imread("photo.png")
# cv2.imshow("image",img)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

#convert to black and white (gray scale)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray_photo",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# save 
# name=input("enter the name of the file with type: ")
# cv2.imwrite(name,gray)

#IMAGE RESIZING    width,height

# resized = cv2.resize(img,(300,300))   
# cv2.imshow("originam image",img)
# cv2.imshow("resized ", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -------------------------------------
# crop image

# cropped = img[100:500 , 100:500]


# cv2.imshow("original", img)
# cv2.imshow("cropped", cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# --------------------------------------------
# image rotating and flipping

"""

(h,w)=img.shape[:2]
center =  (w//2,h//2)
m=cv2.getRotationMatrix2D(center,90, 1.0)
rotated= cv2.warpAffine(img,m,(w,h))

cv2.imshow("rotated",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

# now to flip

# flipped_h= cv2.flip(img,0)
# flipped_v=cv2.flip(img,1)
# flipped_both=cv2.flip(img,-1)

# cv2.imshow("original",img)
# cv2.imshow("h",flipped_h)
# cv2.imshow("v",flipped_v)
# cv2.imshow("both",flipped_both)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ------------------------------------------

# text in image
cv2.putText(img,"added text to image",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.9,(0,0,255),4)


cv2.imshow("added text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
