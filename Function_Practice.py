class Faculty:
    def putData(self):
        self.id = int(input("Enter your employee id: "))
        self.name = input("Enter your name: ")
        self.salary = float(input("Enter your salary: "))
        
    def display(self):
        print("Faculty id:", self.id)
        print("Faculty name:", self.name)
        print("Faculty salary:", self.salary)
        
a = Faculty()
a.putData()
a.display() 