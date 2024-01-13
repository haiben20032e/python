

#hàm có tham số
def showWelcome():
    print("welcome",msg)
# gọi hàm 
#showWelcome("lại đức trung")

# hàm cộng 2 số
def add ( a,b):
    return a + b

#GỌI hàm
sum=add( 4,5 )
print("tổng 2 số là ", sum)
# định nghĩa hàm với số tham số chưa biết trước 
def showEvenNumber(*number):
    for n in number:
        if n%2==0:
            print(n)
showEvenNumber(3,5,7,2,89,34,2)

#truyền giá trị bằng cách chỉ ra tên tham số

def sumthree(a,b,c):
    return a+b+c
#gọi hàm 
s=sumthree(c=5,a=6,b=2)

print(s)

#định nghĩa hàm với tham số chỉ ra tên chưa biết trước
def showMessage(**msg):
    print("welcome to ",msg["p1"])
#gọi hàm 
showMessage(p1= " my home")
#định nghĩa hàm chỉ ra giá trị mặc định cho tham số
#tham số mặc định không dc nằm trước tham số thường
def div( a,b=1):
    return a/b
#gọi hàm
print(div(6))
print(div(6,2))
#định nghĩa hàm trống
def funcEmpty():
    pass
#gọi hàm
funcEmpty()
#định nghĩa hàm đệ quy - tính gia thừa
def factorial(k):
    if k ==1:
        return 1
    else:
        return k*factorial(k-1)
    
#gọi hàm
print("giai thừa của 5 là", factorial(5))

