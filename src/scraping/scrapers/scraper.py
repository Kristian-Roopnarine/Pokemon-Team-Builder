from abc import ABC, abstractmethod
from bs4.element import ResultSet
from bs4 import BeautifulSoup


class Scraper(ABC):
    @abstractmethod
    def make_request(self, url) -> str:
        raise NotImplementedError

    @abstractmethod
    def set_page_source(self, raw_html: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_page_source(self):
        raise NotImplementedError
