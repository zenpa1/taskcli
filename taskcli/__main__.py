import sys
from .classmodule import Task
from .funcmodule import *

# def main():
#     print("In Main")
#     args = sys.argv[1:]
#     print("Count of args :: {}".format(len(args)))  # Counts number of args
#     for arg in args:
#         print("Passed Argument :: {}".format(arg))  # Loop to separate args

#     my_function("Hello World!")  # Placeholder function

#     my_object = MyClass("Thomas")  # Placeholder class
#     my_object.say_name()

    # for arg in args:
    #     print("Argument ", ctr, " :: {}".format(arg))
    #     ctr += 1

def main():
    args = sys.argv[1:]
    command = args[0]
    if command == "add":
        task = addTask()
    else:
        print("Enter a valid command.")   

    printTask(task)

if __name__ == "__main__":
    main()