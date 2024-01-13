import math

def pt(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

# Nhập các hệ số a, b, c từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Giải phương trình
solutions = pt(a, b, c)

# In kết quả
if solutions is None:
    print("Phương trình không có nghiệm thực.")
else:
    print("Nghiệm của phương trình là:", solutions)
