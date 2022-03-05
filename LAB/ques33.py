f1=open("file1.txt","r")
f2=open("file2.txt","w")
data=f1.readlines()
for i in range(0,len(data)):
    if(i%2 !=0):
        f2.write(data[i])
    else:
        pass
f2.close()

f2=open("file2.txt","r")
data1=f2.read()
print(data1)
f1.close()
f2.close()
