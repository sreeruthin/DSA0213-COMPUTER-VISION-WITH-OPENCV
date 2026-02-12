import cv2

img1 = cv2.imread("1a.png")
img2 = cv2.imread("1b.png")

crop = img1[50:200, 50:200]

img2[50:200, 50:200] = crop

cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
