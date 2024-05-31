from PySide6.QtWidgets import QWidget, QMenuBar, QVBoxLayout, QHBoxLayout, QStackedWidget
from models.database import Database, Project
from components.dashboard import Dashboard
from components.new_project import New_project


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Manager")
        self.content = QStackedWidget()

        # window content
        self.content.addWidget(Dashboard()) #0
        self.content.addWidget(New_project())#1

        

        #menubar 
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("file")
        edit_menu = menu_bar.addMenu("Edit")

        #file menu
        new_project = file_menu.addAction("New Project")
        new_project.triggered.connect(self.create_new_project)

        save_project = file_menu.addAction("Save")
        save_project.triggered.connect(self.save_data)

        save_as = file_menu.addAction("Save As")
        save_as.triggered.connect(self.save_data_as)

        #edit menu
        


        #layouts

        #main layout 
        layout = QVBoxLayout() 
        layout.addWidget(menu_bar)
        layout.addWidget(self.content)
        

        self.setLayout(layout)


    

    def create_new_project(self):
        self.content.setCurrentIndex(1)

    def save_data(self):
        print("save")

    def save_data_as(self):
        print("Save as")  
    
   
   
    


        
