from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox
from models.database import Database, Project


class Manager(QWidget):
    def __init__(self, project):
        super().__init__()

        self.project = Project()
        self.db = Database()

        
        #content 
        
        
        #group 
        details = QGroupBox("Project Details")



        #layouts

        #main layout
        layout = QVBoxLayout()
    

        self.setLayout(layout)
    