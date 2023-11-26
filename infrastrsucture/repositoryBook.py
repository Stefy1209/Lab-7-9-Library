class repositoryBook:
    """
    gestionates the list of books
    """
    def __init__(self, Book):
        """
        creates a list of books
        """
        self.__Book = Book
        self.__BookList = []

    def createBook(self, id, title, description, author):
        """
        creates a book
        :param id: string
        :param title: string
        :param description: string
        :param author: string
        :return: class
        """
        return self.__Book(id, title, description, author)

    def addBook(self, Book):
        """
        adds a book to the end of the list
        :param Book: class
        :return: -
        """
        self.__BookList.append(Book)

    def insertBook(self, Book, position):
        """
        inserts a book in the list
        :param Book: class
        :param position: integer
        :return: -
        """
        self.__BookList.insert(Book, position)

    def sizeList(self):
        """
        gets the length of the list of books
        :return: integer
        """
        return len(self.__BookList)

    def getAll(self):
        """
        gets the list of books
        :return: list
        """
        return self.__BookList

    def searchByID(self, ID):
        """
        gets the book which has the ID
        :param ID: string
        :return: class
        """
        for book in self.__BookList:
            if book.getID() == ID:
                return book

    def isInList(self, ID):
        """
        verifies if the book with the ID is in the list
        :param ID: string
        :return: bool
        """
        for book in self.__BookList:
            if book.getID() == ID:
                return True

        return False

    def isEmpty(self):
        """
        verifies if the list is empty or not
        :return: bool
        """
        return len(self.__BookList) == 0

    def removeByID(self, ID):
        """
        removes the book which has the ID
        :param ID: string
        :return: -
        """
        for book in self.__BookList:
            if book.getID() == ID:
                self.__BookList.remove(book)
    def delete(self):
        """
        empties the list
        :return: -
        """
        self.__BookList.clear()