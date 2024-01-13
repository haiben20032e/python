# nhập tên tuổi
name = input("tên bạn là gì nào ?")
age = int(input("tuổi của bạn bao nhiêu ?"))
dtb = int  
# in ra màn hình
print("name:" + name)
print("tuổi:"+ str (age))
if age > 18:
    print ( " bạn đủ điều kiện")
else : print (" bạn éo đủ điều kiện hahah")
print (" kết thúc chạy trương trình , đừng xuống dòng", end ="")


a = 31
b = 33
if a > b :
    print ( " b lớn hơn a")
elif a == b :
    print (" a và b bằng nhau")

score = 80 
if score >=0  and score <= 50 :
    print ('lever a')
elif score > 50 and score <= 80: 
    print(' lever b ')
elif score >= 80 and score <= 100:
    print('lever c ')
else : 
    print('score fail ')