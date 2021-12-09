from __future__ import annotations
from typing import List


class Pokemon:
    STATS_ORDER = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

    def __init__(self):
        self.number = None
        self.name = None
        self.types = None
        self.total = None
        self.hp = None
        self.atk = None
        self.defense = None
        self.sp_atk = None
        self.sp_def = None
        self.spd = None

    def get_stats(self):
        return [self.hp, self.atk, self.defense, self.sp_atk, self.sp_def, self.spd]

    def get_name(self):
        return self.name

    def get_info(self):
        return [
            self.number,
            self.name,
            self.types,
            self.total,
        ] + self.get_stats()

    def create(self) -> PokemonBuilder:
        return PokemonBuilder()

    def __str__(self):
        return f"#{self.number} {self.name} - {self.types} {self.get_stats()}"


class PokemonBuilder:
    def __init__(self, pokemon=Pokemon()):
        self.pokemon = pokemon

    def build(self) -> Pokemon:
        return self.pokemon

    def add_number(self, num: int) -> PokemonBuilder:
        self.pokemon.number = num
        return self

    def add_name(self, name: str) -> PokemonBuilder:
        self.pokemon.name = name
        return self

    def add_types(self, types: list[str]) -> PokemonBuilder:
        self.pokemon.types = types
        return self

    def add_total(self, total: int) -> PokemonBuilder:
        self.pokemon.total = total
        return self

    def add_hp(self, hp: int) -> PokemonBuilder:
        self.pokemon.hp = hp
        return self

    def add_atk(self, atk: int) -> PokemonBuilder:
        self.pokemon.atk = atk
        return self

    def add_def(self, defense: int) -> PokemonBuilder:
        self.pokemon.defense = defense

    def add_spatk(self, spatk: int) -> PokemonBuilder:
        self.pokemon.sp_atk = spatk
        return self

    def add_spdef(self, spdef: int) -> PokemonBuilder:
        self.pokemon.sp_def = spdef
        return self

    def add_speed(self, spd: int) -> PokemonBuilder:
        self.pokemon.speed = spd
        return self
