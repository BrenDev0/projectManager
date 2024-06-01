from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from models.database import Database

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.db = Database()
        
        
        
        #content

        #table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Language", "Stack"])

        #buttons
        button_refresh = QPushButton("Refresh")
        button_refresh.clicked.connect(self.load_data)
        

        #layouts
        
        
        #main
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(button_refresh)
        
        
        
        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        count = self.db.cur.execute("SELECT COUNT(*) FROM projects")
        self.table.setRowCount(count.fetchone()[0])
        projects = self.db.cur.execute("SELECT * FROM projects")
        row = 0
        
        for i in projects:
            self.table.setItem(row, 0, QTableWidgetItem(i[1]))
            self.table.setItem(row, 1, QTableWidgetItem(i[2]))
            self.table.setItem(row, 2, QTableWidgetItem(i[3]))
            row = row + 1
           

            



