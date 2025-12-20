#stworzenie funkcji która sprawdza czy liczba jest parzysta
def is_even(number: int) -> bool:
    return number % 2 == 0
print (is_even(2))
print (is_even(3))
number = 5
result = is_even(number)
if result :
    print("liczba parzysta")
else:
    print("liczba nieparzysta")

