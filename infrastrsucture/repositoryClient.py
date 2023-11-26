class repositoryClient:
    """
    gestionates the list of clients
    """
    def __init__(self, Client):
        """
        creates the list of clients
        """
        self.__Client = Client
        self.__ClientList = []

    def createClient(self, ID, Name, Description):
        return self.__Client(ID, Name, Description)

    def addClient(self, Client):
        """
        adds a client in the list
        :param Client: class
        :return: -
        """
        self.__ClientList.append(Client)

    def insertClient(self, Client, position):
        """
        inserts a client in the list
        :param Client: class
        :param position: integer
        :return: -
        """
        self.__ClientList.insert(Client, position)

    def sizeList(self):
        """
        gets the length of the list
        :return: integer
        """
        return len(self.__ClientList)

    def getAll(self):
        """
        gets the list
        :return: list
        """
        return self.__ClientList

    def searchByID(self, ID):
        """
        gets the client from the list with the ID
        :param ID: string
        :return: class
        """
        for client in self.__ClientList:
            if client.getID() == ID:
                return client

    def isInList(self, ID):
        """
        verifies if the client with the ID is in the list
        :param ID: string
        :return: bool
        """
        for client in self.__ClientList:
            if client.getID() == ID:
                return True

        return False

    def isEmpty(self):
        """
        verifies if the list is empty
        :return: bool
        """
        return len(self.__ClientList) == 0

    def removeByID(self, ID):
        """
        removes the client with the ID
        :param ID: string
        :return: -
        """
        for client in self.__ClientList:
            if client.getID() == ID:
                self.__ClientList.remove(client)

    def delete(self):
        """
        empties the liest
        :return: -
        """
        self.__ClientList.clear()