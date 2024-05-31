from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox, QPushButton



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

        button_submit = QPushButton("Submit")
        button_submit.clicked.connect(self.submit)

        button_back = QPushButton("Back")
        button_back.clicked.connect(self.back)
        

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

        #buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_back)
        button_layout.addWidget(button_submit)

        #details
        details_layout = QVBoxLayout()
        details_layout.addLayout(name_layout)
        details_layout.addLayout(language_layout)
        details_layout.addLayout(stack_layout)

        details.setLayout(details_layout)
        


        #main layout 
        layout = QVBoxLayout()
        layout.addWidget(details)
        layout.addLayout(button_layout)
        

        self.setLayout(layout)

    def submit(self):
        pass

    def back(self):
        pass