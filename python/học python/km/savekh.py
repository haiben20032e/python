import cv2

cap = cv2.VideoCapture(0)

# Thiết lập codec và tạo đối tượng ghi video
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('E:/image1/video.mp4', fourcc, 30, (640,480))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không đọc được frame")
        break
    
    # Ghi từng frame vào video
    out.write(frame)

    # Hiển thị    
    cv2.imshow('frame',frame)
    
    # Nhấn q để thoát 
    if cv2.waitKey(1) == ord('q'):
        break
        
# Giải phóng camera
cap.release()
out.release()
cv2.destroyAllWindows()