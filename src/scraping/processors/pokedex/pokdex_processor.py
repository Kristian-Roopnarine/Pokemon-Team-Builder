from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class PokedexProcessor(ABC):
    @abstractmethod
    def get_name(self, pokemon_row: BeautifulSoup) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_number(self, pokemon_row: BeautifulSoup) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_types(self, pokemon_row: BeautifulSoup) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def get_total_stats(self, pokemon_row: BeautifulSoup) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_stats(self, pokemon_row: BeautifulSoup) -> list[int]:
        raise NotImplementedError

    @abstractmethod
    def get_pokemon_data(self, pokemon_row: BeautifulSoup):
        raise NotImplementedError
