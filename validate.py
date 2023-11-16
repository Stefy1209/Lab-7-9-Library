def validateAction(command):
    """
    validates the command
    :param command: string
    :return: errors
    """
    errors = ""

    validActions = ["add", "remove", "show", "help", "exit"]
    if not command in validActions:
        errors += "Invalid Command!\n"

    if len(errors) > 0:
        raise SyntaxError(errors)