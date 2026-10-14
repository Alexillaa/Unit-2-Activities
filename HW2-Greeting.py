# First, we create the Class Person, in which we define the attributes that each object 
# will have and the order of them. In this case, the attributes are name, age, and city. 
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Then we create a method called greet, which will print a greeting message that includes the person's name, age, and city. 
    def greet(self):
        print(f'Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.')

# Next, we create three instances of the Person class, each with different values for the attributes.
person1 = Person("Alexa", 21, "Juarez")
person2 = Person("Jassive", 19, "Tepic")
person3 = Person("Manuel", 19, "Tepic")

# Finally, we call the greet method for each instance to display their greetings.
person1.greet()
person2.greet()
person3.greet()