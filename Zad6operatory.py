# połączenie 2 list w jedną
list1 = [1, 3, 2, 3]
list2 = [3, 5, 6]


def check_number(list1: list, list2: list) -> list:
    return list(dict.fromkeys(x**3 for x in list1+list2))


print(check_number(list1, list2))
