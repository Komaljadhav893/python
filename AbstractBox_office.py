# AbstractBox_office.py
from abc import ABC, abstractmethod

class AbstractBox_office(ABC):
    @abstractmethod
    def create_items(self, film_id, theater_id, earnings):
        pass

    @abstractmethod
    def read_items(self, film_id=None, theater_id=None):
        pass

    @abstractmethod
    def update_items(self, film_id, theater_id, new_earnings):
        pass

    @abstractmethod
    def delete_items(self, film_id, theater_id):
        pass