"""
Originally created by Sudip Ghimire [ https://github.com/ghimiresdp ]

"""

import cv2
face = cv2.CascadeClassifier('face.xml')
font = cv2.FONT_HERSHEY_SIMPLEX


def face_track():
    cap = cv2.VideoCapture(0)  # capture video from primary camera (0)
    while 1:
        _, pic = cap.read()
        # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        item = face.detectMultiScale(pic, 1.3, 5)
        xx = 0
        yy = 0
        for (x, y, w, h) in item:
            cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 255, 255), 2)
            # cv2.putText(pic, 'Detected', (x, y), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
            xx = x + w / 2
            yy = y + h / 2
            ww, hh = pic.shape[:2]
            if xx < 0.5 * ww and xx != 0:
                cv2.putText(pic, 'towards left', (x, y + h / 3), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            elif xx > 0.8 * ww and xx != 0:
                cv2.putText(pic, 'towards right', (x, y + h / 3), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

            if yy < 0.3 * hh and yy != 0:
                cv2.putText(pic, 'towards top', (x, y + h * 2 / 3), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            elif yy > 0.5 * hh and yy != 0:
                cv2.putText(pic, 'towards bottom', (x, y + h * 2 / 3), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            text = 2500.0 / w * 3.66
            text = int(text)
            txt = str(text) + "cm Far"
            # cv2.putText(pic, 'Target @ Centre',(x, y+h/2), font, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(pic, txt, (x+10, y + h / 2), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("output", pic)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break


face_track()