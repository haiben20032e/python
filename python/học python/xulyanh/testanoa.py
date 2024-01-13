import cv2
import matplotlib.pyplot as plt

name_path = 'e:/baitaptesst/hi.JPG'
img = cv2.imread(name_path)

crop = img[100:300, 100:300]

plt.imshow(crop[:, :, ::-1])


copy = img.copy()
copy[100:200, 100:200] = [0, 0, 255]

plt.imshow(copy[:, :, ::-1])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
