# First, we define a class called Engine that has a method called start. 
# This method prints a message indicating that the engine has started.
class Engine:
    def start(self):
        print("Engine started")

# Next, we define a class called Car that has an attribute called engine,
# which is an instance of the Engine class.
class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

# Finally, we create an instance of the Car class and call the start_car method
# to demonstrate that the Car class has access to the start method of the Engine class.
my_car = Car()
my_car.start_car()