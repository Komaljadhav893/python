# box_office.py
from AbstractBox_office import AbstractBox_office

class Box_office(AbstractBox_office):
    def __init__(self):
        self.data = []

    def create_items(self, film_id, theater_id, earnings):
        self.data.append({'film_id': film_id, 'theater_id': theater_id, 'earnings': earnings})

    def read_items(self, film_id=None, theater_id=None):
        if film_id:
            return [items for items in self.data if items['film_id'] == film_id]
        elif theater_id:
            return [items for items in self.data if items['theater_id'] == theater_id]
        else:
            return self.data

    def update_items(self, film_id, theater_id, new_earnings):
        for items in self.data:
            if items['film_id'] == film_id and items['theater_id'] == theater_id:
                items['earnings'] = new_earnings

    def delete_items(self, film_id, theater_id):
        self.data = [items for items in self.data if not (items['film_id'] == film_id and items['theater_id'] == theater_id)]