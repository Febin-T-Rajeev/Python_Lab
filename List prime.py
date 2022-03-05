lst=[]

n=int(input("Enter how many values to be inserted on a list: "))

for i in range(0,n):
    value=int(input("Enter the value: "))
    if value>=100:
        lst.append('over')
    else:
        lst.append(value)

print("The given list after modification while inserting: ",lst)
        
