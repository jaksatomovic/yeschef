from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class IndexRecepti:
    @classmethod
    def host(cls):
        return "recepti.index.hr"

    def __new__(cls, html, url):
        # if AllRecipesUser.host() in url:
        #     return AllRecipesUser(html, url)
        return IndexReceptiCurated(html, url)


class IndexReceptiCurated(AbstractScraper):
    @classmethod
    def host(cls):
        return "recepti.index.hr"

    def ingredients(self):
        ingredients_list = []

        # Pronađi sve elemente sastojaka
        ingredient_items = self.soup.find_all("div", class_="recipe-page__ingredients__item ng-star-inserted")

        for item in ingredient_items:
            # Pronađi količinu (ako postoji)
            quantity = item.find("strong", class_="ingredient-value ng-star-inserted")
            quantity_text = normalize_string(quantity.text) if quantity else ""

            # Pronađi ime sastojka
            name = item.find("span", class_="ingredient-name ng-star-inserted")
            name_text = normalize_string(name.text) if name else ""

            # Kombiniraj količinu i ime sastojka
            if quantity_text or name_text:
                ingredients_list.append(f"{quantity_text} {name_text}".strip())

        return ingredients_list


