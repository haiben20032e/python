import os
#xóa tệp tin nếu tồn tại
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("tệp tin không tồn tại")
#liệt kê tệp tin và thư mục con trong thư mục
files=os.listdir("demo")
for f in files:
    print(f)
    
# tạo thưu mục nếu chưa tồn tại
if not os.path.exists("example1.txt"):
    os.mkdir("example1")
else:
    print("thư  mục examole1 đã tồn tại")
# xóa thư mục ( thư mục tồn tại phải trống)
if os.path.exists("example1") and len(os.listdir("example1"))==0:
    os.rmdir("example1")
else:
    print("thư mục đang có dữ liệu hoặc đang tồn  tại")