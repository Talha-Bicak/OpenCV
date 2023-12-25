import cv2 as cv

path = r"C:\Users\talha\Desktop"

src = cv.imread(path + "\\" + "opencv.png")

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
rects, weights = hog.detectMultiScale(src,
                                      winStride=(4,4),
                                      padding=(8,8),
                                      scale=1.25)
for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("hog-detector", src)
cv.waitKey(1)