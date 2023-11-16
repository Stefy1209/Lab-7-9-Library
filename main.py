from test import runTest
from validate import validateAction
from service import runAddMenu, runRemoveMenu, runShowMenu, runHelpMenu, runExitMenu

def runMain():
    bookList = []
    clientList = []

    command = ""
    parameters = []
    finished = False

    while not finished:
        command = input(">>> ").lower().strip()
        command = command.split()
        action = command[0].strip()
        parameters = command[1:]

        ok = True
        try:
            validateAction(action)
        except SyntaxError as se:
            print(se, end = "")
            ok = False

        if ok:
            match action:
                case "add":
                    runAddMenu(bookList, clientList, parameters)
                case "remove":
                    runRemoveMenu(bookList, clientList, parameters)
                case "show":
                    runShowMenu(bookList, clientList, parameters)
                case "help":
                    runHelpMenu(parameters)
                case "exit":
                    finished = runExitMenu()

runTest()
runMain()