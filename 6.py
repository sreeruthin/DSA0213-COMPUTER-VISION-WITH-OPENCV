import cv2
import numpy as np

img=cv2.imread("input.png")
h,w=img.shape[:2]

tx,ty=100,50
M=np.float32([[1,0,tx],[0,1,ty]])

moved=cv2.warpAffine(img,M,(w,h))

cv2.imshow("Original Image",img)
cv2.imshow("Moved Image",moved)

cv2.waitKey(0)
cv2.destroyAllWindows()
