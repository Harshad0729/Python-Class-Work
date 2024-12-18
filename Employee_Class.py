class Employee:
    # constructor is special member function which initializes class variable
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of employee is {self.name} which {self.id} age")
    
class Programmer(Employee):
    def displayLanguages(self):
        print("Having knowledge about python")
        
obj = Programmer("Hari", 45)
obj.displayLanguages()
obj.showDetails()

'''
e = Employee("Hari", 45)
e.showDetails()
el = Employee("Ram", 67)
el.showDetails()
'''