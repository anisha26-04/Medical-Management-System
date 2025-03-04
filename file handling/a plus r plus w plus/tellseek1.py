with open("data.txt","r") as fp:
    fp.seek(10,0)
    s= fp.read(20)
    print(fp.tell())
    print(s)