import matplotlib.pyplot as plt
import numpy as np

# dữ liệu làm nhãn
years=['2016', '2017', '2018', '2019', '2020'] 
index=np.arange(5)
width=0.3
# dữ liệu dòng
total_incomec=[230,250,280,320,328]
total_incomev= [46,48,52,35,40]
# vẽ biểu đồ thanh màu đỏ
plt.bar(index, total_incomec, width, color='red', label='Chong')
plt.bar(index+width, total_incomev,width, color='green', label='Vo')
# thiết lập nhãn cho trục x, y, tiêu đề 
plt.title('Biểu đồ tổng thu nhập 5 năm gần đây của 2 vợ chồng') 
plt.xlabel('Năm')
plt.ylabel('Thu nhập (triệu)')
# thiết lập đánh dấu cho trục x 
plt.xticks(index+width/2, years) 
plt.legend(loc='best')
plt.show()