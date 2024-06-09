from PySide6.QtWidgets import *
from models.database import Items

class ViewItem(QWidget):
    def __init__(self, item):
        super().__init__()

        self.item_db = Items()
        self.item = self.item_db.find(item)

        self.setWindowTitle(self.item[1])
        self.resize(500, 500)

        #content
        details = QGroupBox("Item Details")

        item_label = QLabel("Item:")
        item_name = QLabel(self.item[1])

        category_label = QLabel("Category:")
        item_category = QLabel(self.item[2])

        description_label = QLabel("Description:")
        item_description = QLabel(self.item[3])

        notes_label = QLabel("Notes:")
        self.item_notes = QTextEdit()
        self.item_notes.setPlainText(self.item[4])
        self.item_notes.textChanged.connect(self.show_save_button)

        #buttons
        self.save_button = QPushButton("Save") #slot on manage project file
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_window)
        


        #layouts 

        #item
        item_layout = QVBoxLayout()
        item_layout.addWidget(item_label)
        item_layout.addWidget(item_name)

        #category
        category_layout = QVBoxLayout()
        category_layout.addWidget(category_label)
        category_layout.addWidget(item_category)

        #description
        description_layout = QVBoxLayout()
        description_layout.addWidget(description_label)
        description_layout.addWidget(item_description)

        #notes
        notes_layout = QVBoxLayout()
        notes_layout.addWidget(notes_label)
        notes_layout.addWidget(self.item_notes)

        #buttons
        self.button_layout = QHBoxLayout()
        

        #details
        details_layout = QHBoxLayout()
        details_layout.addLayout(item_layout)
        details_layout.addLayout(category_layout)
        details_layout.addLayout(description_layout)

        details.setLayout(details_layout)


        #main
        layout = QVBoxLayout()
        layout.addWidget(details)
        layout.addLayout(notes_layout)
        layout.addLayout(self.button_layout)
        
        self.setLayout(layout)

    def show_save_button(self):
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.save_button)

    def close_window(self):
        self.hide()

        
        
            
        
        
