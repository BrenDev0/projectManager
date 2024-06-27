from PySide6.QtWidgets import *
from PySide6.QtCore import *
from models.database import Items

class ViewItem(QWidget):
    def __init__(self, item):
        super().__init__()

        self.item_db = Items()
        self.item = self.item_db.find(item)

        self.setWindowTitle(self.item[2])
        self.resize(500, 500)

        #content
        details = QGroupBox("Item Details")

        item_label = QLabel("Item:")
        self.item_name = QLabel(self.item[2])
        self.item_line_edit = QLineEdit(self.item[2])
        
        category_label = QLabel("Category:")
        self.item_category = QLabel(self.item[3])
        self.category_select = QComboBox()
        self.category_select.addItems(["Bug", "Feature", "MileStone"])

        description_label = QLabel("Description:")
        self.item_description = QLabel(self.item[4])
        self.description_line_edit = QLineEdit(self.item[4])

        notes_label = QLabel("Notes:")
        self.item_notes = QTextEdit()
        self.item_notes.setPlainText(self.item[5])
        self.item_notes.textChanged.connect(self.show_save_button)

        #buttons
        self.save_button = QPushButton("Save") #slot on manage project file
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_window)
        
        


        #layouts 

        #item
        self.item_layout = QVBoxLayout()
        self.item_layout.addWidget(item_label)
        self.item_layout.addWidget(self.item_name)
       

        #category
        self.category_layout = QVBoxLayout()
        self.category_layout.addWidget(category_label)
        self.category_layout.addWidget(self.item_category)
       

        #description
        self.description_layout = QVBoxLayout()
        self.description_layout.addWidget(description_label)
        self.description_layout.addWidget(self.item_description)
    

        #notes
        notes_layout = QVBoxLayout()
        notes_layout.addWidget(notes_label)
        notes_layout.addWidget(self.item_notes)

        #buttons
        self.button_layout = QHBoxLayout()
        

        #details
        details_layout = QHBoxLayout()
        details_layout.addLayout(self.item_layout)
        details_layout.addLayout(self.category_layout)
        details_layout.addLayout(self.description_layout)
        

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

   

        
        
            
        
        
