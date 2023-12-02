class UI:
    def __init__(self, serviceBook, serviceClient, serviceBorrow):
        self.__serviceBook = serviceBook
        self.__serviceClient = serviceClient
        self.__serviceBorrow = serviceBorrow
        self.__finished = False
        self.__parameters = []
        self.__listActions = {"add": self.UIAdd, "show": self.UIShow, "exit": self.UIExit}

    def UIAdd(self):
        listObject = {"book": self.UIAddBook, "client": self.UIAddClient, "borrow": self.UIAddBorrow}
        listObject[self.__parameters[0]]()

    def UIAddBook(self):
        print("")
        id = input("ID: ")
        title = input("Title: ")
        description = input("Description: ")
        author = input("Author: ")
        print("")
        self.__serviceBook.createBookAndAddToList(id, title, description, author)

    def UIAddClient(self):
        print("")
        id = input("ID: ")
        name = input("Name: ")
        cnp = input("CNP: ")
        print("")
        self.__serviceClient.createClientAndAddToList(id, name, cnp)

    def UIAddBorrow(self):
        print("")
        idBorrow = input("ID Borrow: ")
        idBook = input("ID Book: ")
        idClient = input("ID Client: ")
        print("")
        self.__serviceBorrow.createBorrowAndAddToList(idBorrow, idBook, idClient)

    def UIShow(self):
        listObject = {"book": self.UIShowBook, "books": self.UIShowBook, "client": self.UIShowClient, "clients": self.UIShowClient, "borrow": self.UIShowBorrow, "borrows": self.UIShowBorrow}
        listObject[self.__parameters[0]]()

    def UIShowBook(self):
        list = self.__serviceBook.getListBook()
        for book in list:
            print("")
            print(book)
        print("")

    def UIShowClient(self):
        list = self.__serviceClient.getListClient()
        for client in list:
            print("")
            print(client)
        print("")

    def UIShowBorrow(self):
        list = self.__serviceBorrow.getListBorrow()
        for borrow in list:
            print("")
            print(borrow)
        print("")

    def UIExit(self):
        self.__finished = True

    def runUI(self):
        while not self.__finished:
            command = input(">>> ").strip().lower().split()
            try:
                action = command[0].strip()
                self.__parameters = command[1:]
                self.__listActions[action]()
            except SyntaxError as se:
                print(se)
            except IndexError as ie:
                print("There is no action!")
            except KeyError as ke:
                print(str(ke) + " is not a valid action!")