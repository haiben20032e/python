#mở tệp tin demofile.txt để ghi hoặc ghi đè dữ liệu
#liệu , tạo tệp tin nếu không còn tồn tại
fw = open ("demofile.txt","wt",encoding="utf-8")
data= " dữ liệu nhạy cảm"
fw.write(data)
fw.close()
#mở tệp tin để đọc
fr=open ("demofile.txt","r",encoding="utf-8")
content =fr.read()
print(content)
fr.close()
#mở tệp tin để đọc với lệnh with ( tự đóng)
with open ("demofile.txt",encoding="utf-8")as f:
    c=f.read()
    print(c)
#mở tệp tin để ghi bổ sung
with open ("demofile.txt","a",encoding="utf-8")as f:
    f.write("\nvui lòng không chia sẻ")
#mwor dể đọc
with open("demofile.txt","r",encoding="utf-8")as f:
    content=f.read().splitlines()
    for line in content:
        print(line.strip())