class Book:
    author = ""
    title = ""

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(self.title, ", written by", self.author)


HP = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
HP.display()

Romance = Book("Walter Scott", "Ivanhoe: A Romance")
Romance.display()
