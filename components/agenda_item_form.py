from PySide6.QtWidgets import *


class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Item")

        #content

        #item edits
        self.item = QLabel("Item:")
        self.item_line_edit = QLineEdit()

        #category edits
        self.category = QLabel("Category:")
        self.select = QComboBox()
        self.select.setCurrentIndex(1)
        self.select.addItems(["Bug", "Feature", "Mile Stone"])

        #description
        description = QLabel("Description:")
        self.description_edit = QTextEdit()

        #notes
        notes = QLabel("Initial Notes:")
        self.notes_edit = QTextEdit()

        #Buttons 
        self.button_add_item = QPushButton("Add Item")


        #layouts 

        #item layout
        item_layout = QVBoxLayout()
        item_layout.addWidget(self.item)
        item_layout.addWidget(self.item_line_edit)

        #category layout
        category_layout = QVBoxLayout()
        category_layout.addWidget(self.category)
        category_layout.addWidget(self.select)

        #description
        description_layout = QVBoxLayout()
        description_layout.addWidget(description)
        description_layout.addWidget(self.description_edit)

        #notes
        notes_layout = QVBoxLayout()
        notes_layout.addWidget(notes)
        notes_layout.addWidget(self.notes_edit)

        #main layout 
        layout = QVBoxLayout()
        layout.addLayout(item_layout)
        layout.addLayout(category_layout)
        layout.addLayout(description_layout)
        layout.addLayout(notes_layout)
        layout.addWidget(self.button_add_item)


        self.setLayout(layout)

