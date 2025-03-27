# Shows how a function can be imported and invoked

# def my_function(text_to_display):
#     print("Text from my function :: {}".format(text_to_display))

import sys
from .classmodule import Task
from datetime import datetime

idCount = 0

def addTask():
      args = sys.argv[1:]
      userId = idCount + 1
      userDescription = args[1]
      userStatus = args[2]
      userCreatedAt = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
      userUpdatedAt = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
      task = Task(userId, userDescription, userStatus, userCreatedAt, userUpdatedAt)
      print("Adding task...")
      return task

def printTask(task):
      print("ID:", task.id,
            "\nDescription:", task.description,
            "\nStatus:", task.status,
            "\nCreated:", task.createdAt,
            "\nModified:", task.updatedAt)