# # Single or basic inheritance 

# # Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name 
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
# # Derived Class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")
# # Create an  instance of child
# child = Child("Alice")
# child.greet()         # Output : Hello my name is Alice
# child.play()            # Alice is playing

#----------------------------------------------------------------------------------------------------

# Multilevel inheritance

# Base Class
# class Grandparent:
#     def __init__(self,name):
#         self.name = name 
#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # intermediate calss 
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working.")

# # Derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# #create an instance of child
# child = Child("charlie")
# child.tell_story()
# child.work()
# child.play()    

#------------------------------------------------------------------------------------------------------

# Hierachi inheritance

# Base class

# class Paernt:
#     def __init__(self, name):
#         self.name = name 

#     def greet(self):
#         print(f"Hello my name is {self.name}")

# # Derived class1
# class Child1(Paernt):
#     def play(self):
#         print(f"{self.name} is playing")



# # Derived class2
# class Child2(Paernt):
#     def study(self):
#         print(f"{self.name} is studying")

# # Create instancer of Child1 and Child2
# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()

#----------------------------------------------------------------------------------------------------

# Multiple inheritance (Diamond problem)

# Comman Base class
class A:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        print(f"Hello from A, {self.name}")

class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

class D(B,C):
    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()

# Create an instance of D
d = D("frank")
d.greet()
              




