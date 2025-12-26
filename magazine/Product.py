from . import utils

class Product:
    def __init__(self, name):
        self.name = name

    def show(self):
        utils.print_message(f"Produkt: {self.name}")
