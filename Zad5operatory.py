# sprawdzenie czy lista 1 zawiera wartość z listy 2
type1 = [1, 1, 2, 4, 6, 10]
type2 = 2
def check_list(type1: list, type2: int ) -> bool:
    return type2 in type1
print (check_list (type1, type2))

