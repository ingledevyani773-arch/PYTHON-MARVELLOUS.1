class BookStore:
    # Class variable tracking total books
    NoOfBooks = 0

    def __init__(self, Name, Author):
        # Initializing instance variables
        self.Name = Name
        self.Author = Author
        
        # Incrementing the class variable upon new object creation
        BookStore.NoOfBooks += 1

    def Display(self):
        # Displaying the book details matching the required output format
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


# --- Example Usage ---

# Creating the first object
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()
# Output: Linux System Programming by Robert Love. No of books: 1

# Creating the second object
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()
# Output: C Programming by Dennis Ritchie. No of books: 2