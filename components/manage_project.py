from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout, QTableWidget, QPushButton
from models.database import Database, Project
from components.agenda_item_form import Form


class Manager(QWidget):
    def __init__(self, projectid):
        super().__init__()

        
        self.project_details = Project()
        self.db = Database()
        self.project = self.db.get_project(projectid)
        self.new_item = Form()
        self.connections()


        
        #content 

        #details
        name_key = QLabel("Project:")
        self.name_value = QLabel(self.project[1])

        language_key = QLabel("Language:")
        self.language_value = QLabel(self.project[2])

        stack_key = QLabel("Stack:")
        self.stack_value = QLabel(self.project[3])

        #Tables

        #agenda table
        agenda_table = QTableWidget()
        agenda_table.setColumnCount(3)
        agenda_table.setHorizontalHeaderLabels(["Item", "Category", "Initial Date"])

        #history table
        history_table = QTableWidget()
        history_table.setColumnCount(3)
        history_table.setHorizontalHeaderLabels(["Item", "Category", "Completion Date"])

        #buttons
        add_item_button = QPushButton("Add Item")
        add_item_button.clicked.connect(self.new_agenda_item)



        
        
        #group 
        details = QGroupBox("Project Details")



        #layouts
        #name layout
        name_layout = QVBoxLayout()
        name_layout.addWidget(name_key)
        name_layout.addWidget(self.name_value)

        #language layout 
        language_layout = QVBoxLayout()
        language_layout.addWidget(language_key)
        language_layout.addWidget(self.language_value)

        #stack layout 
        stack_layout = QVBoxLayout()
        stack_layout.addWidget(stack_key)
        stack_layout.addWidget(self.stack_value)

        #details layout
        project_details_layout = QHBoxLayout()
        project_details_layout.addLayout(name_layout)
        project_details_layout.addLayout(language_layout)
        project_details_layout.addLayout(stack_layout)

        details.setLayout(project_details_layout)

        #main layout
        layout = QVBoxLayout()
        layout.addWidget(details)
        layout.addWidget(agenda_table)
        layout.addWidget(history_table)
        layout.addWidget(add_item_button)
    

        self.setLayout(layout)
    #connections 
    def connections(self):
         self.new_item.button_add_item.clicked.connect(self.add_item)

    def new_agenda_item(self):
            self.new_item.show()

    def add_item(self):
         self.new_item.hide()        

    
    