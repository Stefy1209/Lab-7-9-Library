import random


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
        self.__validatorBorrow.BookIsAvaible(book)
        client = self.__repositoryClient.searchClientByID(idClient)
        borrow = self.__repositoryBorrow.createBorrow(idBorrow, book, client)
        self.__repositoryBorrow.addBorrow(borrow)
        book.switchAvaible()

    def removeBorrow(self, idBorrow):
        self.__validatorBorrow.exist(idBorrow)
        self.__validatorBorrow.IDBorrowIsInList(idBorrow)
        borrow = self.__repositoryBorrow.searchBorrowByID(idBorrow)
        book = borrow.getBook()
        book.switchAvaible()
        self.__repositoryBorrow.removeBorrowByID(idBorrow)

    def getListBorrow(self):
        """
        gets the borrow list
        :return: list
        """
        return self.__repositoryBorrow.getList()

    def modifyBook(self, idBorrow, newIdBook):
        self.__validatorBorrow.exist(idBorrow)
        self.__validatorBorrow.IDBorrowIsInList(idBorrow)
        self.__validatorBorrow.IsIDBook(newIdBook)
        newBook = self.__repositoryBook.searchBookByID(newIdBook)
        borrow = self.__repositoryBorrow.searchBorrowByID(idBorrow)
        oldBook = borrow.getBook()
        self.__repositoryBorrow.changeBook(borrow, newBook)
        newBook.switchAvaible()
        oldBook.switchAvaible()

    def modifyClient(self, idBorrow, newIdClient):
        self.__validatorBorrow.exist(idBorrow)
        self.__validatorBorrow.IDBorrowIsInList(idBorrow)
        self.__validatorBorrow.IsIDClient(newIdClient)
        newClient = self.__repositoryClient.searchClientByID(newIdClient)
        borrow = self.__repositoryBorrow.searchBorrowByID(idBorrow)
        oldClient = borrow.getClient()
        self.__repositoryBorrow.changeClient(borrow, newClient)

    def getBorrow(self, id):
        self.__validatorBorrow.exist(id)
        self.__validatorBorrow.IDBorrowIsInList(id)
        return self.__repositoryBorrow.searchBorrowByID(id)

    def generateAndAddBorrow(self):
        idBorrow = random.randint(1, 1000000000)
        listBook = self.__repositoryBook.getList()
        book = random.choice(listBook)
        listClient = self.__repositoryClient.getList()
        client = random.choice(listClient)
        self.__validatorBorrow.BookIsAvaible(book)
        book.switchAvaible()
        borrow = self.__repositoryBorrow.createBorrow(idBorrow, book, client)
        self.__repositoryBorrow.addBorrow(borrow)