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
        self.__available = True

    def __str__(self):
        """
        the way a book is displayed
        :return:
        """
        return (f"ID: {self.__id}\n"
                f"Title: {self.__title}\n"
                f"Description: {self.__description}\n"
                f"Author: {self.__author}\n"
                f"Availability: {self.__available}")

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

    def getAvailable(self):
        """
        gets the availability of a book
        :return: bool
        """
        return self.__available

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

    def setAvailable(self, newAvailable):
        """
        chnages the availability of a book
        :param newAvailable: bool
        :return: -
        """
        self.__available = newAvailable