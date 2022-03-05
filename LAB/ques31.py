class Rectangle:
    def __init__(self, length, width):
        self.__length = length  
        self.__width = width
        self.area = length*width
    
    def __gt__(self, a):
        if(self.area>a.area):
            return True
        else:
            return False

ob1 = Rectangle(2,3)
ob2 = Rectangle(3,4)

if(ob1>ob2):
    print("Area of Rectangle 1 is greater than Rectangle 2")
else:
    print("Area of Rectangle 2 is greater than Rectangle 1")
