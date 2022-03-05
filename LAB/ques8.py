dict1={}
a=int(input("enter the number of values of dictionary :"))
for i in range(a):
    key=input("enter the key")
    value=input("enter the value")
    dict1[key]=value
s=sorted(dict1.items())
print("ascending order is : ",s)
s1=sorted(dict1.items(),reverse=True)
print("descending order is : ",s1)
