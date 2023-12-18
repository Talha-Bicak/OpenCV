import cv2 as cv
import numpy as np

path = "C:\\Users\\talha\\Desktop\\opencv.png"
src = cv.imread(path)
T = 127
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
for i in range(5):
    ret, binary = cv.threshold (gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)
    cv.waitKey(3000)