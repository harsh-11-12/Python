class employee:             #class
    language="Python"       #class attribute
    salary=2200110

    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print("This init funcion is a dunder function, which is automatically called as soon as an object is created")

    def getinfo(self):
        print(f"Name is :{self.name}\nLanguage is :{self.language}\nSalary is :{self.salary}")

    def unstat(self):
        print("This function requires parameter")

    @staticmethod
    def stat():
        print("This is a static function, hence no need of parameter")



emp1=employee("Harsh","Javascript",109000)             #object
emp1.name="Harsh Pant"           #object attribute or instance attribute
# print(emp1.name,emp1.language,emp1.salary)
emp1.language="Java"        #instance attribute overwrites class attribute under object
# print(emp1.language)

emp1.getinfo()  #same as "employee.getinfo(emp1)"
emp1.unstat()   #same as "employee.getinfo(emp1)"
emp1.stat()

emp2=employee("Harsh1","php",125560)
emp2.getinfo()