import numpy as np
import cv2


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def saveImage(image, name_of_image):
    cv2.imwrite(name_of_image, image)


def cropImage(image, x, y, height, weight):
    cropped = image[y:y+height, x:x+weight]
    print(cropped.shape)
    viewImage(cropped, 'Image after Crop')

    return cropped


img = cv2.imread('mask.jpg')
print(img.shape)

viewImage(img, "Demo")
cropppedImg = cropImage(img, 79, 26, 500, 500)
saveImage(cropppedImg, 'croppedMask.jpg')

cv2.waitKey(0)
