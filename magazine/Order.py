class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ""
        for book in self.books:
            books_str += str(book) + "\n"

        return (
            f"Zamówienie:\n"
            f"Data zamówienia: {self.order_date}\n\n"
            f"{self.employee}\n\n"
            f"{self.student}\n\n"
            f"Książki:\n{books_str}"
            f"{'-' * 40}"
        )
