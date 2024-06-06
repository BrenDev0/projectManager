import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("Project_Manager.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cur =  self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS projects (
        projectid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        language TEXT,
        stack TEXT                                                  
        )""") 
    
    def insert(self, project):
        project = self.cur.execute("""INSERT OR IGNORE INTO projects (name, language, stack) VALUES (?,?,?)""", project)
        self.conn.commit() 
        
    def delete(self, name):
        self.cur.execute("DELETE FROM projects WHERE name = ?", name)   
        self.conn.commit() 

    def read(self):
        self.cur.execute("SELECT * FROM projects")    
        row = self.cur.fetchall()
        return row

    def get_project(self, id):
       project = self.cur.execute("SELECT * FROM projects WHERE projectid = ?", id)
       return project.fetchone() 
      


class Items:
    def __init__(self):
        self.conn = sqlite3.connect("Project_Manager.db")
        self.conn.execute("PRAGMA foreign_key = ON")
        self.cur = self.conn.cursor() 
        self.create_table()
         
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS items (
        itemid INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        category TEXT,
        description TEXT,
        notes TEXT,
        project INTEGER,
        FOREIGN KEY (project)  REFERENCES projects (projectid)              
        )""")  
    
    

    def insert(self, data):
        self.cur.execute("""INSERT OR IGNORE INTO items (item, category, description, notes, project)  VALUES (?,?,?,?,?)""", data)  
        self.conn.commit()

    def read(self, projectid):
        self.cur.execute("""SELECT * FROM items WHERE project = ?""", projectid) 
        row = self.cur.fetchall()
        return row   





        



