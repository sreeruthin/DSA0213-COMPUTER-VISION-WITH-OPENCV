import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
gradient = cv2.magnitude(sobelx, sobely)
gradient = cv2.convertScaleAbs(gradient)
sharp = cv2.add(img, gradient)
cv2.imshow("Gradient Sharpening", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
