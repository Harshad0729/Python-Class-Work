class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def bark(self):
        print("Bark Bark!")
        
    def dogInfo(self):
        print(self.name,"is",str(self.age),"years old")
d = Dog("puppy",5)

d.dogInfo()
d.bark()