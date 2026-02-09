import cv2

img=cv2.imread("dd.jpg")

bigger=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
smaller=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

cv2.imshow("Original Image",img)
cv2.imshow("Bigger Image",bigger)
cv2.imshow("Smaller Image",smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
