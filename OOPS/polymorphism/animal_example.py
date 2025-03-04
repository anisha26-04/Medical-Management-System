class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("cat meows.")

a1= Animal()
a1.speak()  #calls speak method from animal

d1=Dog()
d1.speak()  #calls speak method from animal

c1=Cat()
c1.speak()   #calls speak method from animal

# in this code speak method +is executed with diffrently here behaviour of speak() changes depending on the object.
# now suppose you have a list of animals and you want each animal to make its unique sound.with polymorphism you dont need 
# to write seperate code for each animal  
animals=[Dog(),Cat(),Animal()]
for a in animals:
    a.speak()