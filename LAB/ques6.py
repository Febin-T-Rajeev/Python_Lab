a=input("enter the numbers:")
a=a.split(" ")
a=list(map(int,a))
new=[]
for i in range(0,int(len(a))):
    if a[i]%2!=0:
        new.append(a[i])
print(new)
