from domain import *
from infrastructure import *

def runAddMenu(bookList, clientList, parameters):
    """
    adds a book in the book list or adds a client in the client list
    :param bookList: list of books (dictionaries {"id", "title", "description", "author"})
    :param clientList: list of clients (dictionaries {"id", "name", "cnp"})
    :param parameters: list of parameters (strings)
    :return: -
    """
    object = parameters[0].strip()

    match object:
        case "book":
            id = input("ID: ")
            title = input("Title: ")
            description = input("Description: ")
            author = input("Author: ")
            book = createBook(id, title, description, author)

            if not book in bookList:
                addBookToBookList(book, bookList)

        case "client":
            id = input("ID: ")
            name = input("Full name: ")
            cnp = input("CNP: ")
            client = createClient(id, name, cnp)

            if not client in clientList:
                addClientToClientList(client, clientList)

def runRemoveMenu(bookList, clientList, parameters):
    """
    remove a book from the book list or a client from the client list
    :param bookList: list of books (dictionaries {"id", "title", "description", "author"})
    :param clientList: list of clients (dictionaries {"id", "name", "cnp"})
    :param parameters: list of parameters (strings)
    :return: -
    """
    pass

def runShowMenu(bookList, clientList, parameters):
    """
    show the book list or the client list
    :param parameters: list of parameters (strings)
    :return: -
    """
    object = parameters[0].strip()

    match object:
        case "books":
            print(bookList)
        case "clients":
            print(clientList)

def runHelpMenu(parameters):
    """
    run the help menu depending on the paramaters (add, modify, etc.)
    :param parameters: list of parameters (strings)
    :return: shows help menu
    """
    pass

def runExitMenu():
    """
    runs the exit menu
    :return: bool
    """
    return True