# Declare the class Student
# Python convention is to capitalize first letter in each word of class name
class Student:
    # __init__ method is like the constructor in Java
    # instance variales declared in the __init__ method are global and MUST
    # be refereced using self
    # self is like 'this' in Java
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = 10

    # __str__ is like the toString() method in Java
    # it is called when the object is printed
    # it's used for debugging purposes
    def __str__(self):
        return f"{self.lname}  :  {self.id}"

    #you don't necessarily need __str__ to return a string... see below:

    def greeting(self):
        self.enter_greet = input("enter a greeting: ")
        return f"{self.fname} says {self.enter_greet}"
    
    def take_exam(self):
        self.energy_level -= 1
        return f"{self.fname} has taken an exam"

    def get_energy_level(self):
            return f"{self.fname}'s energy level is equal to {self.energy_level}"

    #all of these returned strings, but did not use __str__