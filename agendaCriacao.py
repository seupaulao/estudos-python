import sqlite

connection = sqlite.connect("demo.db")

cur = connection.cursor()

sql = "create table contatos (id NUMBER, nome VARCHAR, fone VARCHAR)"

cur.execute(sql)

connection.commit()
