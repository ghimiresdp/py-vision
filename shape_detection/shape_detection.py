"""
Originally created by Sudip Ghimire [ https://github.com/ghimiresdp ]
The Shapes detected in sufficient lighting are as follows:
Triangle
Rectangle
Pentagon
Hexagon
Heptagon
Circle (for more than 7 vertices detected)

"""
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX


def detect_shape():
    cap = cv2.VideoCapture(0)  # capture video from primary camera (0)
    while 1:
        _, pic = cap.read()
        # pic = cv2.medianBlur(pic, 5)
        pic2 = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(pic2, 100, 255, cv2.THRESH_BINARY)
        _, contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if 60000 > cv2.contourArea(cnt) > 5000:
                approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
                [x, y, w, h] = cv2.boundingRect(cnt)
                # print len(approx)
                if len(approx) == 3:
                    cv2.putText(pic, "Triangle", (x, y + h // 2), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    # print "Triangle"
                    cv2.drawContours(pic, [cnt], 0, (0, 0, 255), 3)

                elif len(approx) == 4:
                    # print "Rectangle"
                    cv2.putText(pic, "Rectangle", (x, y + h // 2), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.drawContours(pic, [cnt], 0, (0, 0, 255), 3)

                elif len(approx) == 5:
                    # print "Pentagon"
                    cv2.putText(pic, "Pentagon", (x, y + h // 2), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.drawContours(pic, [cnt], 0, (0, 0, 255), 3)

                elif len(approx) == 6:
                    # "Hexagon"
                    cv2.putText(pic, "Hexagon", (x, y + h // 2), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.drawContours(pic, [cnt], 0, (0, 0, 255), 3)

                elif len(approx) == 7:
                    # print "Heptagon"
                    cv2.putText(pic, "Heptagon", (x, y + h // 2), font, 0.8, (0, 0, 255), 1, cv2.LINE_8)
                    cv2.drawContours(pic, [cnt], 0, (0, 0, 255), 3)

                elif 20 > len(approx) > 10:
                    # print "circle"
                    cv2.putText(pic, "Circle", (x, y + h // 2), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.drawContours(pic, [cnt], 0, (0, 0, 255), 3)
        cv2.imshow('Shape', pic)
        # cv2.imshow('Cont', thresh)
        # cv2.matchShapes(contour1, contour2, method, parameter)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break


detect_shape()