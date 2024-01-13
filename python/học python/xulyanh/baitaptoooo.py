import cv2
import matplotlib.pyplot as plt
import numpy as np

# Đường dẫn của hình ảnh bạn muốn làm việc với
name_path = ''



# Đọc hình ảnh từ đường dẫn đã cho bằng cv2.imread()
img = cv2.imread(name_path)


# Chuyển ảnh màu thành ảnh xám
anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, anh_den_trang = cv2.threshold(anh_xam, 128, 255, cv2.THRESH_BINARY)

# Tính histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# Hiển thị ảnh xám
plt.subplot(2,4,4)
plt.imshow(anh_xam, cmap='gray')
plt.title('Ảnh Xám')

# Hiển thị ảnh đen trắng
plt.subplot(2,4,5)
plt.imshow(anh_den_trang, cmap='gray')
plt.title('anh den trang')
#hiển thị bản đồ histogram
plt.subplot(2, 2, 4)
plt.plot(hist) 
plt.xlim([0, 256])
plt.title('bản đồ Histogram')

plt.tight_layout()
plt.show()