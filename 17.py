import cv2
import numpy as np

img = cv2.imread("1a.png", 0)
kernel2 = np.array([[1, 1, 1],
                    [1, -8, 1],
                    [1, 1, 1]])
lap2 = cv2.filter2D(img, cv2.CV_64F, kernel2)
sharp2 = img.astype(np.float64) - lap2
sharp2 = np.clip(sharp2, 0, 255).astype(np.uint8)
cv2.imshow("Sharpened 8-Neighbour", sharp2)
cv2.waitKey(0)
cv2.destroyAllWindows()
