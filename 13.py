import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
cv2.imshow("Sobel X", sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
