import cv2
import numpy as np
from stackImage import stackImages


def get_contours(img_input):
    contours, hierarchy = cv2.findContours(img_input, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            obj_cor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if obj_cor == 3:
                object_type = "Tri"
            elif obj_cor == 4:
                asp_ratio = w / float(h)
                if 0.95 < asp_ratio < 1.05:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif obj_cor > 4:
                object_type = "Circles"
            else:
                object_type = "None"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, object_type,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)


path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
get_contours(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)
