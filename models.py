import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("Project_manager.db")
        self.cur =  self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXIST projects (
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

