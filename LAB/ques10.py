a=int(input("enter the first numnber:"))
b=int(input("enter the second number:"))
if a<b:
    num=a
else:
    num=b
for i in range(1,num+1):
    if((a%i==0) and (b%i==0)):
        s=i
print(s)
