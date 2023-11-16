def addBookToBookList(book, bookList):
    """
    adds a book in the book list
    :param book: dictionary {"id", "title", "description", "author"}
    :param bookList: list of books
    :return: -
    """
    bookList.append(book)

def addClientToClientList(client, clientList):
    """
    adds client in the client list
    :param client: dictionary {"id", "name", "cnp"}
    :param clientList: list of clients
    :return: -
    """
    clientList.append(client)