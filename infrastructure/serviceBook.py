class ServiceBook():
    def __init__(self, book):
        self.__book = book
        self.__listBook = []

    def __str__(self):
        pass

    def getList(self):
        return self.__listBook

    def createBook(self, id, title, description, author):
        return self.__book(id, title, description, author)

    def addBook(self, book):
        self.__listBook.append(book)

    def searchBookByID(self, id):
        for book in self.__listBook:
            if book.getID() == id:
                return book

    def removeBookByID(self, id):
        for book in self.__listBook:
            if book.getID() == id:
                self.__listBook.remove(book)

    def delete(self):
        self.__listBook.clear()