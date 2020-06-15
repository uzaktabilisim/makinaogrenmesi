import cv2
import numpy as np
import os

path = './256_GRAY_shift/A/test/'
savePath = './128_GRAY_shift/A/test/'

# viewImage(Image, name_of_window)


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()

# saveImage(Image, name_of_window)


def saveImage(image, name_of_image):
    cv2.imwrite(name_of_image, image)

# cropImage(Image, x_starting_cord, y_starting_cord, height, weight)


def cropImage(image, x, y, height, weight):
    cropped = image[y:y+height, x:x+weight]
    print(cropped.shape)
    viewImage(cropped, 'Image after Crop')

# scaleImage(Image, scale_percent)


def scaleImage(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    viewImage(resized, "After scaling to {0}%".format(scale_percent))

    return resized

# rotateImage(Image, rotate_degree)


def rotateImage(image, degree):
    (h, w, d) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, degree, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    viewImage(rotated, "After turning {0} degrees".format(degree))

# grayImage(Image, black_white_border)


def grayImage(image, border):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, threshold_image = cv2.threshold(gray_image, border, 255, 0)
    print(ret)
    viewImage(gray_image, "Grayscale Image")
    viewImage(threshold_image, "Black-White Image")

# blurredImage(Image, blur_lvl) ==> blur_lvl : need to get odd number


def blurredImage(image, ksize):
    blurred = cv2.GaussianBlur(image, (ksize, ksize), 0)
    viewImage(blurred, "Blurred Image")


def createSenteticMask(height, weight):
    array = np.zeros([height, weight, 4], dtype=np.uint8)

    for x in range(weight):
        for y in range(height):
            if (
                (x % 30 < 10) and (y % 30 < 10)
            ):
                array[y, x] = 255
                array[y, x, 3] = 0
            else:
                array[y, x] = 0

    return array


def addSenteticMask(image):
    height, width, channels = image.shape

    for x in range(width):
        for y in range(height):
            if (
                (x % 30 < 10) and (y % 30 < 10)
            ):
                pass
            else:
                image[y, x] = 0

    return image


def addMask(image, mask):
    ih, iw, ic = image.shape
    mh, mw, mc = mask.shape
    if ih < iw:
        scale_percent = (mw*100) // iw
    else:
        scale_percent = (mw*100) // ih

    resized = scaleImage(image, scale_percent)
    print(resized.shape)
    height, width, channels = resized.shape

    for x in range(width):
        for y in range(height):
            Blue, Green, Red = mask[y, x]
            if (
               Blue > 70 and Green > 70 and Red > 70
               ):
                pass
            else:
                #resized[y, x] = [Blue, Green, Red]
                resized[y, x] = 0

    return resized


def resizeImage(image, height, width):
    ih, iw, ic = image.shape
    if ih < iw:
        scale_percent = (height*100) // iw
    else:
        scale_percent = (height*100) // ih

    resized = scaleImage(image, scale_percent)

    return resized


def main():
    # img = cv2.imread('tiger.jpg')
    # mask = cv2.imread('mask3.jpg')
    # # senteticImg = createSenteticMask(480, 640)
    # print(img.shape)
    # print(mask.shape)
    # maskedImg = addMask(img, mask)
    # viewImage(maskedImg, 'Masked Image')
    # saveImage(maskedImg, 'MaskedImage1.jpg')

    # # r=root, d=directories, f = files
    # for r, d, f in os.walk(path):
    #     for file in f:
    #         img = cv2.imread(path + file)
    #         print(img.shape)
    #         print(mask.shape)
    #         maskedImg = addMask(img, mask)
    #         viewImage(maskedImg, path + file)
    #         saveImage(maskedImg, savePath + file)

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            print(file)
            img = cv2.imread(path + file)
            print(img.shape)
            scaledImage = scaleImage(img, 50)
            viewImage(scaledImage, path + file)
            saveImage(scaledImage, savePath + file)

    # viewImage(img, 'Original')

    # cropImage(img, 500, 500, 500, 1000)

    # scaleImage(img, 60)

    # rotateImage(img, 120)

    # grayImage(img, 127)

    # blurredImage(img, 51)


if __name__ == "__main__":
    main()
