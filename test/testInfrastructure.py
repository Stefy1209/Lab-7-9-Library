from domain.book import Book
from domain.client import Client
from domain.borrow import Borrow
from infrastructure.repositoryBook import RepositoryBook
from infrastructure.repositoryClient import RepositoryClient
from infrastructure.repositoryBorrow import RepositoryBorrow
def testGetListBook():
    SB = RepositoryBook(Book)
    assert SB.getList() == []

def testCreateBook():
    SB = RepositoryBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    assert book == Book(id, title, description, author)

def testAddBook():
    SB = RepositoryBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)

    assert SB.getList() == [book]

def testSearchBookByID():
    SB = RepositoryBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)

    assert SB.searchBookByID(id) == book

def testRemoveByID():
    SB = RepositoryBook(Book)
    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = SB.createBook(id, title, description, author)

    SB.addBook(book)
    SB.removeBookByID(id)

    assert SB.getList() == []

def testDelete():
    SB = RepositoryBook(Book)
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
    SC = RepositoryClient(Client)
    assert SC.getList() == []

def testCreateClient():
    SC = RepositoryClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    assert client == Client(id, name, cnp)

def testAddClient():
    SC = RepositoryClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    SC.addClient(client)

    assert SC.getList() == [client]

def testSearchClientByID():
    SC = RepositoryClient(Client)
    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClient(id, name, cnp)

    SC.addClient(client)

    assert SC.searchClientByID(id) == client
    assert SC.searchClientByID("2") == None

def testRemoveClientByID():
    SC = RepositoryClient(Client)
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
    SC = RepositoryClient(Client)
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

def testGetListBorrow():
    RBr = RepositoryBorrow(Borrow)
    assert RBr.getList() == []

def testCreateBorrow():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = RBk.createBook(id, title, description, author)

    id = "1"
    name = "2"
    cnp = "3"
    client = RC.createClient(id, name, cnp)

    id = "4"
    borrow = RBr.createBorrow(id, book, client)
    assert borrow == Borrow(id, book, client)

def testAddBorrow():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = RBk.createBook(id, title, description, author)

    id = "1"
    name = "2"
    cnp = "3"
    client = RC.createClient(id, name, cnp)

    id = "4"
    borrow = RBr.createBorrow(id, book, client)

    RBr.addBorrow(borrow)
    assert RBr.getList() == [borrow]

    RBr.addBorrow(borrow)
    assert RBr.getList() == [borrow, borrow]

def testSearchBorrowByID():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = RBk.createBook(id, title, description, author)

    id = "1"
    name = "2"
    cnp = "3"
    client = RC.createClient(id, name, cnp)

    id = "4"
    borrow = RBr.createBorrow(id, book, client)

    RBr.addBorrow(borrow)
    assert RBr.searchBorrowByID("1") == None
    assert RBr.searchBorrowByID(id) == borrow

def testRemoveBorrowByID():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = RBk.createBook(id, title, description, author)

    id = "1"
    name = "2"
    cnp = "3"
    client = RC.createClient(id, name, cnp)

    id = "4"
    borrow = RBr.createBorrow(id, book, client)

    RBr.addBorrow(borrow)
    assert RBr.getList() == [borrow]

    RBr.removeBorrowByID(id)
    assert RBr.getList() == []

def testDeleteListBorrow():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    id = "1"
    title = "a"
    description = "b"
    author = "c"
    book = RBk.createBook(id, title, description, author)

    id = "1"
    name = "2"
    cnp = "3"
    client = RC.createClient(id, name, cnp)

    id = "4"
    borrow = RBr.createBorrow(id, book, client)

    RBr.addBorrow(borrow)
    RBr.addBorrow(borrow)
    RBr.delete()
    assert RBr.getList() == []

def testRepositoryBorrow():
    testGetListBorrow()
    testCreateBorrow()
    testAddBorrow()
    testSearchBorrowByID()
    testRemoveBorrowByID()
    testDeleteListBorrow()

def runTestInfrastructure():
    testRepositoryBook()
    testRepositoryClient()
    testRepositoryBorrow()