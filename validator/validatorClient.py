class ValidatorClient():
    def __init__(self, repositoryClient):
        self.__repositoryClient = repositoryClient

    def exist(self, thing):
        if thing == "":
            raise SyntaxError("Something is missing!")

    def IDIsUnique(self, id):
        list = self.__repositoryClient.getList()
        for client in list:
            if id == client.getID():
                raise SyntaxError("ID is not unique!")

    def IDIsInList(self, id):
        list = self.__repositoryClient.getList()
        for client in list:
            if id == client.getID():
                return
        raise SyntaxError("There is no client with this ID!")

    def CNPIsUnique(self, cnp):
        list = self.__repositoryClient.getList()
        for client in list:
            if cnp == client.getCNP():
                raise SyntaxError("CNP is not unique!")