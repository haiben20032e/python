I = ([1,2,4,6,6],
     [2,1,3,4,5],
     [7,2,6,9,1],
     [4,1,2,1,2])
print(I)
bun_size = int (input("nhập giá trị  bun size;"))
print(bun_size)
import numpy
num_row=int (numpy.shape(I)[0])
num_col=int (numpy.shape(I)[1])
print(num_row)
print(num_col)
for i in range(num_row):
    for j in range(num_col):
        I[i][j] = int(I[i][j] / bun_size) * bun_size
print("Ma trận sau khi thay đổi:")
for row in I:
    print(row)