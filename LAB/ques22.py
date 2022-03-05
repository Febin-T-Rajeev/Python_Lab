def fib():
    n=int(input("enter the limit : "))
    s=0
    a=1
    if n==0:
        print("no series!")
    elif n==1:
        print(a)
    else:
        print(s,a,end=" ")
        for i in range(0,n-2):
            b=s+a
            s=a
            a=b
            print(b,end=" ")
fib()
