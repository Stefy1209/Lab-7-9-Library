class Book:
    """
    book is an object which stores the ID, Title, Description and Author of a book
    """
    def __init__(self, id, title, description, author):
        """
        creates a book
        :param id: string
        :param title: string
        :param description: string
        :param author: string
        """
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author

    def getID(self):
        """
        gets the ID
        :return: string
        """
        return self.__id

    def getTitle(self):
        """
        gets title
        :return: string
        """
        return self.__title

    def getDescription(self):
        """
        gets description
        :return: string
        """
        return self.__description

    def getAuthor(self):
        """
        gets author
        :return: string
        """
        return self.__author

    def setTitle(self, newTitle):
        """
        changes the title of a book
        :param newTitle: string
        :return: -
        """
        self.__title = newTitle

    def setDescription(self, newDescription):
        """
        changes the description of a book
        :param newDescription: string
        :return: -
        """
        self.__description = newDescription

    def setAuthor(self, newAuthor):
        """
        changes the author of a book
        :param newAuthor: string
        :return: -
        """
        self.__author = newAuthor

class Client:
    """
    client is an object which stores an ID, Name and CNP
    """
    def __init__(self, id, name, cnp):
        """
        creates a client
        :param id: string
        :param name: string
        :param cnp: string
        """
        self.__id = id
        self.__name = name
        self.__cnp = cnp

    def getID(self):
        """
        gets the ID
        :return: string
        """
        return self.__id

    def getName(self):
        """
        gets the name
        :return: string
        """
        return self.__name

    def getCNP(self):
        """
        gets the CNP
        :return: string
        """
        return self.__cnp

    def setName(self, newName):
        """
        changes the name of a client
        :param newName: string
        :return: -
        """
        self.__name = newName

class Rent:
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
