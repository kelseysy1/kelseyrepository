class Dog:
    # __init__ method is like the constructor in Java
    # instance variales declared in the __init__ method are global and MUST
    # be refereced using self
    # self is like 'this' in Java
    def __init__(self, name, trick, breed, hungry):
        self.name = name
        self.trick = trick
        self.breed = breed
        self.hungry = True

    # __str__ is like the toString() method in Java
    # it is called when the object is printed
    # it's used for debugging purposes
    def __str__(self):
        return f"{self.name}  :  {self.breed}"


    def speak(self):
        self.speaks = "Woof"
        return self.speaks
    

    def feed(self):
        if self.hungry == False:
            return f"{self.name} is no longer hungry"
        else:
            return f"{self.name} is no longer hungry"
    


    def change_trick(self):
        self.trick = input("enter the new trick: ")
        return f"{self.name} learned a new trick!"

    def get_name(self):
        return f"{self.name} is the name of this dog"

    def get_breed(self):
        return f"{self.breed} is the breed of this dog"

    def get_trick(self):
        return f"{self.name} can do this trick: {self.trick}"

    def isHungry(self):
        return self.hungry
