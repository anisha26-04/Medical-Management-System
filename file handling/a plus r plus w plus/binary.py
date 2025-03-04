with open("data.txt","rb") as fp:
    fp.seek(-10,2)
    s= fp.read()
    print(type(s))
    s=s.decode("utf-8")
    print(s)