class RepositoryBook():
    def __init__(self, book):
        self.__book = book
        self.__listBook = []

    def getList(self):
        """
        gets the book list
        :return: list
        """
        return self.__listBook

    def createBook(self, id, title, description, author):
        """
        creates a book
        :param id: string
        :param title: string
        :param description: string
        :param author: string
        :return: class
        """
        return self.__book(id, title, description, author)

    def changeTitle(self, book, newTitle):
        self.__book = book
        self.__book.setTitle(newTitle)

    def changeDescription(self, book, newDescription):
        self.__book = book
        self.__book.setDescription(newDescription)

    def changeAuthor(self, book, newAuthor):
        self.__book = book
        self.__book.setAuthor(newAuthor)

    def addBook(self, book):
        """
        add book to list
        :param book: class
        :return: -
        """
        self.__listBook.append(book)

    def searchBookByID(self, id):
        """
        search book by id
        :param id: string
        :return: class
        """
        for book in self.__listBook:
            if book.getID() == id:
                return book

    def removeBookByID(self, id):
        """
        removes book by id
        :param id: string
        :return: -
        """
        for book in self.__listBook:
            if book.getID() == id:
                self.__listBook.remove(book)

    def delete(self):
        """
        deletes the book list
        :return: -
        """
        self.__listBook.clear()