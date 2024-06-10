from PySide6.QtWidgets import *
from PySide6.QtCore import *
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
        self.item_name = QLabel(self.item[1])
        self.item_line_edit = QLineEdit(self.item[1])
        

        category_label = QLabel("Category:")
        self.item_category = QLabel(self.item[2])
        self.category_line_edit = QLineEdit(self.item[2])

        description_label = QLabel("Description:")
        self.item_description = QLabel(self.item[3])
        self.description_line_edit = QLineEdit(self.item[3])

        notes_label = QLabel("Notes:")
        self.item_notes = QTextEdit()
        self.item_notes.setPlainText(self.item[4])
        self.item_notes.textChanged.connect(self.show_save_button)

        #buttons
        self.save_button = QPushButton("Save") #slot on manage project file
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_window)
        button_edit_details = QPushButton("Edit")
        button_edit_details.clicked.connect(self.edit_details)
        


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
        layout.addWidget(button_edit_details, alignment=Qt.AlignRight)
        layout.addLayout(notes_layout)
        layout.addLayout(self.button_layout)
        
        self.setLayout(layout)

    def show_save_button(self):
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.save_button)

    def close_window(self):
        self.hide()

    def edit_details(self):
        self.item_layout.replaceWidget(self.item_name, self.item_line_edit)

        self.category_layout.replaceWidget(self.item_category, self.category_line_edit)

        self.description_layout.replaceWidget(self.item_description, self.description_line_edit)       
        


        
        
            
        
        
