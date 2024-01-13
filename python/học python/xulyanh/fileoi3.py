with open ("thovui.txt"," r", encoding = " utf -8 ") as f:
    content= f.readline()
    print(content)
    for l in content :
        print (l, end = "")
with open ("thovui.txt", " r", encoding="ùt - 8 ") as f:
    line = f.readline()
    while not line:
        print (line, end= "")
        line=f.readline()
