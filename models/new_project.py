from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox, QRadioButton


class New_project(QWidget):
    def __init__(self):
        super().__init__()

        #content
        name_label = QLabel("Project Name: ")
        name_line_edit = QLineEdit()

        details = QGroupBox("Project Details")

        language_label = QLabel("Language: ")
        language_line_edit = QLineEdit()

        stack_label = QLabel("Stack: ")
        stack_line_edit = QLineEdit()
        

        #layouts
        #name
        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_line_edit) 

        #language
        language_layout = QHBoxLayout()
        language_layout.addWidget(language_label)
        language_layout.addWidget(language_line_edit)

         #stack
        stack_layout = QHBoxLayout()
        stack_layout.addWidget(stack_label)
        stack_layout.addWidget(stack_line_edit)

        #details
        details_layout = QVBoxLayout()
        details_layout.addLayout(language_layout)
        details_layout.addLayout(stack_layout)

        details.setLayout(details_layout)
        


        #main layout 
        layout = QVBoxLayout()
        layout.addLayout(name_layout)
        layout.addWidget(details)
        

        self.setLayout(layout)