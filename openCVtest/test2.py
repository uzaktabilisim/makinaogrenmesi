import cv2 

img = cv2.imread("mask2.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

mask = cv2.inRange(hsv, (0,0,0), (180, 50, 130))
dst1 = cv2.bitwise_and(img, img, mask=mask)

th, threshed = cv2.threshold(v, 150, 255, cv2.THRESH_BINARY_INV)
dst2 = cv2.bitwise_and(img, img, mask=threshed)

th, threshed2 = cv2.threshold(s, 30, 255, cv2.THRESH_BINARY_INV)
dst3 = cv2.bitwise_and(img, img, mask=threshed2)

cv2.imwrite("dst1.png", dst1)
cv2.imwrite("dst2.png", dst2)
cv2.imwrite("dst3.png", dst3)

cv2.imshow("dst1.png", dst1)
cv2.imshow("dst2.png", dst2)
cv2.imshow("dst3.png", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()