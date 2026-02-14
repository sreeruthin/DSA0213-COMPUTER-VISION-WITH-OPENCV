import cv2
import numpy as np

img = cv2.imread("image.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area > 500:
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        extracted_object = img[y:y+h, x:x+w]

        cv2.imshow("Extracted Object", extracted_object)

cv2.imshow("Rectangular Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
