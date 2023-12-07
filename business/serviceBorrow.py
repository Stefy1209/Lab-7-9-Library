import ast
import random
class ServiceBorrow():
    def __init__(self, repositoryBook, repositoryClient, repositoryBorrow, repositoryFile, validatorBorrow, DTO):
        self.__repositoryBook = repositoryBook
        self.__repositoryClient = repositoryClient
        self.__repositoryBorrow = repositoryBorrow
        self.__repositoryFile = repositoryFile
        self.__validatorBorrow = validatorBorrow
        self.__DTO = DTO

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
        self.__DTO.updateNrBorrowedBooks(book)
        self.__DTO.updateNrBorrowingClients(client)

    def uploadFileBorrow(self):
        """
        updates the information from file to program
        :return: -
        """
        text = self.__repositoryFile.read().split("@")
        n = int(text[0])
        for i in range(n):
            idBorrow = text[3*i+1]
            idBook = text[3*i+2]
            idClient = text[3*i+3]
            self.createBorrowAndAddToList(idBorrow, idBook, idClient)

    def updateFileBorrow(self):
        """
        saves the information about borrows in file
        :return: -
        """
        list = self.__repositoryBorrow.getList()
        n = len(list)
        text = ""
        text = text + str(n)
        for borrow in list:
            idBorrow = borrow.getID()
            idBook = borrow.getBook().getID()
            idClient = borrow.getClient().getID()
            text = text + "@" + idBorrow + "@" + idBook + "@" + idClient
        self.__repositoryFile.write(text)

    def removeBorrow(self, idBorrow):
        """
        removes borrow by id
        :param idBorrow: string
        :return: -
        """
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
        """
        modifies the book of a borrow
        :param idBorrow: string
        :param newIdBook: string
        :return: -
        """
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
        """
        modifies the client of the borrow
        :param idBorrow: string
        :param newIdClient: string
        :return: -
        """
        self.__validatorBorrow.exist(idBorrow)
        self.__validatorBorrow.IDBorrowIsInList(idBorrow)
        self.__validatorBorrow.IsIDClient(newIdClient)
        newClient = self.__repositoryClient.searchClientByID(newIdClient)
        borrow = self.__repositoryBorrow.searchBorrowByID(idBorrow)
        oldClient = borrow.getClient()
        self.__repositoryBorrow.changeClient(borrow, newClient)

    def getBorrow(self, id):
        """
        gets borrow
        :param id: string
        :return: class
        """
        self.__validatorBorrow.exist(id)
        self.__validatorBorrow.IDBorrowIsInList(id)
        return self.__repositoryBorrow.searchBorrowByID(id)

    def generateAndAddBorrow(self):
        """
        generates borrow
        :return: -
        """
        idBorrow = str(random.randint(1, 1000000000))
        listBook = self.__repositoryBook.getList()
        book = random.choice(listBook)
        listClient = self.__repositoryClient.getList()
        client = random.choice(listClient)
        self.__validatorBorrow.BookIsAvaible(book)
        book.switchAvaible()
        borrow = self.__repositoryBorrow.createBorrow(idBorrow, book, client)
        self.__repositoryBorrow.addBorrow(borrow)
        self.__DTO.updateNrBorrowedBooks(book)
        self.__DTO.updateNrBorrowingClients(client)

    def filterByName(self):
        """
        gives a list of clients how took at least one book sorted by name
        :return: list
        """
        listBorrow = self.__repositoryBorrow.getList()
        listClient = []
        for borrow in listBorrow:
            if not borrow.getClient() in listClient:
                listClient.append(borrow.getClient())
        def name(client):
            return client.getName()
        listClient.sort(key = name)
        return listClient

    def filterByNrBook(self):
        """
        gives a list of clients how took at least one book sorted by the number of books
        :return: list
        """
        listBorrow = self.__repositoryBorrow.getList()
        listClient = []
        listNr = []
        for borrow in listBorrow:
            client = borrow.getClient()
            if not client in listClient:
                listClient.append(client)
                listNr.append(1)
            else:
                index = listClient.index(client)
                listNr[index] += 1
        for number in listNr:
            index = listNr.index(number)
            pmax = index
            max = number
            for number in listNr[pmax+1:]:
                if number > max:
                    pmax = listNr.index(number)
                    max = number
            listNr[index], listNr[pmax] = listNr[pmax], listNr[index]
            listClient[index], listClient[pmax] = listClient[pmax], listClient[index]

        return listClient