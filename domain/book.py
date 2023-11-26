class Book():
    def __init__(self, id, title, description, author):
        """
        creates book
        :param id: string
        :param title: string
        :param description: string
        :param author: string
        """
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__avaible = True

    def __str__(self):
        """
        the way a book is displayed
        :return:
        """
        return (f"ID: {self.__id}\n"
                f"Title: {self.__title}\n"
                f"Description: {self.__description}\n"
                f"Author: {self.__author}\n"
                f"Avaible: {self.__avaible}")

    def getID(self):
        """
        gets the ID
        :return: string
        """
        return self.__id

    def getTitle(self):
        """
        gets the title
        :return: string
        """
        return self.__title

    def getDescription(self):
        """
        gets the description
        :return: string
        """
        return self.__description

    def getAuthor(self):
        """
        gets the author
        :return: string
        """
        return self.__author

    def getAvaible(self):
        """
        gets the avaible
        :return: bool
        """
        return self.__avaible

    def setTitle(self, newtitle):
        """
        changes the title with the new one
        :param newtitle: string
        :return:
        """
        self.__title = newtitle

    def setDescription(self, newDescription):
        """
        changes the description with the new one
        :param newDescription: string
        :return:
        """
        self.__description = newDescription

    def setAuthor(self, newAuthor):
        """
        changes the description with the new one
        :param newAuthor: string
        :return:
        """
        self.__author = newAuthor

    def switchAvaible(self):
        """
        book avaible => book unavaible
        book unavaible => book avaible
        :return:
        """
        self.__avaible = self.__avaible ^ True