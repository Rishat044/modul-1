class Book:
    def __init__(self, title, author, copies):
        self.title = title          
        self.author = author       
        self.copies = copies       

    def borrow(self):

        if self.copies > 0:
            self.copies -= 1     
            return True            
        return False           

    def return_book(self):

        self.copies += 1

#----------------------------------------------------
class Reader:
    def __init__(self, name, reader_id):
        self.name = name 
        self.reader_id = reader_id 

#--------------------------------------------------

class Library:
    def __init__(self):
        self.books = {}        
        self.readers = {}   

    def add_book(self, book):
        self.books[book.title] = book

    def register_reader(self, reader):
        self.readers[reader.reader_id] = reader

    def borrow_book(self, reader_id, book_title):
        if reader_id in self.readers and book_title in self.books:
            book = self.books[book_title]
            if book.borrow():
                print(f"Читатель {reader_id} взял книгу '{book_title}'.")
            else:
                print(f"Книги '{book_title}' нет в наличии.")
        else:
            print("Читатель или книга не найдены.")

    def return_book(self, reader_id, book_title):
        if reader_id in self.readers and book_title in self.books:
            book = self.books[book_title]
            book.return_book()
            print(f"Читатель {reader_id} вернул книгу '{book_title}'.")


#--------------------------------------------------------------------------------------

library = Library()

book1 = Book("python", "Sasha", 2) 
library.add_book(book1)

reader1 = Reader("Сергей", 1)  
library.register_reader(reader1)

#--------------------------------------------------------------------------------------
library.borrow_book(1, "python") 
library.return_book(1, "python")  