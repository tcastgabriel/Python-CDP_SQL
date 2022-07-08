import sqlite3

nome = "Carlos"
idade = 38
email = "Carlos_Sa@gmail.com"

banco = sqlite3.connect('Primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade interger, email text)")

""" cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"',"+str(idade)+",'"+email+"')") """

cursor.execute("UPDATE pessoas SET idade = '23' WHERE idade = 25")

banco.commit()

""" cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) """