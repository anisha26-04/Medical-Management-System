with open("data1.txt","w+") as fp:
# first write then take cursor back and then read
     fp.write("hi we are writting")
     fp.seek(0,0) # (0,0) takes cursor to the start
     s=fp.read()
     print(s)
     fp.write("another statement")
