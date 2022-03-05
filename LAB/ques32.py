class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour  
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return "{0} hours, {1} minutes, {2} seconds".format(self.__hour, self.__minute, self.__second)    
    
    def __add__(self, a):
        hour = self.__hour + a.__hour
        minute = self.__minute + a.__minute
        second = self.__second + a.__second 
        return Time(hour, minute, second) 
    
ob1 = Time(1,2,3)
ob2 = Time(3,4,50)
ob3 = ob1 + ob2

print("The sum of times is: ",ob3)
