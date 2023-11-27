from domain.book import Book
from domain.client import Client
from infrastructure.repositoryBook import ServiceBook
from infrastructure.repositoryClient import ServiceClient
def testGetListBook():
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

def testSearchBookByID():
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

def testRepositoryBook():
    testGetListBook()
    testCreateBook()
    testAddBook()
    testSearchBookByID()
    testRemoveByID()
    testDelete()

def testGetListClient():
    SC = ServiceClient(Client)
    assert SC.getList() == []

def testCreateClient():
    SC = ServiceClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    assert client == Client(id, name, cnp)

def testAddClient():
    SC = ServiceClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    SC.addClient(client)

    assert SC.getList() == [client]

def testSearchClientByID():
    SC = ServiceClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    SC.addClient(client)

    assert SC.searchClientByID(id) == client
    assert SC.searchClientByID("2") == None

def testRemoveClientByID():
    SC = ServiceClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    SC.addClient(client)
    SC.removeClientByID("2")
    assert SC.getList() == [client]
    SC.removeClientByID(id)
    assert SC.getList() == []

def testDeleteListClient():
    SC = ServiceClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    SC.addClient(client)
    SC.addClient(client)
    SC.delete()
    assert SC.getList() == []

def testRepositoryClient():
    testGetListClient()
    testCreateClient()
    testAddClient()
    testSearchClientByID()
    testRemoveClientByID()
    testDeleteListClient()

def runTestInfrastructure():
    testRepositoryBook()
    testRepositoryClient()