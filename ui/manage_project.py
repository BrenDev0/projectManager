from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from models.database import Database, Items
from ui.agenda_item_form import Form
from ui.view_item import ViewItem


class Manager(QWidget):
    def __init__(self, projectid):
        super().__init__()

        
        self.items_db = Items()
        self.db = Database()
        self.project_details = self.db.get_project(projectid)
        self.new_item = Form()
        
        self.connections()
        


        
        #content 
        

        #details
        name_key = QLabel("Project:")
        self.name_value = QLabel(self.project_details[1])

        language_key = QLabel("Language:")
        self.language_value = QLabel(self.project_details[2])

        stack_key = QLabel("Stack:")
        self.stack_value = QLabel(self.project_details[3])

        #Tables

        #agenda table
        agenda_table_label = QLabel("Project Agenda")
        self.agenda_table = QTableWidget()
        self.agenda_table.setColumnCount(4)
        self.agenda_table.setHorizontalHeaderLabels(["id", "Item", "Category", "Description"])
        self.agenda_table.horizontalHeader().setStretchLastSection(True)
        self.agenda_table.hideColumn(0)
        self.agenda_table.itemSelectionChanged.connect(self.select_row)
        

        #history table
        history_table_label = QLabel("Project History")
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(4)
        self.history_table.setHorizontalHeaderLabels(["id", "Item", "Category", "Description"])
        self.history_table.horizontalHeader().setStretchLastSection(True)
        self.history_table.hideColumn(0)
        
        #buttons
        add_item_button = QPushButton("Add")
        add_item_button.clicked.connect(self.new_agenda_item)

        delete_item_button = QPushButton("Delete")
        delete_item_button.clicked.connect(self.delete_item)

        view_item_button = QPushButton("View")
        view_item_button.clicked.connect(self.view_item)

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

        #tables layout
        agenda_layout = QVBoxLayout()
        agenda_layout.addWidget(agenda_table_label)
        agenda_layout.addWidget(self.agenda_table)

        history_layout = QVBoxLayout()
        history_layout.addWidget(history_table_label)
        history_layout.addWidget(self.history_table)

        #tables button layouts
        action_buttons_layout = QHBoxLayout()
        action_buttons_layout.addWidget(add_item_button)
        action_buttons_layout.addWidget(delete_item_button)
        action_buttons_layout.addWidget(view_item_button)

        #details layout
        project_details_layout = QHBoxLayout()
        project_details_layout.addLayout(name_layout)
        project_details_layout.addLayout(language_layout)
        project_details_layout.addLayout(stack_layout)

        details.setLayout(project_details_layout)

        #main layout
        layout = QVBoxLayout()
        layout.addWidget(details)
        layout.addLayout(agenda_layout)
        layout.addLayout(action_buttons_layout)
        layout.addLayout(history_layout)
        
    

        self.setLayout(layout)
        self.load_data()
        
    #connections 
    def connections(self):
         self.new_item.button_add_item.clicked.connect(self.add_item)
         

    def new_agenda_item(self):
            self.new_item.show()

    def load_data(self):
        count = self.items_db.read(str(self.project_details[0]))
        self.agenda_table.setRowCount(len(count))
        items = self.items_db.read(str(self.project_details[0]))        

        row = 0
        for i in items:
              self.agenda_table.setItem(row, 0, QTableWidgetItem(str(i[0])))
              self.agenda_table.setItem(row, 1, QTableWidgetItem(i[1]))
              self.agenda_table.setItem(row, 2, QTableWidgetItem(i[2]))
              self.agenda_table.setItem(row, 3, QTableWidgetItem(i[3]))
              row = row + 1     

    def select_row(self):
         row = self.agenda_table.currentRow()  
         self.agenda_table.selectRow(row)  

    def add_item(self):
         print("entered")
         item = [
              self.new_item.item_line_edit.text(),
              self.new_item.select.currentText(),
              self.new_item.description_edit.toPlainText(),
              self.new_item.notes_edit.toPlainText(),
              self.project_details[0]
         ]
         print(item)
         self.new_item.hide() 
         self.items_db.insert(item) 
         self.load_data()   

    def view_item(self):
         item = self.agenda_table.item(self.agenda_table.currentRow(), 0).text()
         self.view = ViewItem(item)
         self.view.show()
         self.view.save_button.clicked.connect(self.save_notes)

    def delete_item(self):
         itemid = self.agenda_table.item(self.agenda_table.currentRow(), 0).text()
         self.items_db.delete(itemid)
         self.load_data()

    def save_notes(self):
         itemid = self.agenda_table.item(self.agenda_table.currentRow(), 0).text()
         notes = self.view.item_notes.toPlainText()
         self.items_db.update_notes(notes, itemid)
         self.view.hide()

         
         



    
    