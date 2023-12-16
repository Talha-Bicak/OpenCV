import cv2 as cv
import numpy as np

path = r"C:\Users\talha\Desktop"

img = cv.imread(path + "\\" + "opencv.png")

type(img)

# cv.namedWindow("opencv_test",
#                cv.WINDOW_AUTOSIZE)  # İkinci parametre resmin boyutlarının standart boyutlarda olmasını sağlar.
# cv.imshow("opencv_test", img)
# cv.waitKey(1)
#
# cv.destroyAllWindows()
#
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Gri skalasına çevirme
cv.imshow("gray", gray)
cv.waitKey(4000)

cv.imwrite(path + "gray_opencv.png", gray)
cv.destroyAllWindows()

# img = cv.imread(path + "\\" + "opencv.png", cv.IMREAD_GRAYSCALE)  # Görüntüyü Gri skalasında okuma
# cv.imshow("Gray", img)
# cv.waitKey(1)

m1 = np.copy(img)
m2 = img
type(img)
img[100:200, 200:300, :] = 255
cv.imshow("m2", m2)
cv.waitKey(1000)

cv.waitKey(1)
img = np.ones((550, 770, 3))
black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
cv.rectangle(img, (480, 250), (100, 450), black, 8)
cv.rectangle(img, (580, 150), (200, 350), black, 8)
cv.line(img, (100, 450), (200, 350), black, 8)
cv.line(img, (480, 250), (580, 150), black, 8)
cv.line(img, (100, 250), (200, 150), black, 8)
cv.line(img, (480, 450), (580, 350), black, 8)
start_point = (150, 100)
font_thickness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX
cv.putText(img, 'www.harikaresimcizerim.com', start_point, font, font_size, black, font_thickness)
cv.imshow('dikdortgen', img)
cv.waitKey(3000)

# Görüntünün belirli bir kısmını alma

h, w, ch = img.shape
print("h, w, ch", h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = [b, g, r]
cv.imshow("output", img)
cv.waitKey(3000)
cv.destroyAllWindows()

# Görüntüleri birleştirme
img10 = img
cv.imshow("gray_scala", img10)
cv.waitKey(1000)
cv.imshow("original_scala", img)
cv.waitKey(1000)
horizontal = np.hstack((img, img10))
cv.imshow("Birleştirme", horizontal)
cv.waitKey(5000)
cv.destroyAllWindows()

# Görüntünün istatistiksel değerleri ve bu değ*erleri kullanma

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min loc:", min_loc, ",", "max loc:", max_loc)

# meanStdDev

means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means.item(), stddev.item()))
gray[np.where(gray < means)] = 0
gray[np.where(gray > means)] = 255
cv.imshow("binary", gray)
cv.waitKey(4000)

gray = np.float32(gray)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

means, stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)
cv.imshow("NORM_MINMAX", dst)
cv.waitKey(10000)
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
means, stddev = cv.meanStdDev (dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

### NORM_INF ###

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(1)

### NORM_L1 ###

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(1)

## NORM_L2 ###

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L2", np.uint8(dst*10000))
cv.waitKey(1)