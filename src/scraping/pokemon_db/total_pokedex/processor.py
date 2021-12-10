import re
from base.processors.pokedex.pokdex_processor import PokedexProcessor
from bs4 import BeautifulSoup


class PokdemonDBTotalPokedexProcessor(PokedexProcessor):
    def __init__(self) -> None:
        super().__init__()

    def get_number(self, pokemon_row: BeautifulSoup) -> int:
        num = pokemon_row.find("td", class_="cell-fixed")["data-sort-value"]
        return int(num)

    def get_name(self, pokemon_row: BeautifulSoup) -> str:
        return " ".join(
            pokemon_row.find(attrs={"data-alt": re.compile("icon")})["data-alt"].split(
                " "
            )[:-1]
        )

    def get_types(self, pokemon_row: BeautifulSoup) -> list[str]:
        uncleaned_types_ele = pokemon_row.find_all("a", class_="type-icon")
        cleaned_types = list(map(lambda x: x.text, uncleaned_types_ele))
        return cleaned_types if len(cleaned_types) == 2 else [cleaned_types[0], None]

    def get_stats(self, pokemon_row: BeautifulSoup) -> list[int]:
        uncleaned_stats_ele = pokemon_row.find_all("td", class_="cell-num")[1:]
        return list(map(lambda x: int(x.text), uncleaned_stats_ele))

    def get_total_stats(self, pokemon_row: BeautifulSoup) -> int:
        return int(pokemon_row.find("td", class_="cell-total").text)

    def get_pokemon_data(self, pokemon_row: BeautifulSoup):
        num = self.get_number(pokemon_row)
        name = self.get_name(pokemon_row)
        types_ = self.get_types(pokemon_row)
        total_stats = self.get_total_stats(pokemon_row)
        stats = self.get_stats(pokemon_row)
        return num, name, types_, total_stats, stats
