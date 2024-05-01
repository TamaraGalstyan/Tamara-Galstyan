#Ex1 2 3 4
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def __init__(self):
        print('Shape')
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r=r
    def perimeter(self):
        if self.r>0:
            return 2 * math.pi * self.r
        else:
            print('Invalid r')
    def area(self):
        return math.pi * self.r ** 2
circle1=Circle(3)
print(circle1.perimeter())
print(circle1.area())

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def perimeter(self):
        if self.a and self.b>0:
            return (self.a+self.b)*2
        else:
            print('invalid a and b')
    def area(self):
        if self.a and self.b>0:
            return self.a*self.b
        else:
            print('invalid a and b')
rectangle1=Rectangle(1,2)
print(rectangle1.perimeter())
print(rectangle1.area())

class Triangle(Shape):
    def __init__(self, a,b,c,angle):
        self.a=a
        self.b=b
        self.c=c
        self.angle=angle
    def perimeter(self):
        if self.a and self.b and self.c and self.angle>0:
            return  self.a+self.b+self.c
        else:
            print('invalid args')
    def area(self):
        if self.a and self.b and self.c and self.angle>0:
            return  self.a * self.b * math.sin(self.angle)/2 
        else:
            print('invalid args')
triangle1=Triangle(1,2,3,50)
print(triangle1.perimeter())
print(triangle1.area())









    
    
