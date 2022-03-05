a=int(input("\n enter a number:\t"))
s=0
n=a
while a!=0:
    rem=a%10
    s=s+(rem*rem*rem)
    a=a//10
if s==n:
    print("\n The number is amstrong\n")
else:
    print("\n The number is not amstrong\n")
