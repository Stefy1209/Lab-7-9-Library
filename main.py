from test.test import runTest
from validator.validatorBook import ValidatorBook
from validator.validatorClient import ValidatorClient
from validator.validatorBorrow import ValidatorBorrow
from domain.book import Book
from domain.client import Client
from domain.borrow import Borrow
from infrastructure.repositoryBook import RepositoryBook
from infrastructure.repositoryClient import RepositoryClient
from infrastructure.repositoryBorrow import RepositoryBorrow
from infrastructure.repositoryFile import RepositoryFile
from business.serviceBook import ServiceBook
from business.serviceClient import ServiceClient
from business.serviceBorrow import ServiceBorrow
from business.DTO import DTO
from UI.mainUI import UI

from sortari.sortari import selection_sort

list = [(1, 4), (0, 2), (-23, 4), (0, 234), (2, 4), (-3, 2)]

selection_sort(list, reversed=True, key= lambda x:(x[1], x[0]))

print(list)

#runTest()

RBk = RepositoryBook(Book)
RC = RepositoryClient(Client)
RBr = RepositoryBorrow(Borrow)
RFbk = RepositoryFile("book")
RFc = RepositoryFile("client")
RFbr = RepositoryFile("borrow")

VBk = ValidatorBook(RBk)
VC = ValidatorClient(RC)
VBr = ValidatorBorrow(RBr, VBk, VC)

DTO = DTO()

SBk = ServiceBook(RBk, RFbk, VBk, DTO)
SC = ServiceClient(RC, RFc, VC, DTO)
SBr = ServiceBorrow(RBk, RC, RBr, RFbr, VBr, DTO)

UI = UI(SBk, SC, SBr, DTO)
UI.runUI()