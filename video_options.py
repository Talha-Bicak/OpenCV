import cv2 as cv
import numpy as np

path = "C:\\Users\\talha\\PycharmProjects\\videos\\video.mp4"
capture = cv.VideoCapture(path)

height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)
out = cv.VideoWriter(path,
                     cv.VideoWriter_fourcc('m', 'p', '4', 'v'), 15,
                     (int(width), int(height)), True)

while True:
    # kameradan görüntü al
    ret, frame = capture.read()

    # görüntü başarıyla alındı mı kontrol et
    if ret is True:
        # okunan görüntüyü ekranda göster
        cv.imshow("video-input", frame)
        out.write(frame)
        # 50 sn sonra çık
        c = cv.waitKey(5000)
        if c == 27:  # ESC I
            break
    else:
        break

# Release the capture and writer objects
capture.release()
out.release()

# Close all OpenCV windows
cv.destroyAllWindows()