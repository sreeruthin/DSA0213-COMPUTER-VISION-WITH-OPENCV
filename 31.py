import cv2
import numpy as np

img = cv2.imread(r"C:\Users\sriru\OneDrive\Desktop\CSA0213 OPENCV\1b.png")
template = cv2.imread(r"C:\Users\sriru\OneDrive\Desktop\CSA0213 OPENCV\watch_template.png")

if img is None:
    print("Main image not loaded")
    exit()

if template is None:
    print("Template image not loaded")
    exit()

h, w = template.shape[:2]

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
cv2.imshow("Watch Detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
