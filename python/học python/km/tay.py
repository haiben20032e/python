import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()  

cap = cv2.VideoCapture(0)

connections = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10],
               [10, 11], [11, 12], [0, 13], [13, 14], [14, 15], [15, 16], [0, 17], [17, 18],
               [18, 19], [19, 20], [5, 9], [9, 13], [13, 17]]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    height, width, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            landmark_list = []
            for idx, point in enumerate(hand_landmarks.landmark):
                x, y = int(point.x * width), int(point.y * height)
                landmark_list.append((x, y))
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Tìm tọa độ x, y của hình chữ nhật bao quanh bàn tay
            x_min, x_max = min(landmark_list, key=lambda x: x[0])[0], max(landmark_list, key=lambda x: x[0])[0]
            y_min, y_max = min(landmark_list, key=lambda x: x[1])[1], max(landmark_list, key=lambda x: x[1])[1]

            # Vẽ vòng tròn bao quanh khu vực bàn tay
            center = ((x_min + x_max) // 2, (y_min + y_max) // 2)
            radius = max((x_max - x_min) // 2, (y_max - y_min) // 2)
            cv2.circle(frame, center, radius, (255, 0, 0), 2)

            for connection in connections:
                point1, point2 = landmark_list[connection[0]], landmark_list[connection[1]]
                cv2.line(frame, point1, point2, (0, 0, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
