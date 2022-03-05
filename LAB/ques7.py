a=input("enter colours of list1:")
b=input("enter colours of list2:")
a=a.split(" ")
b=b.split(" ")
print("list 1:",a)
print("list 2:",b)
l=[]
for i in range(0,len(a)):
        if a[i] not in b:
            l.append(a[i])
print(l)
