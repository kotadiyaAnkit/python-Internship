class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "Available"  # fixed spelling
        
    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is already borrowed.')
        
    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" was not borrowed.')
            
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Status: {self.status}")
        

# Test the class
book = Book(1246, "Available", 2011)
book.display()
print()

book.borrow()
book.display()
print()

book.borrow()  # Try borrowing again

book.return_book()
book.display()
print()

book.return_book()  # Try returning again
