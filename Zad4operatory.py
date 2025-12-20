#stworzenie funkcji przyjmującej 3 argumenty typu int
def check_number(number1: int, number2: int, number3: int) -> bool:
    return number1 + number2 >= number3
print (check_number(1, 2, 3))
print (check_number(5, 8, 3))
print (check_number(1, 20, 30))