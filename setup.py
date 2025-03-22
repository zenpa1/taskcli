from setuptools import setup
setup(
    name = "taskcli",
    version = '0.1.0',
    packages = ["taskcli"],  # all included packages

    # The runnable will be called taskcli
    # When executed, it will run the main function in the __main__
    # module in the taskcli package
    entry_points = {
        "console_scripts": [
            "taskcli = taskcli.__main__:main"
        ]
    }
)