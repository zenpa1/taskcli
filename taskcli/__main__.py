import sys
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    print("In Main")
    args = sys.argv[1:]
    print("Count of args :: {}".format(len(args)))  # Counts number of args
    for arg in args:
        print("Passed Argument :: {}".format(arg))  # Loop to separate args

    my_function("Hello World!")  # Placeholder function

    my_object = MyClass("Thomas")  # Placeholder class
    my_object.say_name()

if __name__ == "__main__":
    main()