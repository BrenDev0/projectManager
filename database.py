from PySide6.QtWidgets import QWidget
import sqlite3

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTItle("Project Manager")


    
    def create_connection(self):
        self.connection = sqlite3.connect("Project Manager")
        return self.connection
    
   
    


        
