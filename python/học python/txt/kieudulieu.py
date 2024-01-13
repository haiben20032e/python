# tạo 1 list
flowers = ["mai","lan","hồng","cúc","ly","đào"]
print(flowers)
#in phần tử thứ 2
print (flowers[1])
# in phần tư cuối cùng(in lùi thêm dấu "-")
print (flowers[-1])
#  in từ  phần tử 3 - 5 
print (flowers [ 3:5])
# in từ đầu 3 phần tử
print ( flowers [: 3])
#in từ phần tử 3 đến cuối
print (flowers [3:])
#in từ phần tử -5 đến -1
print (flowers [ -5:-1])
#sửa đổi phần tử 
flowers[4]="súng"
print(flowers)
####################################
# sử dụng vòng lặp với list
#in các phần tử trong flowers trên dòng
for f in flowers:
    print(f)
#duyệt và lấy các flower có chứa chữ a
newflowers=[]
for f in flowers:
    if " a" in f:
        newflowers.append(f)
print(newflowers)
# có thể viết rút gọn inline
newflowers=[f for f in flowers if 'a'in f]
print( newflowers)
#kiểm tra sự tồn tại của phần tử trong list
if "mai"in flowers:
    print("chúc mừng mai")
# lấy độ dài list
print(len(flowers))