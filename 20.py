import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
A = 1.5
blur = cv2.GaussianBlur(img, (5, 5), 0)
mask = cv2.subtract(img, blur)
highboost = cv2.addWeighted(img, A, mask, 1, 0)
cv2.imshow("High-Boost Sharpening", highboost)
cv2.waitKey(0)
cv2.destroyAllWindows()
