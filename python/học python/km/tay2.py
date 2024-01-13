import cv2
import mediapipe as mp
import numpy as np
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

palm_img_path = 'palm_images'
if not os.path.exists(palm_img_path):
    os.makedirs(palm_img_path)

img_counter = 0 

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    output = hands.process(rgb_frame)

    if output.multi_hand_landmarks:
        for hand_landmark in output.multi_hand_landmarks:
            x_max = 0
            y_max = 0
            x_min = frame_width
            y_min = frame_height
            
            for landmark in hand_landmark.landmark:
                x, y = int(landmark.x * frame_width), int(landmark.y * frame_height)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2) 
            hand_frame = frame[y_min:y_max, x_min:x_max]
            
            cv2.imwrite(os.path.join(palm_img_path ,'{}.jpg'.format(img_counter)), hand_frame)
            img_counter += 1
    
    cv2.imshow('Palm Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()