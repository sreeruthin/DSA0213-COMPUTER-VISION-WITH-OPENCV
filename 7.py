import cv2
import numpy as np

img=cv2.imread("input.png")
h,w=img.shape[:2]

pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])

M=cv2.getAffineTransform(pts1,pts2)
affine=cv2.warpAffine(img,M,(w,h))

cv2.imshow("Original Image",img)
cv2.imshow("Affine Transformed Image",affine)

cv2.waitKey(0)
cv2.destroyAllWindows()
