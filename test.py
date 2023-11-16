from domain import *
from infrastructure import *

def testCreateBook():
    id = 23
    title = "Scufita rosie"
    description = "Horror"
    author = "Brothers Grimm"

    book = createBook(id, title, description, author)
    assert book == {"id": 23, "title": "Scufita rosie", "description": "Horror", "author": "Brothers Grimm"}

def testGetID():
    id = 23
    title = "Scufita rosie"
    description = "Horror"
    author = "Brothers Grimm"

    book = createBook(id, title, description, author)
    assert getID(book) == id

    id = 42
    name = "James Bond"
    cnp = "007"

    client = createClient(id, name, cnp)
    assert getID(client) == id

def testGetTitle():
    id = 23
    title = "Scufita rosie"
    description = "Horror"
    author = "Brothers Grimm"

    book = createBook(id, title, description, author)
    assert getTitle(book) == title

def testGetDescription():
    id = 23
    title = "Scufita rosie"
    description = "Horror"
    author = "Brothers Grimm"

    book = createBook(id, title, description, author)
    assert getDescription(book) == description

def testGetAuthor():
    id = 23
    title = "Scufita rosie"
    description = "Horror"
    author = "Brothers Grimm"

    book = createBook(id, title, description, author)
    assert getAuthor(book) == author

def testCreateClient():
    id = 42
    name = "James Bond"
    cnp = "007"

    client = createClient(id, name, cnp)
    assert client == {"id": id, "name": name, "cnp": cnp}

def testGetName():
    id = 42
    name = "James Bond"
    cnp = "007"

    client = createClient(id, name, cnp)
    assert getName(client) == name

def testGetCNP():
    id = 42
    name = "James Bond"
    cnp = "007"

    client = createClient(id, name, cnp)
    assert getCNP(client) == cnp

def testAddBookToBookList():
    id = 23
    title = "Scufita rosie"
    description = "Horror"
    author = "Brothers Grimm"
    book1 = createBook(id, title, description, author)

    id = 17
    title = "Cell"
    description = "Horror"
    author = "Stephen King"
    book2 = createBook(id, title, description, author)

    id = 41
    title = "Foc si sange"
    description = "Fantasy"
    author = "George R. R. Martin"
    book3 = createBook(id, title, description, author)

    bookList = []
    addBookToBookList(book1, bookList)
    addBookToBookList(book3, bookList)
    addBookToBookList(book2, bookList)

    assert bookList == [book1, book3, book2]

def testAddClientToClientList():
    id = 2
    name = "James Bond"
    cnp = "007"
    client1 = createClient(id, name, cnp)

    id = 40
    name = "James Hetfield"
    cnp = "1981"
    client2 = createClient(id, name, cnp)

    id = 3
    name = "Arthur Morgan"
    cnp = "1899"
    client3 = createClient(id, name, cnp)

    clientList = []
    addClientToClientList(client1, clientList)
    addClientToClientList(client3, clientList)
    addClientToClientList(client2, clientList)

    assert clientList == [client1, client3, client2]

def testDomain():
    testCreateBook()
    testGetID()
    testGetTitle()
    testGetDescription()
    testGetAuthor()
    testCreateClient()
    testGetName()
    testGetCNP()

def testInfrastructure():
    testAddBookToBookList()
    testAddClientToClientList()

def runTest():
    testDomain()
    testInfrastructure()