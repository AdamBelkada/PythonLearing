class Dog:
    #Class Attributes
    species = "Canis familiaris"

    def __init__ (self,name,age,breed): #instance attributes ,,dunder methods
        self.name = name
        self.age = age
        self.breed = breed
    
    # Instance method
    def description (self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
    def __str__(self):           ## dunder methods
        return f"{self.name} is {self.age} years old"
        
def main():
    buddy = Dog("Buddy",9,"Jack Russell Terrier")
    miles = Dog("Miles",4,"Dachshund")
    jack = Dog("Jack",3,"Bulldog")
    jim = Dog("Jim",3,"Bulldog")
    print (buddy.name, buddy.age)
    print (miles.name,miles.age)
    buddy.age = 6
    print (buddy.name, buddy.age)
    print (miles.description())
    print (miles.speak("woof woof"))
    print (miles)
if __name__ == "__main__":
    main()

