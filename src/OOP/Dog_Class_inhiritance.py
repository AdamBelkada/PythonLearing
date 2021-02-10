class Dog:
    #Class Attributes
    species = "Canis familiaris"

    def __init__ (self,name,age): #instance attributes ,,dunder methods
        self.name = name
        self.age = age

    
    # Instance method
    def description (self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    def __str__(self):           ## dunder methods
        return f"{self.name} is {self.age} years old"

class JackRussellTerrier(Dog):
    def speak (self, sound ="Arf"):
        # return f"{self.name} says: {sound}"
        return super().speak(sound)  #to keep consistancy of the parent method

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass        
def main():
    miles = JackRussellTerrier("Miles", 4)
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    jim = Bulldog("Jim", 5)
    
    print (miles.species)
    print (buddy.name)
    print (jack)
    print (type(miles))
    print (isinstance (miles,Dog))
    print (miles.speak())
    # print (buddy.speak())

if __name__ == "__main__":
    main()

