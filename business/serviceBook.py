class ServiceBook():
    def __init__(self, repositoryBook, validatorBook):
        self.__repositoryBook = repositoryBook
        self.__validatorBook = validatorBook

    def createBookAndAddToList(self, id, title, description, author):
        """
        creates a book and adds it to list
        :param id: string
        :param title: string
        :param description: string
        :param author: string
        :return: -
        """
        self.__validatorBook.isID(id)
        self.__validatorBook.IDIsUnique(id)
        book = self.__repositoryBook.createBook(id, title, description, author)
        self.__repositoryBook.addBook(book)

    def getListBook(self):
        """
        gets the book list
        :return: list
        """
        return self.__repositoryBook.getList()

    def getBook(self, id):
        """
        gets a book by id
        :param id: string
        :return: class
        """
        return self.__repositoryBook.searchBookByID(id)

    def modifyTitle(self, id, newTitle):
        """
        modifies the title of the book with the id
        :param id: string
        :param newTitle: string
        :return: -
        """
        book = self.__repositoryBook.searchBookByID(id)
        self.__repositoryBook.changeTitle(book, newTitle)

    def modifyDescription(self, id, newDescription):
        """
        modifies the description of the book with the id
        :param id: string
        :param newDescription: string
        :return: -
        """
        book = self.__repositoryBook.searchBookByID(id)
        self.__repositoryBook.changeDescription(book, newDescription)

    def modifyAuthor(self, id, newAuthor):
        """
        modifies the author of the book by id
        :param id: string
        :param newAuthor: string
        :return: -
        """
        book = self.__repositoryBook.searchBookByID(id)
        self.__repositoryBook.changeAuthor(book, newAuthor)