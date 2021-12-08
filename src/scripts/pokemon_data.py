from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

from ._constants import PokemonDatabaseURL
from scrapers.models.Pokemon import Pokemon
from scrapers.pokemon_db.pokedex_scraper import PokemonDBTotalPokedexScraper

COLS = ["Number", "Name", "Type 1", "Type 2", "Total Stats"] + Pokemon.STATS_ORDER


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
    total_pokdex_scraper = PokemonDBTotalPokedexScraper(
        PokemonDatabaseURL.TOTAL_POKEDEX
    )
    pokdex_table = total_pokdex_scraper.make_request().get_pokedex_table()
    total_pokemon_data = fill_pokemon_data_dict(pokdex_table)
    pokemon_df = pd.DataFrame.from_dict(
        total_pokemon_data, columns=COLS, orient="index"
    )
    pokemon_df.to_csv("test.csv", index=False)


if __name__ == "__main__":
    main()
