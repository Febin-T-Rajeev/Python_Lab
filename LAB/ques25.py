a=input("enter the words:")
a=a.split(" ")
x=0
for i in a:
    if len(i)>x:
        x=len(i)
print(x)

    
