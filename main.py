import cv2
import numpy as np
import pyautogui
import sys
lowerh,lowers,lowerv=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
upperh,uppers,upperv=int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])

cap = cv2.VideoCapture(0)

lower_arr = np.array([lowerh,lowers,lowerv])
upper_arr = np.array([upperh, uppers, upperv])
prev_y = 0

while True:
    ret, frame = cap.read()
    #cv2.cvtColor() method is used to convert an image from one color space to another
    #bg2bg2 pan hoy apde hsv aetle hue saturation value jena ma usuluy tracking that
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    mask  = cv2.inRange(hsv, lower_arr, upper_arr)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)           
        if area > 5000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            if y < prev_y:
                pyautogui.press('space')
                # print("det")
            prev_y = y
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()