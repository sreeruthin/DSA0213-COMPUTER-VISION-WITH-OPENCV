import cv2
import numpy as np

img = cv2.imread("1a.png")
overlay = img.copy()
cv2.putText(overlay, "WATERMARK", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
alpha = 0.4
watermarked = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
cv2.imshow("Watermarked Image", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()
