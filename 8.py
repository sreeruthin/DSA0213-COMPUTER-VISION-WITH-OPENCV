import cv2
import numpy as np

img=cv2.imread("1a.png")
h,w=img.shape[:2]

pts1=np.float32([[50,50],[300,50],[50,300],[300,300]])
pts2=np.float32([[10,100],[320,40],[80,350],[300,300]])

M=cv2.getPerspectiveTransform(pts1,pts2)
perspective=cv2.warpPerspective(img,M,(w,h))

cv2.imshow("Original Image",img)
cv2.imshow("Perspective Transformed Image",perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()
