class ValidatorBook():
    def __init__(self, repositoryBook):
        self.__repositoryBook = repositoryBook

    def isID(self, id):
        """
        verifies if is an id
        :param id: string
        :return: -
        """
        if id == "":
            raise SyntaxError("There is no ID!")

    def IDIsUnique(self, id):
        """
        verifies if id is unique
        :param id: string
        :return:
        """
        list = self.__repositoryBook.getList()
        for book in list:
            if id == book.getID():
                raise SyntaxError("ID is not unique!")

    def IDIsInList(self, id):
        """
        verifies if id is in list
        :param id: string
        :return:
        """
        list = self.__repositoryBook.getList()
        for book in list:
            if id == book.getID():
                return
        raise SyntaxError("There is no book with this ID!")

    def bookIsAvaible(self, book):
        """
        verifies if book is avaible
        :param book: class
        :return:
        """
        if book.getAvaible() == False:
            raise SyntaxError("Book is not avaible!")