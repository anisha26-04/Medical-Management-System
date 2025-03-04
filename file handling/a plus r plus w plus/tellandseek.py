with open("data.txt","r") as fp:
    s = fp.read(20)
    print(s)
    print("position: ",fp.tell())
    fp.seek(0,0)
    print("after seek")
    print(fp.read())