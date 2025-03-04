with open("data1.txt","r+") as fp:
    # first bring the text to end the write
    fp.seek(0,2)
    fp.write("anisha")