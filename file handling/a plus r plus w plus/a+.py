with open("data1.txt","a+")as fp:
    # as cursor is at the end bring it to begin
    fp.seek(0,0)
    print(fp.read())