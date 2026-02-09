import cv2
import numpy as np

img=cv2.imread("image.png")
h,w=img.shape[:2]
center=(w//2,h//2)

rot_cw=cv2.getRotationMatrix2D(center,-45,1)
rot_ccw=cv2.getRotationMatrix2D(center,45,1)

cw=cv2.warpAffine(img,rot_cw,(w,h))
ccw=cv2.warpAffine(img,rot_ccw,(w,h))

cv2.imshow("Original",img)
cv2.imshow("Clockwise Rotation",cw)
cv2.imshow("Counter Clockwise Rotation",ccw)

cv2.waitKey(0)
cv2.destroyAllWindows()
