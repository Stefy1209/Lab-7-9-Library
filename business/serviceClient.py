import random
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
        self.__validatorClient.exist(id)
        self.__validatorClient.IDIsInList(id)
        client = self.__repositoryClient.searchClientByID(id)
        self.__repositoryClient.changeName(client, newName)

    def modifyCNP(self, id, newCNP):
        self.__validatorClient.exist(id)
        self.__validatorClient.IDIsInList(id)
        self.__validatorClient.CNPIsUnique(newCNP)
        client = self.__repositoryClient.searchClientByID(id)
        self.__repositoryClient.changeCNP(client, newCNP)

    def getClient(self, id):
        self.__validatorClient.exist(id)
        self.__validatorClient.IDIsInList(id)
        return self.__repositoryClient.searchClientByID(id)

    def generateAndAddClient(self):
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
        id = random.randint(1, 1000000000)
        cnp = random.randint(1, 1000000000)
        client = self.__repositoryClient.createClient(id, name, cnp)
        self.__repositoryClient.addClient(client)