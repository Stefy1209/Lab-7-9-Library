class DTO:
    def __init__(self):
        self.__listBooks = []
        self.__listNrBorrowedBooks = []
        self.__listClients = []
        self.__listNrBorrowingClients = []

    def addBook(self, book):
        if not book in self.__listBooks:
            self.__listBooks.append(book)
            self.__listNrBorrowedBooks.append(0)

    def addClient(self, client):
        if not client in self.__listClients:
            self.__listClients.append(client)
            self.__listNrBorrowingClients.append(0)

    def updateNrBorrowedBooks(self, book):
        list = self.__listNrBorrowedBooks
        index = self.__listBooks.index(book)
        list[index] += 1

    def updateNrBorrowingClients(self, client):
        list = self.__listNrBorrowingClients
        index = self.__listClients.index(client)
        list[index] += 1

    def getListBooksSorted(self):
        listBooks = self.__listBooks
        listNr = self.__listNrBorrowedBooks
        n = len(listNr)
        for i in range(n):
            max = listNr[i]
            pmax = i
            for j in range(i, n):
                if listNr[j] > max:
                    max = listNr[j]
                    pmax = j
            listNr[i], listNr[pmax] = listNr[pmax], listNr[i]
            listBooks[i], listBooks[pmax] = listBooks[pmax], listBooks[i]

        return listBooks

    def getListClientsSorted(self):
        listBooks = self.__listClients
        listNr = self.__listNrBorrowingClients
        for i in range(n):
            max = listNr[i]
            pmax = i
            for j in range(i, n):
                if listNr[j] > max:
                    max = listNr[j]
                    pmax = j
            listNr[i], listNr[pmax] = listNr[pmax], listNr[i]
            listBooks[i], listBooks[pmax] = listBooks[pmax], listBooks[i]

        return listBooks
