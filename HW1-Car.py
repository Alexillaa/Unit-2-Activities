# First, we create the Class Car, in which we define the attributes that each object 
# will have and the order of them. In this case, the attributes are brand, model, and color.
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

# Then we create a method called display_car_info, which will print the car's brand, model, and color.
    def display_car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")

# Next, we create two instances of the Car class, each with different values for the attributes.
car1 = Car("Jeep", "Wrangler","Pink")
print("Car 1 Information:")
print(f"Brand: {car1.brand}\nModel: {car1.model}\nColor: {car1.color}")

# Finally, we create a second instance of the Car class and display its information. Instead of calling the 
# display_car_info method, we directly access the attributes of the car2 object to print its information.
car2 = Car("Mercedez", "AMG GLE 53 Coupe", "Purple")
print("\nCar 2 Information:")
print(f"Brand: {car2.brand}\nModel: {car2.model}\nColor: {car2.color}")
