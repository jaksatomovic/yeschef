from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Coolinarika:
    @classmethod
    def host(cls):
        return "coolinarika.com"

    def __new__(cls, html, url):
        return CoolinarikaCurated(html, url)


class CoolinarikaCurated(AbstractScraper):
    @classmethod
    def host(cls):
        return "coolinarika.com"
    
    def yields(self):
        try:
            # Pretpostavimo da je informacija o yield-u smještena u specifičnom elementu
            yield_element = self.soup.find("div", class_="recipe-yield")
            return normalize_string(yield_element.text) if yield_element else None
        except Exception as e:
            # Ako se dogodi greška, vratite `None` umjesto da program pukne
            print(f"Error fetching yields: {e}")
            return None

    def ingredients(self):
        ingredients_list = []

        # Pronađi sve elemente s klasom "css-155pf7j" unutar "groupItems"
        group_items = self.soup.find("div", class_="groupItems")
        if not group_items:
            return ingredients_list

        ingredient_items = group_items.find_all("div", class_="css-155pf7j")

        for item in ingredient_items:
            # Dohvati količinu i naziv sastojka
            quantity = item.text.strip()  # Dohvaća cijeli tekst iz elementa

            # Provjeri ima li dodatne linkove ili spanove za precizno ime sastojka
            name_span = item.find("span")
            if name_span:
                name_text = name_span.text.strip()
                quantity = quantity.replace(name_text, "").strip()
                ingredients_list.append(f"{quantity} {name_text}".strip())
            else:
                ingredients_list.append(quantity)

        return ingredients_list


