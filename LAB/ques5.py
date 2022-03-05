a=input("enter the numbers in list 1:")
a=a.split(" ")
a=list(map(int,a))
b=input("enter the numbers in list 2:")
b=b.split(" ")
b=list(map(int,b))
print(a)
print(b)
if len(a)==len(b):
    print("the lists are of same length")
else:
    print("the lists are of different length")

s=0
s1=0
for i in range(0,int(len(a))):
    s=s+a[i]
for j in range(0,int(len(b))):
    s1=s1+b[j]
if s1==s:
    print("the lists sums equal")
else:
    print("the list sums different")
l=[]
for m in range(0,int(len(a))):
    for n in range(0,int(len(b))):
        if a[m]==b[n]:
            l.append(a[m])
if len(l)==0:
    print("no common elemnts")
else:
    print("the common elents are:",l)
