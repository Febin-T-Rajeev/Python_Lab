def biggest_3(a,b,c):

    if(a>b):
        if(a>c):
            print(a," is the biggest")
        else:
            print(c," is the biggest")

    else:
        if(b>c):
            print(b," is the biggest")
        else:
            print(c," is the biggest")


n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))

biggest_3(n1,n2,n3)


            
