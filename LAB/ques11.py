a=input("enter the numbers:")
a=a.split(" ")
l=map(int,a)
s=[]
s=[x for x in l if x>0]
print(s)
