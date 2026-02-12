import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
boundary = cv2.filter2D(img, -1, kernel)
cv2.imshow("Boundary Image", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
