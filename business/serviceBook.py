import random
from sortari.sortari import shake_sort
class ServiceBook():
    def __init__(self, repositoryBook, repositoryFile, validatorBook, DTO):
        self.__repositoryBook = repositoryBook
        self.__repositoryFile = repositoryFile
        self.__validatorBook = validatorBook
        self.__DTO = DTO

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
        self.__DTO.addBook(book)
        self.__DTO.addAuthor(author)

    def uploadFileBook(self):
        """
        uploads information from file in program
        :return: -
        """
        text = self.__repositoryFile.read().split("@")
        n = int(text[0])
        for i in range(n):
            id = text[4*i+1]
            title = text[4*i+2]
            description = text[4*i+3]
            auhtor = text[4*i+4]
            self.createBookAndAddToList(id, title, description, auhtor)

    def updateFileBook(self):
        """
        saves information in a file
        :return: -
        """
        list = self.__repositoryBook.getList()
        n = len(list)
        text = ""
        text = text + str(n)
        for book in list:
            id = book.getID()
            title = book.getTitle()
            description = book.getDescription()
            author = book.getAuthor()
            text = text + "@" + id + "@" + title + "@" + description + "@" + author
        self.__repositoryFile.write(text)

    def removeBook(self, idBook):
        """
        removes book
        :param idBook: string
        :return: -
        """
        self.__validatorBook.isID(idBook)
        self.__validatorBook.IDIsInList(idBook)
        book = self.__repositoryBook.searchBookByID(idBook)
        self.__validatorBook.bookIsAvaible(book)
        self.__repositoryBook.removeBookByID(idBook)


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
        self.__validatorBook.isID(id)
        self.__validatorBook.IDIsInList(id)
        return self.__repositoryBook.searchBookByID(id)

    def modifyTitle(self, id, newTitle):
        """
        modifies the title of the book with the id
        :param id: string
        :param newTitle: string
        :return: -
        """
        self.__validatorBook.isID(id)
        self.__validatorBook.IDIsInList(id)
        book = self.__repositoryBook.searchBookByID(id)
        self.__repositoryBook.changeTitle(book, newTitle)

    def modifyDescription(self, id, newDescription):
        """
        modifies the description of the book with the id
        :param id: string
        :param newDescription: string
        :return: -
        """
        self.__validatorBook.isID(id)
        self.__validatorBook.IDIsInList(id)
        book = self.__repositoryBook.searchBookByID(id)
        self.__repositoryBook.changeDescription(book, newDescription)

    def modifyAuthor(self, id, newAuthor):
        """
        modifies the author of the book by id
        :param id: string
        :param newAuthor: string
        :return: -
        """
        self.__validatorBook.isID(id)
        self.__validatorBook.IDIsInList(id)
        book = self.__repositoryBook.searchBookByID(id)
        self.__repositoryBook.changeAuthor(book, newAuthor)

    def delete(self):
        self.__repositoryBook.delete()

    def generateAndAddBook(self):
        """
        generates book
        :return: -
        """
        titleList = ["Pride and Prejudice",
    "1984",
    "Crime and Punishment",
    "Hamlet",
    "History (La Storia, #1-2)",
    "Poems of Paul Celan",
    "Berlin Alexanderplatz",
    "Njal's Saga",
    "The Orchard: The Bostan Of Saadi Of Shiraz",
    "The Poems of Giacomo Leopardi",
    "Swann's Way",
    "A Storm of Swords"]
        descriptionList = ["Fantasy",
    "Science fiction",
    "Mystery fiction",
    "Horror fiction",
    "Historical fiction",
    "Romance novel",
    "Women's fiction",
    "Literary fiction",
    "Magic realism",
    "Graphic novel",
    "Short story",
    "Young adult fiction",
    "New adult fiction",
    "Biography",
    "Self-help",
    "History",
    "True crime",
    "Dystopian",
    "Action & Adventure",
    "Thriller & Suspense",
    "LGBTQ+",
    "Contemporary Fiction",
    "Children's",
    "Memoir & Autobiography",
    "Food & Drink",
    "Art & Photography",
    "Travel",
    "Humor"]
        authorList = ["William Shakespeare",
    "Agatha Christie",
    "Barbara Cartland",
    "Danielle Steel",
    "Harold Robbins",
    "Georges Simenon",
    "Enid Blyton",
    "J. K. Rowling",
    "Sidney Sheldon",
    "Eiichiro Oda",
    "Gilbert Patten",
    "Tom Clancy",
    "Dr. Seuss",
    "Akira Toriyama",
    "Leo Tolstoy",
    "Corín Tellado",
    "Dean Koontz",
    "Jackie Collins",
    "Horatio Alger",
    "Nora Roberts",
    "Jane Austen",
    "Emily Bronte",
    "Geoffrey Chaucer",
    "Homer",
    "Joseph Conrad",
    "Charles Dickens",
    "Herman Melleville",
    "William Faulkner",
    "Edgar Allan Poe",
    "Mark Twain",
    "F. Scott Fitzgerald",
    "Leo Tolstoy",
    "Gustave Flaubert",
    "Herman Melville",
    "Gabriel Garcia Marquez",
    "George Orwell"]
        id = str(random.randint(1, 1000000000))
        title = random.choice(titleList)
        description = random.choice(descriptionList)
        author = random.choice(authorList)
        book = self.__repositoryBook.createBook(id, title, description, author)
        self.__repositoryBook.addBook(book)
        self.__DTO.addBook(book)
        self.__DTO.addAuthor(author)

    def getListSortedByAuthorAndTitle(self):
        list = self.__repositoryBook.getList().copy()
        shake_sort(list, reversed=False, key = lambda book:(book.getAuthor(), book.getTitle()))
        return list