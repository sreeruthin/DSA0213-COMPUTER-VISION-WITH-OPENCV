import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
mask = cv2.subtract(img, blur)
sharp = cv2.add(img, mask)
cv2.imshow("Unsharp Masking", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
