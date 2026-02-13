# Define a class named Book
class Book:
    
    # Constructor to initialize title and number of pages
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Method to add more pages (like adding notes or extra content)
    def add_pages(self, number):
        self.pages += number


# Create two Book objects
book1 = Book("Alice in Wonderland", 200)
book2 = Book("Harry Potter", 350)

# Add pages to book1 only
book1.add_pages(25)

# Print the number of pages
print(book1.pages)  # 225
print(book2.pages)  # 350
