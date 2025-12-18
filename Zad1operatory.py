# Stworzenie funkcji która przyjmuje 2 agrumenty typu string
name = "{Jan}"
surname = "{Kowalski}"
def type_name(name: str, surname: str) -> str:
     return name + " " + surname
print(f"Cześć {type_name(name, surname)}!")