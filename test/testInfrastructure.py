from domain.book import Book
from infrastructure.serviceBook import ServiceBook
def testGetList():
    SB = ServiceBook(Book)
    assert SB.getList() == []

def testCreateBook():
    SB = ServiceBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    assert book == Book(id, title, description, author)

def testAddBook():
    SB = ServiceBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)

    assert SB.getList() == [book]

def testSearchByID():
    SB = ServiceBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)

    assert SB.searchBookByID(id) == book

def testRemoveByID():
    SB = ServiceBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)
    SB.removeBookByID(id)

    assert SB.getList() == []

def testDelete():
    SB = ServiceBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)
    SB.addBook(book)
    SB.delete()

    assert SB.getList() == []

def testServiceBook():
    testGetList()
    testCreateBook()
    testAddBook()
    testSearchByID()
    testRemoveByID()
    testDelete()

def runTestInfrastructure():
    testServiceBook()