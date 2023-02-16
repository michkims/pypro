class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
            print(f"Hello,my name is {self.name} and my age is {self.age}")
# creating my object
person1=Person("Erick",30)
person1.say_hello()
person2=Person("Michelle",19)
person2.say_hello()
person3=Person("Brandon",32)
person3.say_hello()
# create a class called cars with the following attributes/properties
# make.mode.year them create a function that prints make,mode and year
# then create three objects
class cars:
    def __init__(self,make,mode,year):
        self.make = make
        self.mode = mode
        self.year = year
    def state(self):
            print(f"This car was built for {self.mode} and of {self.make} brand in the year {self.year}")
#creating the objects
car1=cars("Lexus","sport",2008)
car1.state()
car2=cars("Chelvoret","comfort",2011)
car2.state()
car3=cars("Lincoln","eco",2020)
car3.state()

# creating class courses
class courses:
    def __init__(self,name,period):
        self.name = name
        self.period = period
    def define(self):
            print(f"The {self.name} course is on holding for {self.period} .")
# creating objects
course1=courses("full stack development","four months")
course1.define()
course2=courses("python","three months")
course2.define()
course3=courses("android","two months")
course3.define()

