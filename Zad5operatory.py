# sprawdzenie czy lista 1 zawiera wartość z listy 2
values = [1, 1, 2, 4, 6, 10]
value = 2


def check_list(values: list, value: int) -> bool:
    return value in values


print(check_list(values, value))
