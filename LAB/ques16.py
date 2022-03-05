a=input("enter the sentence:")
a=a.split(" ")
s={}
for i in a:
    if i in s:
        s[i]=s[i]+1
    else:
        s[i]=1
print(s)
