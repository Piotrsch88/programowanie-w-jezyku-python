# Stworzenie funkcji która przyjmuje 2 agrumenty typu string
name = "Jan"
surname = "Kowalski"
def type_name(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


greetings = type_name(name, surname)
print(greetings)