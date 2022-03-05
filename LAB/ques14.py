a=input("enter the first string")
b=input("enter the second string")
x=a[0]
a=a.replace(a[0],b[0])
b=b.replace(b[0],x)
print(a ,b)
