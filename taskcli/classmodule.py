# Shows how a class can be imported from a module in the same package

class MyClass():
    def __init__(self, name):
        self.name = name
    
    def say_name(self):
        print("Name is {}".format(self.name))