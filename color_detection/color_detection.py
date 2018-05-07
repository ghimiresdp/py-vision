"""
Originally created by Sudip Ghimire [ https://github.com/ghimiresdp ]

Color Detection by masking colors with Open CV
The colors detected in sufficient lighting are as follows:
    Blue
    Pink
    Orange
    Violet
    Green
    Yellow
    Red
    Black


"""

import cv2
import numpy as np
colors = ['orange', 'violet', 'blue', 'green', 'yellow', 'red', 'black', 'pink']
font = cv2.FONT_HERSHEY_SIMPLEX


def mask_color(pic, x):
    pic = cv2.medianBlur(pic, 5)
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)

    if x == 'blue':
        lower = np.array([80, 60, 60])
        upper = np.array([110, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'pink':
        lower = np.array([150, 127, 127])
        upper = np.array([170, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'orange':
        lower = np.array([0, 0, 0])
        upper = np.array([10, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'violet':
        lower = np.array([110, 60, 60])
        upper = np.array([160, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'green':
        lower = np.array([40, 60, 60])
        upper = np.array([80, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'yellow':
        lower = np.array([10, 60, 60])
        upper = np.array([30, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'red':
        lower = np.array([170, 60, 60])
        upper = np.array([180, 255, 255])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask

    elif x == 'black':
        lower = np.array([0, 0, 0])
        upper = np.array([255, 100, 80])
        mask = cv2.inRange(pic, lower, upper)
        result = cv2.bitwise_and(pic, pic, mask=mask)
        return mask


def detect_color():
    cap = cv2.VideoCapture(0)  # capture video from primary camera (0)
    while 1:
        _, pic = cap.read()
        pic = cv2.medianBlur(pic, 3)
        img2 = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img2, 127, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(img, contours, -1, (50, 255, 0), 2)
        # img = cv2.flip(img,1)
        for cnt in contours:
            if 60000 > cv2.contourArea(cnt) > 5000:
                [x, y, w, h] = cv2.boundingRect(cnt)
                cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 0, 255), 2)
                roi = pic[y:y + h, x:x + w]
                ww, hh = roi.shape[:2]
                for color in colors:
                    mask = mask_color(roi, color)
                    sum_of_pixels = 0
                    for line in range(0, ww):
                        px = mask[line, hh // 2]
                        sum_of_pixels += px
                    if sum_of_pixels > ww / 4 * 255:
                        cv2.putText(roi, color, (10, 50), font, 0.8, (255, 255, 0), 1, cv2.LINE_AA)
                        cv2.putText(roi, color, (12, 52), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                        # break
                        # cv2.imshow("ROI", roi)
            cv2.imshow("Image", pic)
            # cv2.imshow("Thresh", thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break


detect_color()
