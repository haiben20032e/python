import cv2

# Đọc hình ảnh màu
anh_mau = cv2.imread('e:/a.jpg')

# Chuyển ảnh màu thành ảnh xám
anh_xam = cv2.cvtColor(anh_mau, cv2.COLOR_BGR2GRAY)
#tăng độ sáng cho ảnh
h, w, c = anh_mau.shape 

# Hiển thị ảnh màu và ảnh xám
cv2.imshow('Anh mau', anh_mau)
cv2.imshow('Anh xam', anh_xam)
# Đợi cho đến khi nhấn một phím bất kỳ để thoát
cv2.waitKey(0)
# Lưu ảnh xám vào đĩa
cv2.imwrite('anh_xam.jpg', anh_xam)