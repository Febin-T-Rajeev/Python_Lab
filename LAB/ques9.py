dict1={}
dict2={}
a=int(input("enter the number of values of dictionary 1:"))
for i in range(a):
    key=input("enter the key")
    value=input("enter the value")
    dict1[key]=value
b=int(input("enter the number of values of dictionary 2:"))
for i in range(b):
    key=input("enter the key")
    value=input("enter the value")
    dict2[key]=value
dict1.update(dict2)
print(dict1)
