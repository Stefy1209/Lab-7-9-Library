class RepositoryFile():
    def __init__(self, nameFile):
        self.__fileName = nameFile

    def read(self):
        file = open(self.__fileName, "r")
        return file.read()

    def write(self, text):
        file = open(self.__fileName, "w")
        file.write(text)
        file.close()