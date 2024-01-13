import numpy as np

# Nhập số hàng và số cột của mảng
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

# Sử dụng NumPy để tạo mảng hai chiều và nhập giá trị
my_array = np.zeros((rows, cols), dtype=int)

for i in range(rows):
    for j in range(cols):
        my_array[i][j] = int(input(f"Nhập giá trị tại [{i}][{j}]: "))

# In mảng
print("Mảng đã nhập:")
print(my_array)
rows = int(input("Nhập số hàng: "))
columns = int(input("Nhập số cột: "))
 # Khởi tạo ma trận
matrix = [[0 for i in range(columns)] for i in range(rows)]
 # Nhập giá trị của ma trận
for i in range(rows):
    for j in range(columns):
        matrix[i][j] =int(input("Nhập phần tử thứ ({},{}): = " .format(i, j)))
# Đếm số lượng số 1, số 2 và số 3 trong ma trận
count_1 = 0
count_2 = 0
count_4 = 0
count_3 = 0
count_7 = 0
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 1: 
            count_1 += 1
        elif matrix[i][j] ==2: 
            count_2 += 1 
        elif matrix[i][j] == 3: 
            count_3 += 1
        elif matrix[i][j] == 4: 
            count_4 += 1
        elif matrix[i][j] == 7:
            count_7 += 1
# bun_size

# In ra số lượng số 1, số 2 và số 3 trong ma trận
print("Số lượng số 1:", count_1)
print("Số lượng số 2:", count_2)
print("Số lượng số 3:", count_3)
print("Số lượng số 4:", count_4)
print("Số lượng số 7:", count_7)