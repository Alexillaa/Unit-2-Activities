# First, we define a class called Book that has the attributes 'title' and 'num_pages'.
class Book:
    def __init__(self, title, num_pages):
        self.title = title
        self.num_pages = num_pages

# Next, we define the dunder methods __str__ and __len__ for the Book class.
# By usinng '_-len__', we can return the number of pages in the book.
    def __str__(self):
        return f"Book: {self.title}, Pages: {self.num_pages}"

    def __len__(self):
        return self.num_pages

# Finallu, we create an instance of the Book class and print the book's information.
Book1 = Book("The Oddysey", 587)
print(Book1)          # Uses __str__
print(len(Book1))     # Uses __len__