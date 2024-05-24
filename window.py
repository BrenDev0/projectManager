from PySide6.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Manager")

        #menubar
        menu_bar  = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")


        #file menu options
        new_action = file_menu.addAction("New Project")
        save_action = file_menu.addAction("Save")
        save_as_action  = file_menu.addAction("Save as")

        #edit menu options
        