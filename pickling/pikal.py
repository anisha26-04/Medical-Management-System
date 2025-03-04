from stu import Student
import pickle

def serialize(data):
    fp = open("data.fbs","wb")
    pickle.dump(list1,fp)
    fp.close()

def desealize():
    output= []
    fp=open("data.fbs","rb")
    output = pickle.load(fp)#from fp read ,converting to output(list)
    fp.close()
    return output

if(__name__ == "__main__"):
    s1=Student(101,"mansi",80)
    s2=Student(102,"anisha",99)
    s3=Student(103,"pranjali",97)
    list1 =[s1,s2,s3]
    serialize(list1)

    output = desealize()
    print(output)
    for x in output:
        print(x)
