# # Simple Inheritance

# # # Base class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Derived class
# class Dog(Animal):
   
        

#     def speak1(self):
#         print(f"{self.name} barks." )

# # animal = Animal("Generic animal")
# # animal.speak()  # Output : Generic animal makes a sound 

# ## create an instance of dog
# dog = Dog() # Output : Buddy Barks
# dog.speak()

# Super Keyword

class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak()  # CALL THE BASE CALSS METHOD
        print(f"{self.name} barks. he is a {self.breed}")

dog = Dog("Golden Retriver")
dog.speak()


