class RepositoryFile():
    def __init__(self, nameFile):
        self.__fileName = nameFile

    def read(self):
        """
        reads a file
        :return: string
        """
        file = open(self.__fileName, "r")
        text = file.read()
        file.close()
        return text

    def write(self, text):
        """
        writes in the file
        :param text: string
        :return: -
        """
        file = open(self.__fileName, "w")
        file.write(text)
        file.close()