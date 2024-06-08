from PySide6.QtWidgets import *
from models.database import Items

class ViewItem(QWidget):
    def __init__(self, item):
        super().__init__()

        self.item_db = Items()
        self.item = self.item_db.find(item)

        self.setWindowTitle(self.item[1])
        self.resize(500, 500)