from infrastructure import *

def runAddMenu(bookList, clientList, parameters):
    """
    adds a book in the book list or adds a client in the client list
    :param bookList: list of books (dictionaries {"id", "title", "description", "author"})
    :param clientList: list of clients (dictionaries {"id", "name", "cnp"})
    :param parameters: list of parameters (strings)
    :return: -
    """
    pass

def runRemoveMenu(bookList, clientList, parameters):
    """
    remove a book from the book list or a client from the client list
    :param bookList: list of books (dictionaries {"id", "title", "description", "author"})
    :param clientList: list of clients (dictionaries {"id", "name", "cnp"})
    :param parameters: list of parameters (strings)
    :return: -
    """
    pass

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