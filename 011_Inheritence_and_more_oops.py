class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()

###########################################################################3

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()    #super method is used to call out the constructor(init) of parent class
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)

#########################################################################


class method_class:
    a = 1
    
    @classmethod  # @classmethod ignores the instance attribute and accepts class attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = method_class()
e.a = 45 #as @classmethod is used this is ignored

e.show()