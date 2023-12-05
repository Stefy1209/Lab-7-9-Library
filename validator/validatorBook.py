class ValidatorBook():
    def __init__(self, repositoryBook):
        self.__repositoryBook = repositoryBook

    def isID(self, id):
        if id == "":
            raise SyntaxError("There is no ID!")

    def IDIsUnique(self, id):
        list = self.__repositoryBook.getList()
        for book in list:
            if id == book.getID():
                raise SyntaxError("ID is not unique!")

    def IDIsInList(self, id):
        list = self.__repositoryBook.getList()
        for book in list:
            if id == book.getID():
                return
        raise SyntaxError("There is no book with this ID!")

    def bookIsAvaible(self, book):
        if book.getAvaible() == False:
            raise SyntaxError("Book is not avaible!")