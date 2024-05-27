import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("Project_manager.db")
        self.cur =  self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXIST projects (
        projectid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date DATE,
        language TEXT,
        library TEXT                                                  
        )""") 
    
    def insert(self, project):
        self.cur.execute("""INSERT OR IGNORE INTO projects VALUES (?,?,?,?)""", project)
        self.conn.commit() 

    def delete(self, name):
        self.cur.execute("""DELETE FROM projects WHERE name = ?""", name)   
        self.conn.commit() 

    def read(self):
        self.cur.execute("""SELECT * FROM projects""")    
        row = self.cur.fetchall()
        print(row)


class Project:
    def __init__(self):
        self.conn = sqlite3.connect("project_manager.db")
        self.cur = self.conn.cursor() 
        self.create_table()  

    def create_table(self, id):
        self.cur.execute("""CREATE TABLE IF NOT EXIST ? (
        type TEXT,
        description, TEXT,
        phase TEXT,
        FOREIGNKEY(project) REFERENCES(projectid)   
                      
        )""", id)  

    def insert(self, name, data):
        self.cur.execute("""INSERT OR IGNORE INTO ?  VALUES (?,?,?,?)""", (name, data))  
        self.conn.commit()

    def read(self, table_name):
        self.cur.execute("""SELECT * FROM ?""", table_name) 
        row = self.cur.fetchall()
        print(row)    



