class Calculator:
    def __init__(self, n):
        self.n = n 
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()

####################################################################

class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute


from random import randint

####################################################################

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")