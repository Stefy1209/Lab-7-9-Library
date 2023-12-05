class RepositoryClient():
    def __init__(self, client):
        self.__client = client
        self.__listClient = []

    def getList(self):
        """
        gets client list
        :return: list
        """
        return self.__listClient

    def createClient(self, id, name, cnp):
        """
        creates a client
        :param id: string
        :param name: string
        :param cnp: string
        :return: class
        """
        return self.__client(id, name, cnp)

    def addClient(self, client):
        """
        adds client to list
        :param client: class
        :return: -
        """
        self.__listClient.append(client)

    def changeName(self, client, newName):
        client.setName(newName)

    def changeCNP(self, client, newCNP):
        client.setCNP(newCNP)

    def searchClientByID(self, id):
        """
        search client by id
        :param id: string
        :return: class
        """
        for client in self.__listClient:
            if client.getID() == id:
                return client

    def removeClientByID(self, id):
        """
        removes client by id
        :param id: string
        :return: -
        """
        for client in self.__listClient:
            if client.getID() == id:
                self.__listClient.remove(client)

    def delete(self):
        """
        deletes client list
        :return: -
        """
        self.__listClient.clear()