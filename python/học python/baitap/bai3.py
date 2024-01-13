def tong(n):
    tong = 0
    for i in range(1,n+1):
        tong += i
    return tong

n = int(input("Nhập n: "))
ket_qua = tong(n)
print("tong từ 1 đến", n, "là", ket_qua)