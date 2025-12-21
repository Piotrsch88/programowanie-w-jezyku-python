# stworzenie skryptu pytonowego
import requests


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        longitude: str,
        latitude: str,
        phone: str,
        website_url: str
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"Nazwa browaru: {self.name}\n"
            f"Typ: {self.brewery_type}\n"
            f"Adres: {self.street}, {self.city}, {self.state}, {self.postal_code}\n"
            f"Kraj: {self.country}\n"
            f"Telefon: {self.phone}\n"
            f"Strona WWW: {self.website_url}\n"
            f"Współrzędne: ({self.latitude}, {self.longitude})\n"
            "--------------------------------------------"
        )


def main():
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

    response = requests.get(url)

    breweries_data = response.json()

    breweries_list = []

    for brewery in breweries_data:
        brewery_object = Brewery(
            id=brewery.get("id"),
            name=brewery.get("name"),
            brewery_type=brewery.get("brewery_type"),
            street=brewery.get("street"),
            city=brewery.get("city"),
            state=brewery.get("state"),
            postal_code=brewery.get("postal_code"),
            country=brewery.get("country"),
            longitude=brewery.get("longitude"),
            latitude=brewery.get("latitude"),
            phone=brewery.get("phone"),
            website_url=brewery.get("website_url")
        )

        breweries_list.append(brewery_object)

    for brewery in breweries_list:
        print(brewery)


if __name__ == "__main__":
    main()
