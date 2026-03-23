# initiate a class
class employee:
    # Special method/magic method/dunder method  constructor
    def __init__(self):
        print(id(self))
        #print("started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        #print("attributes/data have been initiated")

    def travel (self):
        print("This travel method called manually")
        print(f"Employee is now travelling to Delhi")

# Creating an object/instance of the class
sam = employee()
#sam.name = "SamKumar"
#print(sam.name)

#print(id(sam))



# shaktiman = employee()
# print(id(shaktiman))

# printing the attributes
#print(sam.id)

# calling a method
#sam.travel()
#print(type(sam))
