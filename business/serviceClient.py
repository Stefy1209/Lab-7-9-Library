class ServiceClient():
    def __init__(self, repositoryClient, validatorClient):
        self.__repositoryClient = repositoryClient
        self.__validatorClient = validatorClient

    def createClientAndAddToList(self, id, name, cnp):
        """
        creates a client and adds to list
        :param id: string
        :param name: string
        :param cnp: string
        :return: -
        """
        self.__validatorClient.exist(id)
        self.__validatorClient.exist(name)
        self.__validatorClient.exist(cnp)
        self.__validatorClient.IDIsUnique(id)
        self.__validatorClient.CNPIsUnique(cnp)
        client = self.__repositoryClient.createClient(id, name, cnp)
        self.__repositoryClient.addClient(client)

    def getListClient(self):
        """
        gets client list
        :return: list
        """
        return self.__repositoryClient.getList()