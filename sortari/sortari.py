def shake_sort(list = [], *, reversed = False, key = lambda x:x):
    """
    sort list
    :param list: list
    :param reversed: False => sort from lowest to highest, True => sort from highest to lowest
    :param key: how to compare 2 elements
    :return: -
    """
    sorted = False
    while not sorted:
        sorted = True
        for index in range(0, len(list)-1):
            if reversed:
                if key(list[index]) < key(list[index+1]):
                    list[index], list[index+1] = list[index+1], list[index]
                    sorted = False
            else:
                if key(list[index]) > key(list[index+1]):
                    list[index], list[index+1] = list[index+1], list[index]
                    sorted = False

        for index in range(len(list), 1):
            if reversed:
                if key(list[index - 1]) < key(list[index]):
                    list[index - 1], list[index] = list[index], list[index - 1]
                    sorted = False
            else:
                if key(list[index - 1]) > key(list[index]):
                    list[index - 1], list[index] = list[index], list[index - 1]
                    sorted = False

def selection_sort(list, * , reversed = False, key = lambda x:x):
    """
    sort list
    :param list: list
    :param reversed: False => sort from lowest to highest, True => sort from highest to lowest
    :param key: how to compare 2 elements
    :return: -
    """
    for i in range(len(list) - 1):
        min = list[i]
        pmin = i
        for j in range(i+1, len(list)):
            if not reversed:
                if key(min) > key(list[j]):
                    min = list[j]
                    pmin = j
            else:
                if key(min) < key(list[j]):
                    min = list[j]
                    pmin = j

        list[i], list[pmin] = list[pmin], list[i]