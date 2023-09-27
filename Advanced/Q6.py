#Single Inheritance Example:

class Person:
    def __init__(self,name='',age=0):
        self.name=name
        self.age=age

    def details1(self):
        return f"Student Name is {self.name} and student age is {self.age}"

class Student(Person):
    def __init__(self,nm='',ag=0,classs='',branch=''):
        super().__init__(nm,ag)
        self.classs=classs
        self.branch=branch
    def details2(self):
        return f"{super().details1()} and Student class is {self.classs} and student branch is {self.branch}"
    
S=Student("Amit", 34,"B.tech","CS")
print(S.details2())
print(S.details1())


#Multiple inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details1(self):
        return f"I am {self.name} and I am {self.age} years old."

class Skills:
    def __init__(self,skills):
        self.skills=skills

    def details2(self):
        return f"My skills include: {self.skills}."
    
class Programmer(Person,Skills):
    def __init__(self,name,age,skills,program):
        Person.__init__(self,name, age)
        Skills.__init__(self,skills)
        self.program=program

    def details3(self):

        return f"{super().details1()} {super().details2()} and Program name is {self.program}"


programmer = Programmer("Alice", 30, "JavaScript", "Skill enhance program")
print(programmer.details3())
print(programmer.details2())
print(programmer.details1())

# Multilevel inheritance
class Vehical:
    def __init__(self,brand):
        self.brand=brand

    def details1(self):
        return f" Vehical Brand is {self.brand}"

class Car(Vehical):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def details2(self):
        return f" Vehical Brand is {super().details1} and model is {self.model}"
    
class ElectronicCar(Car):
    def __init__(self,brand,model,battery_type):
        super().__init__(brand,model)
        self.battery_type=battery_type

    def details3(self):
        return f"Vehical Brand is {self.brand} and model is {self.model} and battery type is is {self.battery_type}"
    
electric_car = ElectronicCar("Tesla", "Model S", "Lithium-ion")
print(electric_car.details3())  


jose portlia -python udemy

