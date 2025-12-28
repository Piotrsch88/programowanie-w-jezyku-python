from datetime import date

from magazine.Library import Library
from magazine.Employee import Employee
from magazine.Student import Student
from magazine.Book import Book
from magazine.Order import Order

# ====== BIBLIOTEKI ======
library1 = Library(
    "Katowice",
    "Mariacka 10",
    "40-150",
    "07:00 - 17:00",
    "111-222-333",
)
library2 = Library(
    "Wrocław",
    "Zamkowa 2",
    "50-001",
    "08:00 - 19:00",
    "222-111-333",
)

# ====== PRACOWNICY ======
employee1 = Employee(
    "Jan",
    "Kowalski",
    "2020-05-01",
    "1980-05-13",
    "Mysłowice",
    "Działkowa 1",
    "43-500",
    "000-001-000",
)
employee2 = Employee(
    "Jan",
    "Nowak",
    "2011-06-05",
    "1990-08-05",
    "Zabrze",
    "Roosevelta 5",
    "44-100",
    "000-005-001",
)

# ====== STUDENCI ======
student1 = Student("Jan", "Mak", "S123")
student2 = Student("Katarzyna", "Lewandowska", "S456")

# ====== KSIĄŻKI ======
book1 = Book(library1, "2010-01-01", "Adam", "Mickiewicz", 350)
book2 = Book(library1, "2015-06-12", "Henryk", "Sienkiewicz", 420)
book3 = Book(library2, "2005-03-05", "Bolesław", "Prus", 280)

# ====== ZAMÓWIENIA ======
order1 = Order(employee1, student1, [book1, book2], date.today())
order2 = Order(employee2, student2, [book3], date.today())

# ====== WYŚWIETLENIE ======
print(order1)
print(order2)
