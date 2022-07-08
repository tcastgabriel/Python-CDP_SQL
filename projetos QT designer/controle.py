from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked() :
        print("Categoria Informatica foi selecionada")
        categoria ="Eletronicos"
    elif formulario.radioButton_2.isChecked() :
        print("Categoria eletronicos foi selecionada")
        categoria ="Informatica"     
    
    print("Codigo:" ,linha1)
    print("Descricao:" ,linha2)
    print("Preco:" ,linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()



app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()















#criando a tabela (MYSQL)

""" create table produtos (
    id INT NOT NULL AUTO_INCREMENT,
    codigo INT,
    descricao VARCHAR(50),
    preco DOUBLE,
    categoria VARCHAR(20),
    PRIMARY KEY (id)

); """


#INSERIR REGISTRO NA TABELA (SQL)
""" INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (123,"monitor",1000.00,"informatica"); """


#VER TABELA TERMINAL
""" select * from produtos; """





