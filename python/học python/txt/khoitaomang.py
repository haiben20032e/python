import numpy as np
#khởi chạy mảng 1 chều với kiểu dữ liệu mặc định
arr1 = np.array([1,3,4,5,6])

arr1 = np.array([1,3,4,5,6],dtype = int)
# khởi tạo mảng 1 chiều với kiểu dữ liệu các phần tử là integer
arr2 = np.array([(4,5,6), (1,2,3)],dtype = int)
#khởi chạy mảng 3 chiều
arr2= np.array(([(2,4,0,6),(4,7,5,6)],
                [(0,3,2,1),(9,4,5,6)],
                [(5,8,6,4),(1,4,6,8)]),dtype= int)
#khởi tạo mảng vưới các hàm có sẵn
farr1=np.zeros(5,dtype=int)#mảng 1 chiều 5 phần tử với giá trị 0
farr2=np.zeros((3,5),dtype=int)# mảng 2 chiều 3x5 với phần tử giá trị 0
farr3=np.ones((3,4,5),dtype=int)# mảng 3 chiều 3x5x4 phần tử với giá trị 1
farr11=np.arange(1,10,2) # mảng 1 chiều từ giá trị từ 1-10 bước nhảy 2
farr22=np.full((2,3),5)# mảng 2 chiều các phần tử 5 với kích thước 4x4
matrix=np.eye(4,dtype=int) # ma trận đơn vị kích thước là 4x4
matrix_rd=np.random.random((6,8))# ma trận các phần tử ngẫu nhiên từ 0.0- 1.0 với kích thước 6x8
print(matrix_rd)
#thao tác với mảng
print ("kiểu dữ liệu của phần tử trong mảng:",arr2.dtype)
print ("số phần tử trong mảng:",arr2.shape)
print ("kích thước của mảng:",arr2.size)
print ("số chiều của mảng:",arr2.ndim)
print("Giá trị lớn nhất của mảng arr1 là:", np.max(arr1))
print("Giá trị nhỏ nhất của mảng arr2 là:", np.min(arr2))
print("Tổng tất cả các phần tử của mảng arr1 là:", np.sum(arr1)) 
print("Trung bình cộng tất cả các phần tử của mảng arr1 là:", np.mean(arr1)) 
print("Giá trị trung vị của mảng arr2 là:", np.median(arr2))





