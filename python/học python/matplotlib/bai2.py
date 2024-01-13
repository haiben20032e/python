import matplotlib.pyplot as plt
# biểu diễn nhiều tập dữ liệu trên 1 biểu đồ
x = [1, 2, 3, 4, 5]

y1 = [1, 2, 3, 4, 10]
y2 = [2, 3, 4, 5, 15]
y3 = [3, 5, 7, 9, 20]

plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go', label='GeenCircle',)
plt.plot([1,2,3,4,5], [2,3,4,5,15], 'b*', label='BlueStars')
plt.plot([1,2,3,4,5], [3,5,7,9,20], 'yD', label='YellowDiamond')
plt.plot(x, y1, 'g--')
plt.plot(x, y2, 'b--')
plt.plot(x, y3, 'y--')
plt.title('Biểu diễn nhiều tập dữ liệu trên 1 đồ thị')
plt.ylabel('Trục Y')
plt.xlabel('Trục X')
# hiển thị chú thích
plt.legend (loc= 'best')
plt.show()
