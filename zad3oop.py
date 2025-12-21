class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            "Dom\n"
            + "Adres: " + self.address + "\n"
            + "Powierzchnia: " + str(self.area) + "\n"
            + "Pokoje: " + str(self.rooms) + "\n"
            + "Cena: " + str(self.price) + "\n"
            + "Dzialka: " + str(self.plot)
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            "Mieszkanie\n"
            + "Adres: " + self.address + "\n"
            + "Powierzchnia: " + str(self.area) + "\n"
            + "Pokoje: " + str(self.rooms) + "\n"
            + "Cena: " + str(self.price) + "\n"
            + "Pietro: " + str(self.floor)
        )


# Tworzenie obiektów
house = House(120, 4, 750000, "Warszawa, ul. Lesna 10", 500)
flat = Flat(55, 2, 420000, "Krakow, ul. Dluga 5", 3)

# Wyswietlanie
print(house)
print()
print(flat)
