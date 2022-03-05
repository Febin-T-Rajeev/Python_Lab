class employee:
    def __init__(self,empid,name,salary,address):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.address=address
class teacher(employee):
    def __init__(self,empid,name,salary,address,department,subject):
        employee.__init__(self,empid,name,salary,address)
        self.department=department
        self.subject=subject
    def display(self):
        print("Employee ID:\t",self.empid,"\nName:\t\t",self.name,"\nSalary:\t\t",self.salary,"\nAddress:\t",self.address,"\nDepartment:\t",self.department,"\nSubject:\t",self.subject)
i=int(input("Enter the employee id:\t"))
n=input("Enter the employee name:\t")
s=int(input("Enter the salary of the employee:\t"))
a=input("Enter the address of the employee:\t")
d=input("Enter the department of the employee:\t")
sub=input("Enter the subject of employee:\t")
ob=teacher(i,n,s,a,d,sub)
ob1=employee(i,n,s,a)
ob.display()
