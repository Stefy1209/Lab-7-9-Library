class Client:
    """
    client is an object which stores the ID, Name and CNP
    """
    def __init__(self, id, name, cnp):
        """
        creates a client
        :param id: string
        :param name: string
        :param cnp: string
        """
        self.__id = id
        self.__name = name
        self.__cnp = cnp

    def __str__(self):
        """
        the way a client is displayed
        :return:
        """
        return (f"ID: {self.__id}\n"
                f"Name: {self.__name}\n"
                f"CNP: {self.__cnp}")

    def getID(self):
        """
        gets the ID
        :return: string
        """
        return self.__id

    def getName(self):
        """
        gets the name
        :return: string
        """
        return self.__name

    def getCNP(self):
        """
        gets the CNP
        :return: string
        """
        return self.__cnp

    def setName(self, newName):
        """
        changes the name of a client
        :param newName: string
        :return: -
        """
        self.__name = newName

    def setCNP(self, newCNP):
        """
        chnages the CNP
        :param newCNP: string
        :return: -
        """
        self.__cnp = newCNP