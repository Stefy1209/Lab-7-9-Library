class ValidatorBorrow():
    def __init__(self, repositoryBorrow, validatorBook, validatorClient):
        self.__repositoryBorrow = repositoryBorrow
        self.__validatorBook = validatorBook
        self.__validatorClient = validatorClient

    def exist(self, thing):
        """
        verifies if it is not empty
        :param thing: string
        :return:
        """
        if thing == "":
            raise SyntaxError("Something is missing!")

    def IsIDBook(self, idBook):
        """
        verifies if id coresponds with a book
        :param idBook:
        :return:
        """
        self.__validatorBook.IDIsInList(idBook)

    def IsIDClient(self, idClient):
        """
        verifies if id coresponds with a client
        :param idClient: string
        :return:
        """
        self.__validatorClient.IDIsInList(idClient)

    def IDBorrowIsUnique(self, idBorrow):
        list = self.__repositoryBorrow.getList()
        for borrow in list:
            if idBorrow == borrow.getID():
                raise SyntaxError("ID borrow is not unique!")

    def IDBorrowIsInList(self, idBorrow):
        list = self.__repositoryBorrow.getList()
        for borrow in list:
            if idBorrow == borrow.getID():
                return
        raise SyntaxError("There is no borrow with this ID!")

    def BookIsAvaible(self, book):
        if book.getAvaible() == False:
            raise SyntaxError("Book is not avaible!")