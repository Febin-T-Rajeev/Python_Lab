list1=[1,2,3]
list2=[3,5,6]
print(len(list1))
print(len(list2))
if len(list1)==(len(list2)):
    print("Length is same")
else :
    print("Length is not Same")
if sum(list1)==sum(list2):
    print("Sum is same")
else :
    print("Sum is not same")
s1=(set(list1))
print(set(list1))
s2=(set(list2))
print(set(list2))
s3=s1.intersection(s2)
print(s3)