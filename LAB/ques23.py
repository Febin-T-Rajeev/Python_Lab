def pattern():
    a=int(input("enter the number of steps : "))
    for i in range(1,a+1):
        print()
        for j in range(1,i+1):
            print(i*j," ",end="\t")
pattern()
