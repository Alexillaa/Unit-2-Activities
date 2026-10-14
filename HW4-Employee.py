# First, we create the Class Employee, in which we define the attributes that each object
# will have and the order of them. 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Then we create a method called show_info, which will print the employee's name and salary.
    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Next, we create a subclass called Manager that inherits from the Employee class. 
# In the Manager class, we define an additional attribute called department.
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

# Then, we override the show_info method to include the department information.
    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")

# Finally, we create instances of the Employee and Manager classes and call
# their show_info methods to display their information.
Employee1 = Employee("Alice", 50000)
Employee1.show_info()

Manager1 = Manager("John", 200000, "Engineering")
Manager1.show_info()