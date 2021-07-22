import sqlite3

class Data:

	def __init__(self):

		self.conn = sqlite3.connect('basedata.db')
		self.cursor = self.conn.cursor()

	def insertItems(self, code, name, supp, price, cant):
		sql = "INSERT INTO productosre (code, name, price, supp, cant ) VALUES(?,?,?,?,?)"
		params = (code, name, price, supp, cant)
		self.cursor.execute(sql, params)
		self.conn.commit()

	def returnOneItem(self, ejm):
		sql = "SELECT * FROM productosre WHERE name = '{}'".format(ejm)
		self.cursor.execute(sql)
		return self.cursor.fetchone()

	def returnAllElements(self):
		sql = "SELECT * FROM productosre ORDER BY price"
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	def delete(self, ejm):
		sql = "DELETE FROM productosre WHERE name = '{}'".format(ejm)
		self.cursor.execute(sql)
		self.conn.commit()

	def updateItem(self, elem, pls):
		sql = "UPDATE productosre SET code ='{}', name='{}', supp='{}', price='{}', cant='{}' WHERE name = '{}'".format(elem[0], elem[1], elem[2], elem[3], elem[4], pls)
		self.cursor.execute(sql)
		self.conn.commit()