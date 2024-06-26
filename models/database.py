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
        self.cur.execute("DELETE FROM projects WHERE projectid = ?", name)   
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
        status TEXT,
        item TEXT,
        category TEXT,
        description TEXT,
        notes TEXT,
        project INTEGER,
        FOREIGN KEY (project)  REFERENCES projects (projectid)              
        )""")  
    
    

    def insert(self, data):
        self.cur.execute("""INSERT OR IGNORE INTO items (status, item, category, description, notes, project)  VALUES (?,?,?,?,?,?)""", data)  
        self.conn.commit()

    def read_active(self, projectid):
        self.cur.execute("""SELECT * FROM items WHERE project = ? AND status = 'active'""", projectid) 
        row = self.cur.fetchall()
        return row 

    def read_completed(self, projectid):
        self.cur.execute("""SELECT * FROM items WHERE project = ? AND status = 'completed'""", projectid) 
        row = self.cur.fetchall()
        return row         

    def delete(self, id):
        self.cur.execute("DELETE FROM items WHERE itemid = ?", id)
        self.conn.commit()

    def find(self, id):
        item = self.cur.execute("SELECT * FROM items WHERE itemid = ?", id)
        return item.fetchone()

    def update_notes(self, data, id):
        self.cur.execute("UPDATE items SET notes = ? WHERE itemid = ? ", (data, id))
        self.conn.commit()

    def mark_completed(self, id):
        self.cur.execute("UPDATE items SET status = 'completed' WHERE itemid = ?", id)
        self.conn.commit()
        



