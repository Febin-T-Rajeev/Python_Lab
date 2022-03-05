list_1=[10,20,30,40,50]
print("Given list is:")
print(list_1)
item=int(input("Enter item to be searched"))

flag=0
for i in list_1:
    if(item==i):
        print("The element found at position: ",list_1.index(item)+1)
        flag=1
        break
if(flag==0):
    print("Item not found!!!")
        
        
