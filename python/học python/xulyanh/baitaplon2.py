import cv2
import matplotlib.pyplot as plt
import numpy as np

# Đường dẫn của hình ảnh bạn muốn làm việc với
name_path = 'e:/baitaptesst/hi.JPG'



# Đọc hình ảnh bằng cv2.imread()
img = cv2.imread(name_path)

# Tăng độ sáng bằng cách thêm một giá trị cố định cho tất cả các pixel
brightness_increase = 100 #khai báo giá trị
brightened_img = np.where((255 - img) < brightness_increase, 255, img + brightness_increase)

# Giảm độ sáng bằng cách trừ một giá trị cố định từ tất cả các pixel
brightness_decrease = 100
darkened_img = np.where(img < brightness_decrease, 0, img - brightness_decrease)

# Tạo lưới 1x3 cho các khu vực hiển thị (1 hàng x 3 cột)
plt.figure(figsize=(12, 4))

# Hiển thị ảnh ban đầu
plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Ảnh Gốc')

# Hiển thị ảnh tăng độ sáng
plt.subplot(132)
plt.imshow(cv2.cvtColor(brightened_img, cv2.COLOR_BGR2RGB))
plt.title('Ảnh Tăng Độ Sáng')

# Hiển thị ảnh giảm độ sáng
plt.subplot(133)
plt.imshow(cv2.cvtColor(darkened_img, cv2.COLOR_BGR2RGB))
plt.title('Ảnh Giảm Độ Sáng')

plt.show()