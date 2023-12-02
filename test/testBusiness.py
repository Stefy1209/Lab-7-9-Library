from domain.book import Book
from domain.client import Client
from domain.borrow import Borrow
from validator.validatorBook import ValidatorBook
from validator.validatorClient import ValidatorClient
from validator.validatorBorrow import ValidatorBorrow
from infrastructure.repositoryBook import RepositoryBook
from infrastructure.repositoryClient import RepositoryClient
from infrastructure.repositoryBorrow import RepositoryBorrow
from business.serviceBook import ServiceBook
from business.serviceClient import ServiceClient
from business.serviceBorrow import ServiceBorrow
def testGetAllBook():
    RB = RepositoryBook(Book)
    VB = ValidatorBook(RB)
    SB = ServiceBook(RB, VB)
    assert SB.getListBook() == []

def testCreateBookAndAddToList():
    RB = RepositoryBook(Book)
    VB = ValidatorBook(RB)
    SB = ServiceBook(RB, VB)

    id = "1"
    title = "2"
    description = "3"
    author =  "4"

    SB.createBookAndAddToList(id, title, description, author)
    assert SB.getListBook() == [Book(id, title, description, author)]

def testGetBook():
    RB = RepositoryBook(Book)
    VB = ValidatorBook(RB)
    SB = ServiceBook(RB, VB)

    id = "1"
    title = "2"
    description = "3"
    author = "4"

    SB.createBookAndAddToList(id, title, description, author)
    assert SB.getBook(id) == Book(id, title, description, author)

def testModifyTitle():
    RB = RepositoryBook(Book)
    VB = ValidatorBook(RB)
    SB = ServiceBook(RB, VB)

    id = "1"
    title = "2"
    description = "3"
    author = "4"

    SB.createBookAndAddToList(id, title, description, author)
    newTitle = "5"
    SB.modifyTitle(id, newTitle)
    assert SB.getBook(id) == Book(id, newTitle, description, author)

def testModifyDecription():
    RB = RepositoryBook(Book)
    VB = ValidatorBook(RB)
    SB = ServiceBook(RB, VB)

    id = "1"
    title = "2"
    description = "3"
    author = "4"

    SB.createBookAndAddToList(id, title, description, author)
    newdescription = "5"
    SB.modifyDescription(id, newdescription)
    assert SB.getBook(id) == Book(id, title, newdescription, author)

def testModifyAuthor():
    RB = RepositoryBook(Book)
    VB = ValidatorBook(RB)
    SB = ServiceBook(RB, VB)

    id = "1"
    title = "2"
    description = "3"
    author = "4"

    SB.createBookAndAddToList(id, title, description, author)
    newAuthor = "5"
    SB.modifyAuthor(id, newAuthor)
    assert SB.getBook(id) == Book(id, title, description, newAuthor)

def testServiceBook():
    testGetAllBook()
    testCreateBookAndAddToList()
    testGetBook()
    testModifyTitle()
    testModifyDecription()
    testModifyAuthor()

def testGetListClient():
    RC = RepositoryClient(Client)
    VC = ValidatorClient(RC)
    SC = ServiceClient(RC, VC)
    assert SC.getListClient() == []

def testCreateClientAndAddToList():
    RC = RepositoryClient(Client)
    VC = ValidatorClient(RC)
    SC = ServiceClient(RC, VC)

    id = "1"
    name = "2"
    cnp = "3"
    client = SC.createClientAndAddToList(id, name, cnp)

    assert SC.getListClient() == [Client(id, name, cnp)]

def testServiceClient():
    testGetListClient()
    testCreateClientAndAddToList()

def testGetListBorrow():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    VBk = ValidatorBook(RBk)
    VC = ValidatorClient(RC)
    VBr = ValidatorBorrow(RBr, VBk, VC)

    SBr = ServiceBorrow(RBk, RC, RBk, VBr)
    assert SBr.getListBorrow() == []

def testCreateBorrowAndAddToList():
    RBk = RepositoryBook(Book)
    RC = RepositoryClient(Client)
    RBr = RepositoryBorrow(Borrow)

    VBk = ValidatorBook(RBk)
    VC = ValidatorClient(RC)
    VBr = ValidatorBorrow(RBr, VBk, VC)

    SBk = ServiceBook(RBk, VBk)
    SC = ServiceClient(RC, VC)
    SBr = ServiceBorrow(RBk, RC, RBr, VBr)

    idBook = "1"
    title = "2"
    description = "3"
    author = "4"
    SBk.createBookAndAddToList(idBook, title, description, author)

    idClient = "5"
    name = "6"
    cnp = "7"
    SC.createClientAndAddToList(idClient, name, cnp)

    idBorrow = "8"
    SBr.createBorrowAndAddToList(idBorrow, idBook, idClient)

    assert SBr.getListBorrow() == [Borrow(idBorrow, Book(idBook, title, description, author), Client(idClient, name, cnp))]

def testServiceBorrow():
    testGetListBorrow()
    testCreateBorrowAndAddToList()

def runTestBusiness():
    testServiceBook()
    testServiceClient()
    testServiceBorrow()