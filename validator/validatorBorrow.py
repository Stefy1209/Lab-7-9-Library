class ValidatorBorrow():
    def __init__(self, repositoryBorrow, validatorBook, validatorClient):
        self.__repositoryBorrow = repositoryBorrow
        self.__validatorBook = validatorBook
        self.__validatorClient = validatorClient

    def exist(self, thing):
        if thing == "":
            raise SyntaxError("Something is missing!")

    def IsIDBook(self, idBook):
        self.__validatorBook.IDIsInList(idBook)

    def IsIDClient(self, idClient):
        self.__validatorClient.IDIsInList(idClient)

    def IDBorrowIsUnique(self, idBorrow):
        list = self.__repositoryBorrow.getList()
        for borrow in list:
            if idBorrow == borrow.getID():
                raise SyntaxError("ID borrow is not unique!")