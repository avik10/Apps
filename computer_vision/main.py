import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)
lower_red0 = np.array([0,50,50])
upper_red0 = np.array([10,255,255])
lower_red1 = np.array([170,50,50])
upper_red1 = np.array([180,255,255])
prev_Y = 0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv,yellow_lower,yellow_upper)
    mask0 = cv2.inRange(hsv, lower_red0, upper_red0)
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask = mask0 + mask1
    contours, hirarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 20000:
            x,y,w,h =  cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y),(x+w, y+h),(0, 255, 0), 5)
            if y < prev_Y :
                print(area)
                pyautogui.press('down')
            # elif y > prev_Y:
            #     pyautogui.scroll(10)
            #     print('UP')
            prev_Y = y
    cv2.imshow('Frame', hsv)
    cv2.imshow('Mask', mask)
    if ord('q') == cv2.waitKey(10) & 0xff:
        break

cap.release()
cv2.destroyAllWindows()