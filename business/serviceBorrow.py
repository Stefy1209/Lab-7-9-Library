class ServiceBorrow():
    def __init__(self, repositoryBook, repositoryClient, repositoryBorrow, validatorBorrow):
        self.__repositoryBook = repositoryBook
        self.__repositoryClient = repositoryClient
        self.__repositoryBorrow = repositoryBorrow
        self.__validatorBorrow = validatorBorrow

    def createBorrowAndAddToList(self, idBorrow, idBook, idClient):
        """
        creates borrow and adds to list
        :param idBorrow: string
        :param idBook: string
        :param idClient: string
        :return: -
        """
        self.__validatorBorrow.exist(idBorrow)
        self.__validatorBorrow.exist(idBook)
        self.__validatorBorrow.exist(idClient)
        self.__validatorBorrow.IsIDBook(idBook)
        self.__validatorBorrow.IsIDClient(idClient)
        self.__validatorBorrow.IDBorrowIsUnique(idBorrow)
        book = self.__repositoryBook.searchBookByID(idBook)
        client = self.__repositoryClient.searchClientByID(idClient)
        borrow = self.__repositoryBorrow.createBorrow(idBorrow, book, client)
        self.__repositoryBorrow.addBorrow(borrow)

    def getListBorrow(self):
        """
        gets the borrow list
        :return: list
        """
        return self.__repositoryBorrow.getList()