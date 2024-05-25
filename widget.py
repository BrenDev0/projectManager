from PySide6.QtWidgets import QWidget, QMenuBar, QVBoxLayout
import sqlite3

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Manager")

        #menubar 
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("file")
        edit_menu = menu_bar.addMenu("Edit")

        #file menu
        new_project = file_menu.addAction("New Project")
        new_project.triggered.connect(self.create_new_project)

        save_project = file_menu.addAction("Save")
        save_project.triggered.connect(self.save_data)

        #edit menu
        


        

        #layouts

        #main layout 
        layout = QVBoxLayout() 
        layout.addWidget(menu_bar)

        self.setLayout(layout)


    
    def create_connection(self):
        self.connection = sqlite3.connect("Project Manager")
        return self.connection

    def create_new_project(self):
        print("New Project")  

    def save_data(self):
        print("Save")
    
   
   
    


        
