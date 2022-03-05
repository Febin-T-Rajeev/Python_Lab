a=int(input("enter a number:"))
s=0
while a!=0:
    rem=a%10
    s=(s*10)+rem
    a=a//10
print(s)
