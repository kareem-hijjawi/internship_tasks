
class Book:
    

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self._is_borrowed = False

    def is_available(self):
       
        return not self._is_borrowed

    def borrow(self):
       
        if self._is_borrowed:
            raise ValueError(f"The book '{self.title}' is already borrowed.")
        self._is_borrowed = True

    def return_book(self):
       
        if not self._is_borrowed:
            raise ValueError(f"The book '{self.title}' was not borrowed.")
        self._is_borrowed = False

    def get_info(self):
        
        return f"Title: {self.title}, Author: {self.author}, ID: {self.book_id}"


class Fiction(Book):
   

    def __init__(self, title, author, book_id, genre):
        super().__init__(title, author, book_id)
        self.genre = genre

    def get_info(self):
      
        return (
            f"Fiction - Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ID: {self.book_id}"
        )


class NonFiction(Book):
   

    def __init__(self, title, author, book_id, subject):
        super().__init__(title, author, book_id)
        self.subject = subject

    def get_info(self):
       
        return (
            f"Non-Fiction - Title: {self.title}, Author: {self.author}, Subject: {self.subject}, ID: {self.book_id}"
        )


class Library:
    

    def __init__(self):
        self.books = {}

    def add_book(self, book):
       
        if book.book_id in self.books:
            raise ValueError(f"Book ID {book.book_id} already exists.")
        self.books[book.book_id] = book

    def display_books(self):
       
        if not self.books:
            return "The library has no books."
        return "\n".join(book.get_info() for book in self.books.values())

    def find_book(self, book_id):
      
        return self.books.get(book_id, None)


class User:
    

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book_id):
        
        book = library.find_book(book_id)
        if not book:
            raise ValueError(f"Book ID {book_id} not found.")
        book.borrow()
        self.borrowed_books.append(book)
        return f"{self.name} borrowed '{book.title}'."

    def return_book(self, library, book_id):
       
        book = library.find_book(book_id)
        if not book:
            raise ValueError(f"Book ID {book_id} not found.")
        if book not in self.borrowed_books:
            raise ValueError(f"{self.name} has not borrowed the book '{book.title}'.")
        book.return_book()
        self.borrowed_books.remove(book)
        return f"{self.name} returned '{book.title}'."



if __name__ == "__main__":
    library = Library()

    library.add_book(Fiction("The Great Gatsby", "F. Scott Fitzgerald", 1, "Classic"))
    library.add_book(NonFiction("Sapiens", "Yuval Noah Harari", 2, "History"))

   
    print("Library Books:")
    print(library.display_books())

    
    user = User("Alice")
    print("\nBorrowing Books:")
    print(user.borrow_book(library, 1))
    print(user.borrow_book(library, 2))

    print("\nReturning Books:")
    print(user.return_book(library, 1))
    print(user.return_book(library, 2))
