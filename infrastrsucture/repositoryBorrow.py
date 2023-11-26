class repositoryBorrow:
    """
    gestionates the list of borrows
    """
    def __init__(self, Borrow):
        """
        creates the list of borrows
        """
        self.__repositoryBook = repositoryBook()
        self.__repositoryClient = repositoryClient()
        self.__Borrow = Borrow
        self.__BorrowList = []

    def createBorrow(self, ID, IDBook, IDClient):
        """
        creates a borrow
        :param ID: string
        :param IDBook: string
        :param IDClient: string
        :return: class
        """
        book = self.__repositoryBook.searchByID(IDBook)
        client = self.__repositoryClient.searchByID(IDClient)
        borrow = self.__Borrow(ID, book, client)

        return borrow

    def addBorrow(self, Borrow):
        """
        adds a borrow at the end of the list
        :param Borrow: class
        :return: -
        """
        self.__BorrowList.append(Borrow)

    def insertBorrow(self, Borrow, position):
        """
        inserts a borrow in the list
        :param Borrow: class
        :param position: integer
        :return: -
        """
        self.__BorrowList.insert(Borrow, position)

    def sizeList(self):
        """
        gets the size of the list
        :return: integer
        """
        return len(self.__BorrowList)

    def getAll(self):
        """
        gest the list
        :return: list
        """
        return self.__BorrowList

    def searchByID(self, ID):
        """
        gets the borrow with the ID
        :param ID: string
        :return: class
        """
        for borrow in self.__BorrowList:
            if borrow.getID() == ID:
                return borrow

    def isInList(self, ID):
        """
        verifies if the borrow with the ID is in the list
        :param ID: string
        :return: bool
        """
        for borrow in self.__BorrowList:
            if borrow.getID() == ID:
                return True

        return False

    def isEmpty(self):
        """
        verifies if the list is empty
        :return: bool
        """
        return len(self.__BorrowList) == 0

    def removeByID(self, ID):
        """
        removes the borrow with the ID
        :param ID: string
        :return: -
        """
        for borrow in self.__BorrowList:
            if borrow.getID() == ID:
                self.__BorrowList.remove(borrow)

    def delete(self):
        """
        deletes the list
        :return: -
        """
        self.__BorrowList.clear()