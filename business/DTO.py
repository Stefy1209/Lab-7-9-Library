class DTO:
    def __init__(self):
        self.__listBooks = []
        self.__listNrBorrowedBooks = [] # for every book we will remember how many times it was borrowed
        self.__listClients = []
        self.__listNrBorrowingClients = [] # for every client we will remember how many times he/she borrowed a book
        self.__listAuthor = []
        self.__listNrBorrowedBooksAuthor = [] # for every author we will remember how many of their books were borrowed

    def addBook(self, book):
        """
        adds book, remembering how many times it was borrowed
        :param book: class
        :return: -
        """
        if not book in self.__listBooks:
            self.__listBooks.append(book)
            self.__listNrBorrowedBooks.append(0)

    def addClient(self, client):
        """
        add client remembering how many times he/she took a book
        :param client: class
        :return: -
        """
        if not client in self.__listClients:
            self.__listClients.append(client)
            self.__listNrBorrowingClients.append(0)

    def updateNrBorrowedBooks(self, book):
        """
        updates how many times the book was borrowed
        :param book: class
        :return: -
        """
        list = self.__listNrBorrowedBooks
        index = self.__listBooks.index(book)
        list[index] += 1

    def updateNrBorrowingClients(self, client):
        """
        updates how many times a client took a book
        :param client: class
        :return: -
        """
        list = self.__listNrBorrowingClients
        index = self.__listClients.index(client)
        list[index] += 1

    def getListBooksSorted(self):
        """
        sort the list of books descendent by how many times it was borrowed
        :return: list
        """
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
        """
        sort the list of clients decendent by haw many times he/she took a book
        :return:
        """
        listBooks = self.__listClients
        listNr = self.__listNrBorrowingClients
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

    def addAuthor(self, author):
        if not author in self.__listAuthor:
            self.__listAuthor.append(author)
            self.__listNrBorrowedBooksAuthor.append(0)

    def updateNrBorrowedBooksAuthor(self, author):
        list = self.__listAuthor
        index = list.index(author)
        self.__listNrBorrowedBooksAuthor[index] += 1

    def getTopAuthor(self):
        max = -1
        maxAuthor = -1 # the author with the most borrowed books
        for number in self.__listNrBorrowedBooksAuthor:
            if number > max:
                max = number
                maxAuthor = self.__listAuthor[self.__listNrBorrowedBooksAuthor.index(number)]

        if maxAuthor == -1:
            return "There is no author!"

        return maxAuthor

    def upload(self):
        print("Upload DTO de implementat!")
