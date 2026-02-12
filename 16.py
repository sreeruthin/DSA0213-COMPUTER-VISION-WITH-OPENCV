import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
kernel1 = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])
lap1 = cv2.filter2D(img, cv2.CV_64F, kernel1)
sharp1 = img.astype(np.float64) - lap1
sharp1 = np.clip(sharp1, 0, 255).astype(np.uint8)
cv2.imshow("Sharpened 4-Neighbour", sharp1)
cv2.waitKey(0)
cv2.destroyAllWindows()
