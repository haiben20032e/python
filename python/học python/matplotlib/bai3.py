import matplotlib.pyplot as plt # dữ liệu cột
years=[2016,2017,2018, 2019, 2020]
# dữ liệu dòng # vẽ biểu đồ thanh màu đỏ
total_income=[230,250,280,320,328]
plt.bar(years, total_income, color='blue')
plt.title('Biểu đồ tổng thu nhập 5 năm gần đây')
plt.xlabel('Năm')
plt.ylabel('Thu nhập (triệu)')
plt.show()