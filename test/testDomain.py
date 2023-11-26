from domain.book import Book
from domain.client import Client
from domain.borrow import Borrow
def testGetIDBook():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    assert book.getID() == id

def testGetTitle():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    assert book.getTitle() == title

def testGetDescription():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    assert book.getDescription() == description

def testGetAuthor():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    assert book.getAuthor() == author

def testGetAvaible():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    assert book.getAvaible() == True

def testSetTitle():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    newtitle = "d"
    book.setTitle(newtitle)

    assert book.getTitle() == newtitle

def testSetDescription():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    newDescription = "d"
    book.setDescription(newDescription)

    assert book.getDescription() == newDescription

def testSetAuthor():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    newAuthor = "d"
    book.setAuthor(newAuthor)

    assert book.getAuthor() == newAuthor

def testSwitchAvaible():
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(id, title, description, author)

    book.switchAvaible()

    assert book.getAvaible() == False

    book.switchAvaible()

    assert book.getAvaible() == True

def testBook():
    testGetIDBook()
    testGetTitle()
    testGetDescription()
    testGetAuthor()
    testGetAvaible()
    testSetTitle()
    testSetDescription()
    testSetAuthor()
    testSwitchAvaible()

def testGetIDClient():
    id = "1"
    name = "a"
    cnp = "b"
    client = Client(id, name, cnp)

    assert client.getID() == id

def testGetName():
    id = "1"
    name = "a"
    cnp = "b"
    client = Client(id, name, cnp)

    assert client.getName() == name

def testGetCNP():
    id = "1"
    name = "a"
    cnp = "b"
    client = Client(id, name, cnp)

    assert client.getCNP() == cnp

def testSetName():
    id = "1"
    name = "a"
    cnp = "b"
    client = Client(id, name, cnp)

    newName = "c"
    client.setName(newName)

    assert client.getName() == newName

def testSetCNP():
    id = "1"
    name = "a"
    cnp = "b"
    client = Client(id, name, cnp)

    newCNP = "c"
    client.setCNP(newCNP)

    assert client.getCNP() == newCNP

def testClient():
    testGetIDClient()
    testGetName()
    testGetCNP()
    testSetName()
    testSetCNP()

def testGetIDBorrow():
    idBook = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(idBook, title, description, author)

    idClient = "1"
    name = "a"
    cnp = "b"
    client = Client(idClient, name, cnp)

    idBorrow = "3"
    borrow = Borrow(idBorrow, book, client)

    assert borrow.getID() == idBorrow

def testGetBook():
    idBook = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(idBook, title, description, author)

    idClient = "1"
    name = "a"
    cnp = "b"
    client = Client(idClient, name, cnp)

    idBorrow = "3"
    borrow = Borrow(idBorrow, book, client)

    assert borrow.getBook() == book

def testGetClient():
    idBook = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(idBook, title, description, author)

    idClient = "1"
    name = "a"
    cnp = "b"
    client = Client(idClient, name, cnp)

    idBorrow = "3"
    borrow = Borrow(idBorrow, book, client)

    assert borrow.getClient() == client

def testSetBook():
    idBook = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(idBook, title, description, author)

    idClient = "1"
    name = "a"
    cnp = "b"
    client = Client(idClient, name, cnp)

    idBorrow = "3"
    borrow = Borrow(idBorrow, book, client)

    newIDBook = "4"
    newTitle = "5"
    newDescription = "6"
    newAuthor = "7"
    newBook = Book(newIDBook, newTitle, newDescription, newAuthor)

    borrow.setBook(newBook)

    assert borrow.getBook() == newBook

def testSetClient():
    idBook = "1"
    title = "a"
    description = "b"
    author = "c"
    book = Book(idBook, title, description, author)

    idClient = "1"
    name = "a"
    cnp = "b"
    client = Client(idClient, name, cnp)

    idBorrow = "3"
    borrow = Borrow(idBorrow, book, client)

    newIDClient = "4"
    newName = "5"
    newCNP = "6"
    newClient = Client(newIDClient, newName, newCNP)

    borrow.setClient(newClient)

    assert borrow.getClient() == newClient

def testBorrow():
    testGetIDBorrow()
    testGetBook()
    testGetClient()
    testSetBook()
    testSetClient()

def runTestDomain():
    testBook()
    testClient()
    testBorrow()