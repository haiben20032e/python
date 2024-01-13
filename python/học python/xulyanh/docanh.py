import cv2
import matplotlib.pyplot as plt
name_path ='e:/a.jpg'
img = cv2.imread(name_path)
#chỉnh cỡ ảnh
h,w = img.shape[:2]
resized=cv2.resize(img,(500,500))
plt.imshow(resized[:,:,::-1])
#lưu ảnh
cv2.imwrite('e:/baitaptesst/hi.JPG',resized)
#hiển thị ảnh bằng open cv
crop=img[100:300,100:300]
plt.imshow(crop[:,:,::-1])
#chuyển màu vungfnta vừa cop thành màu xanh:
copy = img.copy()
copy[100:100,200:200] = [255,0,0]
#assing blue color
plt.imshow(copy[:,:,::-1])
cv2.imshow('test',copy)
cv2.waitKey(0)

