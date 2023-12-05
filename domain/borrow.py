class Borrow():
    def __init__(self, id, book, client):
        """
        creates a borrow
        :param id: string
        :param book: class
        :param client: class
        """
        self.__id = id
        self.__book = book
        self.__client = client

    def __str__(self):
        """
        the way a borrow is displayed
        :return:
        """
        return (f"ID Borrow: {self.__id}\n\n"
                f"{self.__book}\n\n"
                f"{self.__client}")

    def __eq__(self, other):
        if not isinstance(other, Borrow):
            return NotImplemented

        return other.__id == self.__id and other.__book == self.__book and other.__client == self.__client

    def getID(self):
        """
        gets the id
        :return: string
        """
        return self.__id

    def getBook(self):
        """
        gets the book
        :return: class
        """
        return self.__book

    def getClient(self):
        """
        gets the client
        :return: class
        """
        return self.__client

    def setBook(self, newBook):
        """
        changes the book with a new one
        :param newBook: class
        :return:
        """
        self.__book = newBook

    def setClient(self, newClient):
        """
        changes the client with a new one
        :param newClient: class
        :return:
        """
        self.__client = newClient