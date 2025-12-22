#stworzenie funkcji która sprawdza czy liczba jest parzysta
def is_even(number: int) -> bool:
    return number % 2 == 0


number = 6
result = is_even(number)
if result :
    print("liczba parzysta")
else:
    print("liczba nieparzysta")

