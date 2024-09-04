import cv2 as cv
import numpy as np

img = cv.imread("./road34.png")

gray_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

# converting the grayscale value using nested for loop (3 byte into one byte)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        gray_img[i][j] = int(img[i][j][0] * 0.299 + img[i]
                             [j][1] * 0.578 + img[i][j][2] * 0.114)

# getting the maximum and minimum contrast
max_con = 0
min_con = 255

for i in range(img.shape[0]):
    if (max_con < max(gray_img[i])):
        max_con = max(gray_img[i])
    if (min_con > min(gray_img[i])):
        min_con = min(gray_img[i])

en_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
scale = 255 / (max_con - min_con)

# scale up into fit for black and white pixel into 0 and 255
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        en_img[i][j] = int(gray_img[i][j] * scale)

cv.imwrite("original.jpg", en_img)

# function for applying Filters


def applyFilter(filt, image, a, b):
    value = 0
    for i in range(5):
        for j in range(5):
            value += image[a + i][b + j] * filt[i][j]
    return int(value)

# function for normalizing Filter


def normalizeFilter(filt):
    filt_sum = np.sum(np.abs(filt))
    if filt_sum != 0:
        filt = filt / filt_sum
    return filt

# function for calculating RMS value


def rmsDifference(img, filtImg):
    if img.shape != filtImg.shape:
        raise ValueError(
            "Original and filtered images must have the same dimensions.")

    squaredDiff = (img - filtImg) ** 2
    meanSquaredDiff = np.mean(squaredDiff)
    rmsDiff = np.sqrt(meanSquaredDiff)
    return rmsDiff


# create a border with black pixel
border_img = np.zeros((img.shape[0] + 8, img.shape[1] + 8), dtype=np.uint8)
border_img[4:-4, 4:-4] = en_img


# filters
filter_A = [
    [0, -1, -1, -1, 0],
    [-1, 2, 2, 2, -1],
    [-1, 2, 8, 2, -1],
    [-1, 2, 2, 2, -1],
    [0, -1, -1, -1, 0],
]
filter_B = [
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1],
]
filter_C = [
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
]
filter_D = [
    [0, -1, -1, -1, 0],
    [-1, 2, 2, 2, -1],
    [-1, 2, 16, 2, -1],
    [-1, 2, 2, 2, -1],
    [0, -1, -1, -1, 0],
]

# for filter A
fil_A_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        fil_A_img[i][j] = applyFilter(
            normalizeFilter(filter_A), border_img, i, j)

cv.imwrite("Filter_A.jpeg", fil_A_img)
print("RMS value for Filter A : ", rmsDifference(en_img, fil_A_img))

# for filter B
fil_B_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        fil_B_img[i][j] = applyFilter(
            normalizeFilter(filter_B), border_img, i, j)

cv.imwrite("Filter_B.jpeg", fil_B_img)
print("RMS value for Filter B : ", rmsDifference(en_img, fil_B_img))

# for filter C
fil_C_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        fil_C_img[i][j] = applyFilter(
            normalizeFilter(filter_C), border_img, i, j)

cv.imwrite("Filter_C.jpeg", fil_C_img)
print("RMS value for Filter C : ", rmsDifference(en_img, fil_C_img))

# for filter D
fil_D_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        fil_D_img[i][j] = applyFilter(
            normalizeFilter(filter_D), border_img, i, j)

cv.imwrite("Filter_D.jpeg", fil_D_img)
print("RMS value for Filter D : ", rmsDifference(en_img, fil_D_img))

# Display the image
cv.imshow("test-1", en_img)
cv.imshow("test-2", fil_A_img)
cv.imshow("test-3", fil_B_img)
cv.imshow("test-4", fil_C_img)
cv.imshow("test-5", fil_D_img)
cv.waitKey(0)
cv.destroyAllWindows()
