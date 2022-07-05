import sqlite3

banco = sqlite3.connect('Primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email text)")

""" cursor.execute("INSERT INTO pessoas VALUES('Carlos',32,'Carlos_moreira@gmail.com')") """

#banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())