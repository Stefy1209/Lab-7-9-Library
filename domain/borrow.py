class Borrow:
    """
    borrow is class which makes the link between a client and a book and tells that the client "A" borrowed the book "B"
    """
    def __init__(self, id, Book, Client):
        """
        creates a rent
        :param id: string
        :param Book: class(id, title, description, author)
        :param Client: class(id, name, CNP)
        """
        self.__id = id
        self.__book = Book
        self.__client = Client

    def __str__(self):
        """
        the way a borrow is diplayed
        :return:
        """
        return (f"{self.__book}\n"
                f"{self.__client}")

    def getID(self):
        """
        gets the id of a rent
        :return: string
        """
        return self.__id

    def getBook(self):
        """
        gets the book of a rent
        :return: class(id, title, description, author)
        """
        return self.__book

    def getClient(self):
        """
        gets the client of a rent
        :return: class(id, name, CNP)
        """
        return self.__client

    def setBook(self, newBook):
        """
        changes the book of a rent
        :param newBook: class(id, title, description, author)
        :return: -
        """
        self.__book = newBook

    def setClient(self, newClient):
        """
        changes the client of a rent
        :param newClient: class(id, name, CNP)
        :return: -
        """
        self.__client = newClient