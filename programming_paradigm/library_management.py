# A class representing a Book in the library
class Book:
    def _init_(self, title, author):
        if not title or not author:
            raise ValueError("Title and author cannot be empty.")
        self.title = title  
        self.author = author  
        self._is_checked_out = False 
        
        
    def check_out(self):
        if not self._is_checked_out: 
            self._is_checked_out = True 
            return True  
        raise Exception(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out: 
            self._is_checked_out = False 
            return True 
        raise Exception(f"'{self.title}' is already available.")

    def is_available(self):
        return not self._is_checked_out  

class Library:
    def _init_(self):
        self._books = [] 

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Only Book instances can be added to the library.")
        self._books.append(book) 

    def check_out_book(self, title):
        for book in self._books:  
            if book.title == title:  
                try:
                    if book.is_available():  
                        book.check_out()  
                        print(f"Checked out: '{title}'")
                    else:
                        raise Exception(f"'{title}' is already checked out.")
                except Exception as e:
                    print(e)
                return
        print(f"Book '{title}' not found in the library.")  
    def return_book(self, title):
        for book in self._books:  
            if book.title == title:  
                try:
                    if not book.is_available():  
                        book.return_book()  
                        print(f"Returned: '{title}'")
                    else:
                        raise Exception(f"'{title}' is already available.")
                except Exception as e:
                    print(e)
                return
        print(f"Book '{title}' not found in the library.")  

    def list_available_books(self):
        try:
            available_books = [book for book in self._books if book.is_available()]  
            if available_books:  
                print("Available books:")
                for book in available_books:  
                    print(f"{book.title} by {book.author}")
            else:
                raise Exception("No books are currently available.")
        except Exception as e:
            print(e)
    