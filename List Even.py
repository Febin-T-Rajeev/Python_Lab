list=[11,22,33,44,55]
print("List values= ",list)
for i in list:
    if(i%2==0):
     list.remove(i)
print("List after removing Even numbers= ",list)