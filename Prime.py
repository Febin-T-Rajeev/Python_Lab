limit = int(input("Enter Range:"))
print("Prime numbers upto ",limit," are: ")
for i in range(1, limit+1):
    if(i>1):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                break
        else:
            print(i,end=" ")

