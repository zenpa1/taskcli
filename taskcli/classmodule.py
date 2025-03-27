# Shows how a class can be imported from a module in the same package
import os

# class MyClass:
#     def __init__(self, name):
#         self.name = name
    
#     def say_name(self):
#         print("Name is {}".format(self.name))

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def get_id(self):
        return self.id
    
    def set_id(self, value):
        self.id = value

    def get_description(self):
        return self.description
    
    def set_description(self, value):
        self.description = value

    def get_status(self):
        return self.status
    
    def set_status(self, value):
        self.status = value

    def get_createdAt(self):
        return self.createdAt
    
    def set_createdAt(self, value):
        self.createdAt = value

    def get_updatedAt(self):
        return self.updatedAt
    
    def set_updatedAt(self, value):
        self.updatedAt = value