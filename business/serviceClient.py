import random
class ServiceClient():
    def __init__(self, repositoryClient, repositoryFile, validatorClient, DTO):
        self.__repositoryClient = repositoryClient
        self.__repositoryFile = repositoryFile
        self.__validatorClient = validatorClient
        self.__DTO = DTO

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
        self.__DTO.addClient(client)

    def uploadFileClient(self):
        """
        updates the information from file to program
        :return: -
        """
        text = self.__repositoryFile.read().split("@")
        n = int(text[0])
        for i in range(n):
            id = text[3*i+1]
            name = text[3*i+2]
            cnp = text[3*i+3]
            self.createClientAndAddToList(id, name, cnp)

    def updateFileClient(self):
        """
        saves the information from program in a file
        :return: -
        """
        list = self.__repositoryClient.getList()
        n = len(list)
        text = ""
        text = text + str(n)
        for client in list:
            id = client.getID()
            name = client.getName()
            cnp = client.getCNP()
            text = text + "@" + id + "@" + name + "@" + cnp
        self.__repositoryFile.write(text)

    def removeClient(self, idClient):
        """
        removes client
        :param idClient: string
        :return: -
        """
        self.__validatorClient.exist(idClient)
        self.__validatorClient.IDIsInList(idClient)
        self.__repositoryClient.removeClientByID(idClient)

    def getListClient(self):
        """
        gets client list
        :return: list
        """
        return self.__repositoryClient.getList()

    def modifyName(self, id, newName):
        """
        modifies the name of a client
        :param id: string
        :param newName: string
        :return: -
        """
        self.__validatorClient.exist(id)
        self.__validatorClient.IDIsInList(id)
        client = self.__repositoryClient.searchClientByID(id)
        self.__repositoryClient.changeName(client, newName)

    def modifyCNP(self, id, newCNP):
        """
        modifies the cnp of a client
        :param id: string
        :param newCNP: string
        :return: -
        """
        self.__validatorClient.exist(id)
        self.__validatorClient.IDIsInList(id)
        self.__validatorClient.CNPIsUnique(newCNP)
        client = self.__repositoryClient.searchClientByID(id)
        self.__repositoryClient.changeCNP(client, newCNP)

    def getClient(self, id):
        """
        gets a client
        :param id: string
        :return: class
        """
        self.__validatorClient.exist(id)
        self.__validatorClient.IDIsInList(id)
        return self.__repositoryClient.searchClientByID(id)

    def generateAndAddClient(self):
        """
        generates a client
        :return: -
        """
        nameList = ["James",
    "Robert",
    "John",
    "Michael",
    "David",
    "William",
    "Richard",
    "Joseph",
    "Thomas",
    "Christopher",
    "Charles",
    "Daniel",
    "Matthew",
    "Anthony",
    "Mark",
    "Donald",
    "Steven",
    "Andrew",
    "Paul",
    "Joshua",
    "Kenneth",
    "Kevin",
    "Brian",
    "George",
    "Timothy",
    "Edward",
    "Jeffrey",
    "Ryan",
    "Jacob",
    "Gary",
    "Nicholas",
    "Eric",
    "Jonathan",
    "Stephen",
    "Larry",
    "Justin",
    "Scott",
    "Brandon",
    "Benjamin",
    "Samuel",
    "Gregory",
    "Patrick",
    "Frank",
    "Raymond",
    "Jack",
    "Dennis",
    "Jerry",
    "Tyler",
    "Aaron",
    "Jose",
    "Adam",
    "Nathan",
    "Henry",
    "Zachary",
    "Douglas",
    "Peter",
    "Kyle",
    "Noah",
    "Ethan",
    "Jeremy",
    "Walter",
    "Christian",
    "Keith",
    "Roger",
    "Austin",
    "Sean",
    "Gerald",
    "Carl",
    "Keith",
    "Roger",
    "Terry",
    "Austin",
    "Sean",
    "Gerald",
    "Carl"]
        name = random.choice(nameList)
        id = str(random.randint(1, 1000000000))
        cnp = str(random.randint(1, 1000000000))
        client = self.__repositoryClient.createClient(id, name, cnp)
        self.__repositoryClient.addClient(client)
        self.__DTO.addClient(client)