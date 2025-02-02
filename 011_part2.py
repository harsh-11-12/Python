#property decorator

class Employee:

    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harsh Pant"
print(e.fname, e.lname)

e.show()

#operator overloading

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): #if we dont define "+" by overloading it will not recognise it
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)

# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)
#__str__() # used to set what gets displayed upon calling str(obj)
#__len__() #used to set what gets displayed upon calling.__len__() or len(obj)