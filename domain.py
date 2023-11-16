def createBook(id, title, description, author):
    """
    creates a book
    :param id: int
    :param title: string
    :param description: string
    :param author: string
    :return: dictionary
    """
    return {"id": id, "title": title, "description": description, "author": author}

def getID(object):
    """
    gets the ID of an object(book or client)
    :param object: dictionary
    :return: int
    """
    return object["id"]

def getTitle(book):
    """
    gets the title of a book
    :param book: dictionary
    :return: string
    """
    return book["title"]

def getDescription(book):
    """
    gets the description of a book
    :param book: dictionary
    :return: string
    """
    return book["description"]

def getAuthor(book):
    """
    gets the author of a book
    :param book: dictionary
    :return: string
    """
    return book["author"]

def createClient(id, name, cnp):
    """
    creates a client
    :param id: int
    :param name: string
    :param CNP: string
    :return: dictionary
    """
    return {"id": id, "name": name, "cnp": cnp}

def getName(client):
    """
    gets the name of a client
    :param client: dictionary
    :return: string
    """
    return client["name"]

def getCNP(client):
    """
    gets the CNP of a client
    :param client: dictionary
    :return: string
    """
    return client["cnp"]