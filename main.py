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
from business.serviceBook import ServiceBook
from business.serviceClient import ServiceClient
from business.serviceBorrow import ServiceBorrow
from UI.mainUI import UI

runTest()

RBk = RepositoryBook(Book)
RC = RepositoryClient(Client)
RBr = RepositoryBorrow(Borrow)

VBk = ValidatorBook(RBk)
VC = ValidatorClient(RC)
VBr = ValidatorBorrow(RBr, VBk, VC)

SBk = ServiceBook(RBk, VBk)
SC = ServiceClient(RC, VC)
SBr = ServiceBorrow(RBk, RC, RBr, VBr)

UI = UI(SBk, SC, SBr)
UI.runUI()