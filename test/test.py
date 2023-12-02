from test.testDomain import runTestDomain
from test.testInfrastructure import runTestInfrastructure
from test.testBusiness import runTestBusiness
def runTest():
    runTestDomain()
    runTestInfrastructure()
    runTestBusiness()