import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("Sobel Y", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
