class Client():
    def __init__(self, id, name, cnp):
        """
        creates client
        :param id:
        :param name:
        :param cnp:
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
        gets the id
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
        gets the cnp
        :return: string
        """
        return self.__cnp

    def setName(self, newName):
        """
        changes the name with the new one
        :param newName: string
        :return:
        """
        self.__name = newName

    def setCNP(self, newCNP):
        """
        chnages the cnp with the new one
        :param newCNP: string
        :return:
        """
        self.__cnp = newCNP