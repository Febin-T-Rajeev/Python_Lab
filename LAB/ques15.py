a=input("enter a string:")
x=" "
x=x+a[0]
for i in range(1,len(a)):
    if a[i]==a[0]:
        x=x+"$"
    else :
        x=x+a[i]
print(x)
        
