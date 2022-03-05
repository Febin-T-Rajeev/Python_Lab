lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  
print(lst)
lst.sort() 
if n % 2 == 0:
    median1 = lst[n//2]
    median2 = lst[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = lst[n//2]
print("Median is: " + str(median))