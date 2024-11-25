from Barbora_Find_Item import Barbora_Find_Item
from Data_base import DB


class Barbora_item():

    def __init__(self, driver):
        self.driver = driver

    def save(self):
        self.db = DB()
        query = (f"INSERT INTO `start_info` (`id`, `title`, `quantity`) VALUES (%s, %s, %s)")
        self.db.conn.cursor().execute(query, (0, self.title, self.size))
        self.db.conn.commit()
        self.db.close()

    def fill(self):
        bip = Barbora_Find_Item(self.driver)
        self.title = bip.get_title()
        self.size = bip.get_size()