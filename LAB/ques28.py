class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
x=Rectangle(2,3)
y=Rectangle(3,4)
if x.area()==y.area():
    print("both are equal")
else:
    print("both are not equal")
    
