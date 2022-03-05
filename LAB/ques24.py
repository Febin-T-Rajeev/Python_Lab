def factor():
    a=int(input("enter the number"))
    print("The factors of %d are:" %a)
    for i in range(1,a+1):
        if (a%i)==0:
            print(i)
factor()
