from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_cadastroUsuario(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(591, 428)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(110, 80, 351, 301))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nome_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.nome_lineEdit.setGeometry(QtCore.QRect(80, 80, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome_lineEdit.setFont(font)
        self.nome_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nome_lineEdit.setText("")
        self.nome_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.email_lineEdit.setGeometry(QtCore.QRect(80, 110, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.username_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.username_lineEdit.setGeometry(QtCore.QRect(80, 140, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_lineEdit.setText("")
        self.username_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.password_lineEdit.setGeometry(QtCore.QRect(80, 170, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)  # Oculta a digitação da senha
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.cadastrar_Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_Button.setGeometry(QtCore.QRect(140, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_Button.setFont(font)
        self.cadastrar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.cadastrar_Button.setObjectName("cadastrar_Button")
        self.voltar_Button = QtWidgets.QPushButton(self.frame)
        self.voltar_Button.setGeometry(QtCore.QRect(140, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voltar_Button.setFont(font)
        self.voltar_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar_Button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.voltar_Button.setObjectName("voltar_Button")
        # self.id_usuario_lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        # self.id_usuario_lineEdit_2.setGeometry(QtCore.QRect(80, 50, 191, 20))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.id_usuario_lineEdit_2.setFont(font)
        # self.id_usuario_lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.id_usuario_lineEdit_2.setText("")
        # self.id_usuario_lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        # self.id_usuario_lineEdit_2.setObjectName("id_usuario_lineEdit_2")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(200, 50, 181, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.nome_lineEdit.setPlaceholderText(_translate("Cadastro", "Nome"))
        self.email_lineEdit.setPlaceholderText(_translate("Cadastro", "Email"))
        self.username_lineEdit.setPlaceholderText(_translate("Cadastro", "Username"))
        self.password_lineEdit.setPlaceholderText(_translate("Cadastro", "Password"))
        self.cadastrar_Button.setText(_translate("Cadastro", "Cadastrar"))
        self.voltar_Button.setText(_translate("Cadastro", "Voltar"))
        # self.id_usuario_lineEdit_2.setPlaceholderText(_translate("Cadastro", "id_usuario"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">CADASTRE-SE, USUARIO</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_cadastroUsuario()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())
