from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout
from models.database import Database, Project


class Manager(QWidget):
    def __init__(self, projectid):
        super().__init__()

        
        self.project_details = Project()
        self.db = Database()
        self.project = self.db.get_project(projectid)

        
        #content 
        name_key = QLabel("Name:")
        self.name_value = QLabel(self.project[1])

        language_key = QLabel("Language:")
        self.language_value = QLabel(self.project[2])

        stack_key = QLabel("Stack:")
        self.stack_value = QLabel(self.project[3])


        
        
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
    

        self.setLayout(layout)

    
    