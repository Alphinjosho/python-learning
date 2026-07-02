class Book:
    def __init__ (self,title,author):
        self.title=title
        self.author=author

book1 =Book("Atomic Habits","James Clear")

print("Title:",book1.title)
print("Author:",book1.author)