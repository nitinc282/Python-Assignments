class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    
    def area(self):
        return self.length*self.length

length=int(input("enter the length:"))
c1=Shape()
c1.area()
c2=Square(length)
c2.area()

print("The area of Shape is", c1.area())
print("The area of Sqaure is", c2.area())

