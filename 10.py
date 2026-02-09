import cv2
import numpy as np

img=cv2.imread("image.png")
h,w=img.shape[:2]

pts1=np.float32([[50,50],[300,50],[50,300],[300,300]])
pts2=np.float32([[10,100],[320,40],[80,350],[300,300]])

H,_=cv2.findHomography(pts1,pts2)
homography=cv2.warpPerspective(img,H,(w,h))

cv2.imshow("Original Image",img)
cv2.imshow("Homography Transformed Image",homography)

cv2.waitKey(0)
cv2.destroyAllWindows()
