#   multilevel inheritance program 
class Animal:
    def legs(self):
        print("I have four legs")
        
    def fur(self):
        print("My body is covered with fur")
        
class Dog(Animal):
    def bark(self):
        print("The dog barks")
        
class Cat(Dog):
    def purr(self):
        print("The cat purrs")
        
        
c=Cat()
c.purr()
