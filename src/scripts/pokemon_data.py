from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

from ._constants import PokemonDatabaseURL
from ..scrapers.models.Pokemon import Pokemon

COLS = ["Number", "Name", "Type 1", "Type 2", "Total Stats"] + Pokemon.STATS_ORDER


def get_total_pokedex_html() -> str:
    r = requests.get(url=PokemonDatabaseURL.TOTAL_POKEDEX)
    html_text = r.text
    return html_text


def get_table(soup):
    return soup.table.tbody.find_all("tr")


def fill_pokemon_data_dict(poke_table):
    pokemon_data_dict = dict()

    for pokemon_row in poke_table:
        uncleaned_name_ele = pokemon_row.find(attrs={"data-alt": re.compile("icon")})[
            "data-alt"
        ]
        uncleaned_stats_ele = pokemon_row.find_all("td", class_="cell-num")[1:]
        uncleaned_type_ele = pokemon_row.find_all("a", class_="type-icon")

        pokemon_number = int(
            pokemon_row.find("td", class_="cell-fixed")["data-sort-value"]
        )
        pokemon_stat_total = int(pokemon_row.find("td", class_="cell-total").text)

        cleaned_types = list(map(lambda x: x.text, uncleaned_type_ele))
        cleaned_pokemon_stats = list(map(lambda x: int(x.text), uncleaned_stats_ele))

        if len(cleaned_types) < 2:
            cleaned_types.append(None)

        curr_pokemon = Pokemon(
            number=pokemon_number,
            name=uncleaned_name_ele,
            types=cleaned_types,
            total=pokemon_stat_total,
            hp=cleaned_pokemon_stats[0],
            atk=cleaned_pokemon_stats[1],
            defense=cleaned_pokemon_stats[2],
            sp_atk=cleaned_pokemon_stats[3],
            sp_def=cleaned_pokemon_stats[4],
            spd=cleaned_pokemon_stats[5],
        )
        pokemon_data_dict[curr_pokemon.get_name()] = curr_pokemon.get_info()

    return pokemon_data_dict


def main():
    text = get_total_pokedex_html()
    pokedex_soup = BeautifulSoup(text, "html.parser")
    pokemon_table = get_table(pokedex_soup)
    pokedex = fill_pokemon_data_dict(pokemon_table)
    pokemon_df = pd.DataFrame.from_dict(pokedex, columns=COLS, orient="index")
    pokemon_df.to_csv("test.csv", index=False)


if __name__ == "__main__":
    main()
