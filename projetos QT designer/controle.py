from PyQt5 import uic,QtWidgets
import mysql.connector

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked() :
        print("Categoria Informatica foi selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria eletronicos foi selecionada")     
    
    print("Codigo:" ,linha1)
    print("Descricao:" ,linha2)
    print("Preco:" ,linha3)



app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()