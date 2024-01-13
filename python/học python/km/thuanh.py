import cv2
import os

cap = cv2.VideoCapture(0)  # Mở kết nối với webcam (0 là chỉ số của webcam)

save_path = "E:/image1"  # Đường dẫn để lưu ảnh
os.makedirs(save_path, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại

frame_count = 0  # Biến đếm số lượng khung hình đã được lưu

while True:
    ret, frame = cap.read()  # Đọc khung hình từ webcam
    
    if not ret:
        print("Lỗi lấy khung hình")
        break

    cv2.imshow('frame', frame)  # Hiển thị khung hình từ webcam
    
    k = cv2.waitKey(1)  # Chờ nhận phím nhập
    
    if k == ord('c'):  # Nếu phím 'c' được nhấn
        frame_name = os.path.join(save_path, f'frame_{frame_count}.jpg')  # Tạo tên file cho khung hình
        cv2.imwrite(frame_name, frame)  # Lưu khung hình thành file ảnh
        frame_count += 1  # Tăng số lượng khung hình đã được lưu
        print(f"Đã lưu: {frame_name}")  # In thông báo lưu khung hình thành công

    if k == ord('q'):  # Nếu phím 'q' được nhấn
        break  # Thoát khỏi vòng lặp while
        
cap.release()  # Giải phóng kết nối với webcam
cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ hiển thị
