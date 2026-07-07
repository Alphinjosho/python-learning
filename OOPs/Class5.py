class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
         print("Book:",self.title,"Author:",self.author)

book1 = Book("Atomic Habits", "James Clear")
book2 = Book("Clean Code", "Robert Martin")

book1.show_book()
book2.show_book()   