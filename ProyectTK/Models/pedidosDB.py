import sqlite3

class DataPedidos:

	def __init__(self):

		self.conn = sqlite3.connect('basedata.db')
		self.cursor = self.conn.cursor()

	def insertItems(self, code, name, supp, price, cant):
		sql = "INSERT INTO pedidos (naservil, naclient, product, descript, phone ) VALUES(?,?,?,?,?)"
		params = (code, name, price, supp, cant)
		self.cursor.execute(sql, params)
		self.conn.commit()

	def returnOneItem(self, ejm):
		sql = "SELECT * FROM pedidos WHERE naclient = '{}'".format(ejm)
		self.cursor.execute(sql)
		return self.cursor.fetchone()

	def returnAllElements(self):
		sql = "SELECT * FROM pedidos ORDER BY id"
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	def delete(self, ejm):
		sql = "DELETE FROM pedidos WHERE naclient = '{}'".format(ejm)
		self.cursor.execute(sql)
		self.conn.commit()

	def updateItem(self, elem, pls):
		sql = "UPDATE pedidos SET naservil ='{}', naclient='{}', product='{}', descript='{}', phone='{}' WHERE naclient = '{}'".format(elem[0], elem[1], elem[2], elem[3], elem[4], pls)
		self.cursor.execute(sql)
		self.conn.commit()