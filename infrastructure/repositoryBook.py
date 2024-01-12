from operator import index
class RepositoryBook():
    def __init__(self, book):
        self.__book = book
        self.__listBook = []

    def getList(self):
        """
        gets the book list
        :return: list
        """
        return self.__listBook

    def createBook(self, id, title, description, author):
        """
        creates a book
        :param id: string
        :param title: string
        :param description: string
        :param author: string
        :return: class
        """
        return self.__book(id, title, description, author)

    def changeTitle(self, book, newTitle):
        """
        changes the tile of a book
        :param book: class
        :param newTitle: string
        :return: -
        """
        self.__book = book
        self.__book.setTitle(newTitle)

    def changeDescription(self, book, newDescription):
        """
        changes the description of a book
        :param book: class
        :param newDescription: string
        :return: -
        """
        self.__book = book
        self.__book.setDescription(newDescription)

    def changeAuthor(self, book, newAuthor):
        """
        changes the auhtor of a book
        :param book: class
        :param newAuthor: string
        :return: -
        """
        self.__book = book
        self.__book.setAuthor(newAuthor)

    def addBook(self, book):
        """
        add book to list
        :param book: class
        :return: -
        """
        self.__listBook.append(book)

    def searchBookByID(self, id, index = 0):
        """
        search book by id
        :param id: string
        :return: class
        """
        #for book in self.__listBook:
            #if book.getID() == id:
                #return book
        if index == len(self.__listBook):
            return None

        if self.__listBook[index].getID() == id:
            return self.__listBook[index]

        return self.searchBookByID(id, index+1)


    def removeBookByID(self, id, index = 0):
        """
        removes book by id
        :param id: string
        :return: -
        """
        #for book in self.__listBook:
            #if book.getID() == id:
                #self.__listBook.remove(book)
        """
        Calcul Complexitate:
            1) Caz favorabil: elementul care trebuie eliminat este primul    => 2 comparatii        => teta(1)
            2) Caz nefavorabil: elementul care trebuie eliminat este ultimul => 2n + 1 comparatii   => teta(n)
            
            1), 2) => complexitate timp este O(n)
        """
        if index == len(self.__listBook):
            return None

        if self.__listBook[index].getID() == id:
            self.__listBook.remove(self.__listBook[index])
            return

        return self.removeBookByID(id, index+1)

    def delete(self):
        """
        deletes the book list
        :return: -
        """
        self.__listBook.clear()