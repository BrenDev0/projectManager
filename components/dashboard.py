from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        
        
        #headers
        project_name = QLabel("Name")
        project_language = QLabel("Language")
        project_stack = QLabel("Stack")


        #layouts
        
        #table head
        head_layout = QHBoxLayout()
        head_layout.addWidget(project_name)
        head_layout.addWidget(project_language)
        head_layout.addWidget(project_stack)
        #main
        layout = QVBoxLayout()
        layout.addLayout(head_layout)
        

        self.setLayout(layout)



