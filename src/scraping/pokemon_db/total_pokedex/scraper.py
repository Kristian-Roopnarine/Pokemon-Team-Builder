from __future__ import annotations
from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests

from base.scrapers.scraper import Scraper


class PokemonDBTotalPokedexScraper(Scraper):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.page_source = None

    def make_request(self) -> PokemonDBTotalPokedexScraper:
        r = requests.get(url=self.url)
        self.set_page_source(r.text)
        return self

    def set_page_source(self, raw_html: str) -> None:
        self.page_source = BeautifulSoup(raw_html, "html.parser")

    def get_page_source(self):
        return self.page_source

    def get_pokedex_table(self) -> ResultSet:
        return self.get_page_source().table.tbody.find_all("tr")
