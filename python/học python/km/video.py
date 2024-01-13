import cv2

# Tải mô hình phát hiện khuôn mặt đã được đào tạo sẵn từ OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("D:/Khung_hinh/cam_video_with_faces.mp4", vid_cod, 20.0, (640, 480))

while True:
    ret, frame = vid_capture.read()
    if not ret:
        break

    # Chuyển đổi khung hình sang màu xám để phát hiện khuôn mặt
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt trong khung hình
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Vẽ hình chữ nhật xung quanh khuôn mặt đã phát hiện
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Video của tôi với khuôn mặt", frame)
    output.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

vid_capture.release()
output.release()
cv2.destroyAllWindows()
