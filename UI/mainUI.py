class UI:
    def __init__(self, serviceBook, serviceClient, serviceBorrow, DTO):
        self.__serviceBook = serviceBook
        self.__serviceClient = serviceClient
        self.__serviceBorrow = serviceBorrow
        self.__DTO = DTO
        self.__finished = False
        self.__parameters = []
        self.__listActions = {"add": self.UIAdd,
                              "remove": self.UIRemove,
                              "modify": self.UIModify,
                              "search": self.UISearch,
                              "generate": self.UIGenerate,
                              "sort": self.UISort,
                              "top": self.UITop,
                              "show": self.UIShow,
                              "delete": self.UIDelete,
                              "exit": self.UIExit}

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

    def UIUpload(self):
        self.__serviceBook.uploadFileBook()
        self.__serviceClient.uploadFileClient()
        self.__serviceBorrow.uploadFileBorrow()
        self.__DTO.upload()

    def UISave(self):
        self.__serviceBook.updateFileBook()
        self.__serviceClient.updateFileClient()
        self.__serviceBorrow.updateFileBorrow()

    def UIRemove(self):
        listObject = {"book": self.UIRemoveBook, "client": self.UIRemoveClient, "borrow": self.UIRemoveBorrow}
        listObject[self.__parameters[0]]()

    def UIRemoveBook(self):
        print("")
        idBook = input("ID Book: ")
        print("")
        self.__serviceBook.removeBook(idBook)

    def UIRemoveClient(self):
        print("")
        idClient = input("ID Client: ")
        print("")
        self.__serviceClient.removeClient(idClient)

    def UIRemoveBorrow(self):
        print("")
        idBorrow = input("ID Borrow: ")
        print("")
        self.__serviceBorrow.removeBorrow(idBorrow)

    def UIModify(self):
        listObjects = {"book": self.UIModifyBook, "client": self.UIModifyClient, "borrow": self.UIModifyBorrow}
        listObjects[self.__parameters[0]]()

    def UIModifyBook(self):
        listAtributes = {"title": self.UIModifyBookTitle, "description": self.UIModifyBookDescription, "author": self.UIModifyBookAuthor}
        listAtributes[self.__parameters[1]]()

    def UIModifyBookTitle(self):
        print("")
        idBook = input("ID Book: ")
        newTitle = input("New Title: ")
        print("")
        self.__serviceBook.modifyTitle(idBook, newTitle)

    def UIModifyBookDescription(self):
        print("")
        idBook = input("ID Book: ")
        newDescription = input("New Description: ")
        print("")
        self.__serviceBook.modifyDescription(idBook, newDescription)

    def UIModifyBookAuthor(self):
        print("")
        idBook = input("ID Book: ")
        newAuthor = input("New Author: ")
        print("")
        self.__serviceBook.modifyAuthor(idBook, newAuthor)

    def UIModifyClient(self):
        listAtributes = {"name": self.UIModifyClientName, "cnp": self.UIModifyClientCNP}
        listAtributes[self.__parameters[1]]()

    def UIModifyClientName(self):
        print("")
        idClient = input("ID Client: ")
        newName = input("New Name: ")
        print("")
        self.__serviceClient.modifyName(idClient, newName)

    def UIModifyClientCNP(self):
        print("")
        idClient = input("ID Client: ")
        newCNP = input("New CNP: ")
        print("")
        self.__serviceClient.modifyCNP(idClient, newCNP)

    def UIModifyBorrow(self):
        listAtributes = {"book": self.UIModifyBorrowBook, "client": self.UIModifyBorrowClient}
        listAtributes[self.__parameters[1]]()

    def UIModifyBorrowBook(self):
        print("")
        idBorrow = input("ID Borrow: ")
        newIdBook = input("New ID Book: ")
        print("")
        self.__serviceBorrow.modifyBook(idBorrow, newIdBook)

    def UIModifyBorrowClient(self):
        print("")
        idBorrow = input("ID Borrow: ")
        newIdClient = input("New ID Client: ")
        print("")
        self.__serviceBorrow.modifyClient(idBorrow, newIdClient)

    def UISearch(self):
        listObject = {"book": self.UISearchBook, "client": self.UISearchClient, "borrow": self.UISearchBorrow}
        listObject[self.__parameters[0]]()

    def UISearchBook(self):
        print("")
        idBook = input("ID Book: ")
        print("")
        book = self.__serviceBook.getBook(idBook)
        print(book)
        print("")

    def UISearchClient(self):
        print("")
        idClient = input("ID Client: ")
        print("")
        client = self.__serviceClient.getClient(idClient)
        print(client)
        print("")

    def UISearchBorrow(self):
        print("")
        idBorrow = input("ID Borrow: ")
        print("")
        borrow = self.__serviceBorrow.getBorrow(idBorrow)
        print(borrow)
        print("")

    def UIGenerate(self):
        listObject = {"book": self.UIGenerateBook,"books": self.UIGenerateBook, "client": self.UIGenerateClient, "clients": self.UIGenerateClient, "borrow": self.UIGenerateBorrow, "borrows": self.UIGenerateBorrow}
        listObject[self.__parameters[1]]()

    def UIGenerateBook(self):
        n = int(self.__parameters[0])
        for i in range(n):
            self.__serviceBook.generateAndAddBook()
        print("")

    def UIGenerateClient(self):
        n = int(self.__parameters[0])
        for i in range(n):
            self.__serviceClient.generateAndAddClient()
        print("")

    def UIGenerateBorrow(self):
        n = int(self.__parameters[0])
        for i in range(n):
            self.__serviceBorrow.generateAndAddBorrow()
        print("")

    def UISort(self):
        listObject = {"name": self.UISortByName, "nr_books": self.UISortByNrBook, "books_author": self.UISortBooksByAuthor}
        listObject[self.__parameters[1]]()

    def UISortBooksByAuthor(self):
        list = self.__serviceBook.getListSortedByAuthorAndTitle()
        for book in list:
            print("*" * 20)
            print("")
            print(book)
            print("")
        print("*" * 20)

    def UISortByName(self):
        list = self.__serviceBorrow.filterByName()
        for client in list:
            print("*" * 20)
            print("")
            print(client)
            print("")
        print("*" * 20)

    def UISortByNrBook(self):
        list = self.__serviceBorrow.filterByNrBook()
        for client in list:
            print("*" * 20)
            print("")
            print(client)
            print("")
        print("*" * 20)

    def UIShow(self):
        listObject = {"book": self.UIShowBook, "books": self.UIShowBook, "client": self.UIShowClient, "clients": self.UIShowClient, "borrow": self.UIShowBorrow, "borrows": self.UIShowBorrow}
        listObject[self.__parameters[0]]()

    def UIShowBook(self):
        list = self.__serviceBook.getListBook()
        for book in list:
            print("*" * 20)
            print("")
            print(book)
            print("")
        print("*" * 20)

    def UIShowClient(self):
        list = self.__serviceClient.getListClient()
        for client in list:
            print("*" * 20)
            print("")
            print(client)
            print("")
        print("*" * 20)

    def UIShowBorrow(self):
        list = self.__serviceBorrow.getListBorrow()
        for borrow in list:
            print("*" * 20)
            print("")
            print(borrow)
            print("")
        print("*" * 20)

    def UITop(self):
        listObjects = {"books": self.UITopBooks, "clients": self.UITopClients, "author": self.UITopAuthor}
        listObjects[self.__parameters[0]]()

    def UITopBooks(self):
        list = self.__DTO.getListBooksSorted()
        for book in list:
            print("*" * 20)
            print("")
            print(book)
            print("")
        print("*" * 20)

    def UITopClients(self):
        list = self.__DTO.getListClientsSorted()
        n = int(len(list) / 5 + 1)
        for i in range(n):
            print("*" * 20)
            print("")
            print(list[i])
            print("")
        print("*" * 20)

    def UITopAuthor(self):
        author = self.__DTO.getTopAuthor()
        print("*" * 20)
        print("")
        print(author)
        print("")
        print("*" * 20)

    def UIDelete(self):
        self.__serviceBook.delete()
        self.__serviceClient.delete()
        self.__serviceBorrow.delete()

    def UIExit(self):
        self.UISave()
        self.__finished = True

    def runUI(self):
        self.UIUpload()
        while not self.__finished:
            command = input(">>> ").strip().lower().split()
            try:
                action = command[0].strip()
                self.__parameters = command[1:]
                self.__listActions[action]()
            except SyntaxError as se:
                print(se)
            except IndexError as ie:
                print("Incomplete action!")
            except KeyError as ke:
                print(str(ke) + " is not a valid action!")