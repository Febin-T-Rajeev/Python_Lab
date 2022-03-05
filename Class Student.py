class Student:
    marks = []
    def readData(self, rollno, name, mark1, mark2):
        Student.rollno = rollno
        Student.name = name
        Student.marks.append(mark1)
        Student.marks.append(mark2)
        
    def printDetails(self):
        print ("Roll Number is: ", Student.rollno)
        print ("Name is: ", Student.name)
        print ("Marks are: ", Student.marks)
        print ("Total Marks are: ", self.ComputeTotal())
        
    def ComputeTotal(self):
        return (Student.marks[0] + Student.marks[1])
    

s1 = Student()
s2 = Student()
s3 = Student()
s2.readData(1, "Vipin", 20 , 25)
s2.readData(2, "Vishnu", 25 , 28)
s3.readData(3, "Vyshak", 24, 26)
s1.printDetails()
s2.printDetails()
s3.printDetails()
