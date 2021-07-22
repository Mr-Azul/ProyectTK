import sqlite3

class DataLogin:

    def __init__(self):

        self.conn = sqlite3.connect('basedata.db')
        self.cursor = self.conn.cursor()

    def insertItems(self, name, surname, user, password):
        sql = "INSERT INTO usuarios (name, surname, user, password) VALUES(?,?,?,?)"
        params = (name, surname, user, password)
        self.cursor.execute(sql, params)
        self.conn.commit()
    
    def loginValidate(self, user, password):
        sql = "SELECT * FROM usuarios WHERE user = ? AND password = ?"
        params = (user, password)   
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()