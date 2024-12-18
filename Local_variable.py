class Person:
    age = 34    # Instance Variable
    def display(self):
        c = 23+67   # Instance Method Variable is local
        print(c)
        print("The age is", self.age)
    def getData(self):
        c = 4-2
        print(c)        # Scope of local variable is restricted within a block 
        
p = Person()
p.display()
p.getData()