# make the most simple class possible


class SimpleClass:
    def __init__(self):
        print("SimpleClass instance created")
    


# create an instance of your SimpleClass and print it out
simpleClassObj = SimpleClass()
print(simpleClassObj)

# now add some functionality to your simple class


class LessSimpleClass:
    # add one class attribute
    def __init__(self):
        self.class_attribute = "I am a class attribute"
        print("LessSimpleClass instance created")
    # add a class method
    def class_method(self):
        print("This is a class method")


# print out your class attribute both from an instance of the class and through the class directly
lessSimpleClassObj = LessSimpleClass()
print(lessSimpleClassObj.class_attribute)
# run the method - both directly from the class and through an instance.
lessSimpleClassObj.class_method()

