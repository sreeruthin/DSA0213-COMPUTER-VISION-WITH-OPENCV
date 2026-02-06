import cv2
image = cv2.imread(r"C:\Users\sriru\OneDrive\Desktop\CSA0213 OPENCV\1b.png")  
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
