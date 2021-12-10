from bs4.element import ResultSet
import re
import pandas as pd

from ..._constants import PokemonDatabaseURL
from scraping.pokemon_db.total_pokedex.processor import PokdemonDBTotalPokedexProcessor
from scraping.pokemon_db.total_pokedex.scraper import PokemonDBTotalPokedexScraper
from models.pokemon import Pokemon

COLS = ["Number", "Name", "Type 1", "Type 2", "Total Stats"] + Pokemon.STATS_ORDER


def fill_pokemon_data_dict(poke_table: ResultSet):
    pokemon_data_dict = dict()
    poke_processor = PokdemonDBTotalPokedexProcessor()
    for pokemon_row in poke_table:
        poke_number = poke_processor.get_number(pokemon_row)
        poke_name = poke_processor.get_name(pokemon_row)
        poke_types = poke_processor.get_types(pokemon_row)
        poke_total_stats = poke_processor.get_total_stats(pokemon_row)
        hp, atk, defense, spatk, spdef, speed = poke_processor.get_stats(pokemon_row)

        pokemon: Pokemon = (
            Pokemon.create()
            .add_number(poke_number)
            .add_name(poke_name)
            .add_types(poke_types)
            .add_total(poke_total_stats)
            .add_hp(hp)
            .add_atk(atk)
            .add_def(defense)
            .add_spatk(spatk)
            .add_spdef(spdef)
            .add_speed(speed)
            .build()
        )

        pokemon_data_dict[pokemon.get_name()] = pokemon.get_info()
    return pokemon_data_dict


def main():
    total_pokedex_scraper = PokemonDBTotalPokedexScraper(
        PokemonDatabaseURL.TOTAL_POKEDEX
    )
    pokedex_table = total_pokedex_scraper.make_request().get_pokedex_table()
    total_pokemon_data = fill_pokemon_data_dict(pokedex_table)
    pokemon_df = pd.DataFrame.from_dict(
        total_pokemon_data, columns=COLS, orient="index"
    )
    pokemon_df.to_csv("test.csv", index=False)


if __name__ == "__main__":
    main()
