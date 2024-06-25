from PySide6.QtWidgets import QWidget, QMenuBar, QVBoxLayout, QHBoxLayout, QStackedWidget
from ui.dashboard import Dashboard
from ui.new_project import New_project
from ui.manage_project import Manager


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Manager")
        self.resize(500, 500)
        self.content = QStackedWidget()
        self.dashboard = Dashboard()
        self.new_project = New_project()
        self.connections()
        
        

        # window content
        self.content.addWidget(self.dashboard) #0
        self.content.addWidget(self.new_project) #1
    

        

        #menubar 
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("file")
        edit_menu = menu_bar.addMenu("Edit")

        #file menu
        new_project = file_menu.addAction("New Project")
        new_project.triggered.connect(self.page_create_new_project)

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


    

    def page_create_new_project(self):
       self.content.setCurrentIndex(1)

    def save_data(self):
        print("save")

    def save_data_as(self):
        print("Save as")  

    def connections(self):
        self.new_project.button_dashboard.clicked.connect(self.page_dashboard)
        self.dashboard.button_manage.clicked.connect(self.page_manage)
        
    #function for button_dashboard on new project page
    def page_dashboard(self):
        self.content.setCurrentIndex(0) 
        self.dashboard.load_data() 
        if self.content.count() == 3:
            self.content.removeWidget(self.project)
        else:
            pass    

    # function for button_manage on dashboard
    def page_manage(self):
        id = self.dashboard.table.item(self.dashboard.table.currentRow(), 0).text()
        self.project = Manager(id)
        self.content.addWidget(self.project)
        self.content.setCurrentIndex(2)
        
        
             
    
   
    
   
   
    


        
