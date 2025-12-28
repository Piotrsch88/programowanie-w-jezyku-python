from datetime import date


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka:\n"
            f"  Adres: {self.street}, {self.zip_code} {self.city}\n"
            f"  Godziny otwarcia: {self.open_hours}\n"
            f"  Telefon: {self.phone}"
        )


class Employee:
    def __init__(
            self,
            first_name,
            last_name,
            hire_date,
            birth_date,
            city,
            street,
            zip_code,
            phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name}\n"
                f"Data Zatrudnienia: {self.hire_date}\n"
                f"data urodzenia: {self.birth_date}\n"
                f"adres: {self.city}, {self.street}, {self.zip_code}\n"
                f"telefon: {self.phone}"
                )


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return (f"Student: {self.first_name} {self.last_name}\n"
                f"Numer Studenta: {self.student_id}")


class Book:
    def __init__(
            self,
            library,
            publication_date,
            author_name,
            author_surname,
            number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: \n"
                f"Data publikacji: {self.publication_date}\n"
                f"Imię Autora: {self.author_name} {self.author_surname}\n"
                f"liczba stron: {self.number_of_pages}\n"
                f"{self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ""
        for book in self.books:
            books_str = books_str + str(book) + "\n"

        return (
            f"Zamówienie:\n"
            f"Data zamówienia: {self.order_date}\n\n"
            f"{self.employee}\n\n"
            f"{self.student}\n\n"
            f"Książki:\n{books_str}"
            f"{'-' * 40}"
        )


# Tworzenie obiektów
# Biblioteki
library1 = Library(
    "Katowice",
    "Mariacka 10",
    "40-150",
    "07:00 - 17:00",
    "111-222-333",
)
library2 = Library(
    "Wrocław",
    "zamkowa 2",
    "50-001",
    "08:00 - 19:00",
    "222-111-333",
)
# Pracownicy
employee1 = Employee(
    "Jan",
    "Kowalski",
    "2020-05-01",
    "1980-05-13",
    "Mysłowice",
    "działkowa 1",
    "43-500",
    "000-001-000",
)
employee2 = Employee(
    "Jan",
    "Nowak",
    "2011-06-05",
    "1990-08-05",
    "Zabrze",
    "Rosvelata 5",
    "44-100",
    "000-005-001")
employee3 = Employee(
    "Jan",
    "Jeziorański",
    "2010-11-30",
    "1985-07-05",
    "Chorzów",
    "Cicha 6",
    "41-500",
    "000-001-020",
)
# Studenci
student1 = Student("Jan", "Mak", "S123")
student2 = Student("Katarzyna", "Lewandowska", "S456")
student3 = Student("Tomasz", "Szymański", "S789")
# Książki
book1 = Book(library1, "2010-01-01", "Adam", "Mickiewicz", 350)
book2 = Book(library1, "2015-06-12", "Henryk", "Sienkiewicz", 420)
book3 = Book(library2, "2005-03-05", "Bolesław", "Prus", 280)
book4 = Book(library2, "2018-10-09", "Olga", "Tokarczuk", 390)
book5 = Book(library1, "2020-05-10", "Andrzej", "Sapkowski", 500)
# Zamówienia
order1 = Order(employee1, student1, [book1, book2], date.today())
order2 = Order(employee2, student2, [book3, book4, book5], date.today())
# ====== WYŚWIETLENIE ZAMÓWIEŃ ======
print(order1)
print(order2)
