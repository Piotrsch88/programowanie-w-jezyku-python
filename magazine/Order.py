from . import utils


class Order:
    def __init__(self, order_number):
        self.order_number = order_number

    def show(self):
        utils.print_message(f"Zamówienie nr: {self.order_number}")
