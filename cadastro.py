from PyQt5 import uic, QtWidgets
import mysql.connector
import datetime


#Define o Banco de Dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)


def funcao_principal():
    nome = cadastro.lineEdit.text()
    if nome == "":
        # Exibe mensagem de erro para o campo "Nome"
        cadastro.lineEdit.setStyleSheet("background-color: red;")
        return
    
    cpf = cadastro.lineEdit_2.text()
    if cpf == "":
        # Exibe mensagem de erro para o campo "CPF"
        cadastro.lineEdit_2.setStyleSheet("background-color: red;")
        return

    datanascimento = cadastro.lineEdit_5.text()
    if datanascimento == "":
        # Exibe mensagem de erro para o campo "Data de Nascimento"
        cadastro.lineEdit_5.setStyleSheet("background-color: red;")
        return
    data_nascimento = datetime.datetime.strptime(datanascimento, "%d/%m/%Y").strftime("%Y-%m-%d")
    email = cadastro.lineEdit_3.text()
    telefone = cadastro.lineEdit_4.text()

#Retorna os dados inseridos
    print("Nome", nome)
    print("CPF", cpf)
    print("Data de Nascimento", datanascimento)
    print("Email", email)
    print("Telefone", telefone)

    if cadastro.radioButton.isChecked() :
        print("F")
    elif cadastro.radioButton_2.isChecked() :
        print("M")
    else :
        print("O")
    sexos = {
    cadastro.radioButton.isChecked(): "M",
    cadastro.radioButton_2.isChecked(): "F",
    cadastro.radioButton_3.isChecked(): "O",
    }
    sexo = sexos[True]
#Insere no Banco de Dados
    cursor = banco.cursor()
    query = """
    INSERT INTO `clientes` (`cpf`,`nome`,`datanascimento`,`email`,`telefone`,`sexo`)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (cpf, nome, data_nascimento, email, telefone, sexo))
    banco.commit()

    cursor.close()
    banco.close()

    

# Limpa os campos de texto
    cadastro.lineEdit.clear()
    cadastro.lineEdit_2.clear()
    cadastro.lineEdit_3.clear()
    cadastro.lineEdit_4.clear()
    cadastro.lineEdit_5.clear()


app=QtWidgets.QApplication([])
cadastro=uic.loadUi("cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)
cadastro.show()
app.exec()
