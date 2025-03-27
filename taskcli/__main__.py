import sys
from .classmodule import Task
from .funcmodule import printTask
from datetime import datetime

# def main():
#     print("In Main")
#     args = sys.argv[1:]
#     print("Count of args :: {}".format(len(args)))  # Counts number of args
#     for arg in args:
#         print("Passed Argument :: {}".format(arg))  # Loop to separate args

#     my_function("Hello World!")  # Placeholder function

#     my_object = MyClass("Thomas")  # Placeholder class
#     my_object.say_name()

def main():
    ctr = 1
    args = sys.argv[1:]
    # for arg in args:
    #     print("Argument ", ctr, " :: {}".format(arg))
    #     ctr += 1

    userId = args[0]
    userDescription = args[1]
    userStatus = args[2]
    userCreatedAt = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    userUpdatedAt = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    task = Task(userId, userDescription, userStatus, userCreatedAt, userUpdatedAt)
    printTask(task)

if __name__ == "__main__":
    main()