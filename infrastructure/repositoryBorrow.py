class RepositoryBorrow():
    def __init__(self, Borrow):
        """
        :param Borrow: class
        """
        self.__Borrow = Borrow
        self.__listBorrow = []

    def getList(self):
        """
        gets list
        :return: list
        """
        return self.__listBorrow

    def createBorrow(self, id, book, client):
        """
        creates borrow
        :param id: string
        :param book: class
        :param client: class
        :return: class
        """
        return self.__Borrow(id, book, client)

    def addBorrow(self, borrow):
        """
        adds borrow
        :param borrow: class
        :return: -
        """
        self.__listBorrow.append(borrow)

    def searchBorrowByID(self, id):
        """
        search borrow by id
        :param id: string
        :return: class
        """
        for borrow in self.__listBorrow:
            if borrow.getID() == id:
                return borrow

    def removeBorrowByID(self, id):
        """
        removes borrow by id
        :param id: string
        :return: -
        """
        for borrow in self.__listBorrow:
            if borrow.getID() == id:
                self.__listBorrow.remove(borrow)

    def delete(self):
        """
        deletes list
        :return: -
        """
        self.__listBorrow.clear()

    def changeBook(self, borrow, newBook):
        borrow.setBook(newBook)

    def changeClient(self, borrow, newClient):
        borrow.setClient(newClient)