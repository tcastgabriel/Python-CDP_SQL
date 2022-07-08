import sqlite3

try:


   banco = sqlite3.connect('Primeiro_banco.db')

   cursor = banco.cursor()

   cursor.execute("DELETE from pessoas WHERE idade = 32")

   banco.commit()
   banco.close()
   print("Os dados foram deletados com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao tentar excluir!" ,erro)