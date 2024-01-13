#mở tệp tin và ghi ra 1 list
fw=open("thovui.txt","w",encoding="utf-8")
data=["ngày xưa sung sức thì nghèo\n",
      "ngày nay rủng rỉnh nó teo mất rồi\n",
      "ngày xưa như sắt như đồng\n",
      "ngày nay như cải muối dưa\n",
      "mười tháng minh mạng vẫn chưa ngỏng đầu\n"]
fw.writelines(data)
fw.close()
with open ("thovui.txt","r", encoding = " utf -8 ") as f:
    content= f.readlines()
    print(content)
    for l in content :
        print (l, end = "")
with open ("thovui.txt", " r", encoding="uft - 8 ") as f:
    line = f.readline()
    while not line:
        print (line, end= "")
        line=f.readline()
