import cv2

tiger = cv2.imread('tiger.jpg')

mask = cv2.imread('SenteticMask.jpg')

img = cv2.add(tiger, mask)

cv2.imshow('image', img)

cv2.waitkey(0)

cv2.distroyAllWindows()
