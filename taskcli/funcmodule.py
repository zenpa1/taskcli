# Shows how a function can be imported and invoked

# def my_function(text_to_display):
#     print("Text from my function :: {}".format(text_to_display))

def printTask(task):
        print("ID:", task.id,
              "\nDescription:", task.description,
              "\nStatus:", task.status,
              "\nCreated:", task.createdAt,
              "\nModified:", task.updatedAt)