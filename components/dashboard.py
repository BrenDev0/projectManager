from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Dashboard")

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)



