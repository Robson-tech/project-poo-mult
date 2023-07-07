from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(483, 447)
        Login.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(80, 130, 321, 221))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cpf_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cpf_lineEdit.setGeometry(QtCore.QRect(70, 40, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cpf_lineEdit.setFont(font)
        self.cpf_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.cpf_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.cpf_lineEdit.setReadOnly(False)
        self.cpf_lineEdit.setObjectName("cpf_lineEdit")
        self.senha_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.senha_lineEdit.setGeometry(QtCore.QRect(70, 70, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.senha_lineEdit.setFont(font)
        self.senha_lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.senha_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.senha_lineEdit.setObjectName("senha_lineEdit")
        self.login_Button = QtWidgets.QPushButton(self.frame)
        self.login_Button.setGeometry(QtCore.QRect(70, 110, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.login_Button.setFont(font)
        self.login_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_Button.setStyleSheet("QPushButton{\n"
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
        self.login_Button.setObjectName("login_Button")
        self.nova_conta_Button = QtWidgets.QPushButton(self.frame)
        self.nova_conta_Button.setGeometry(QtCore.QRect(70, 140, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nova_conta_Button.setFont(font)
        self.nova_conta_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nova_conta_Button.setStyleSheet("QPushButton{\n"
                                              "\n"
                                              "    color: rgb(0, 0, 0);\n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              "    border-radius:10px\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    background-color: rgb(0, 0, 0);\n"
                                              "}")
        self.nova_conta_Button.setObjectName("nova_conta_Button")
        self.sair_login_Button = QtWidgets.QPushButton(self.frame)
        self.sair_login_Button.setGeometry(QtCore.QRect(70, 170, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sair_login_Button.setFont(font)
        self.sair_login_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sair_login_Button.setStyleSheet("QPushButton{\n"
                                              "\n"
                                              "    color: rgb(0, 0, 0);\n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              "    border-radius:10px\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    background-color: rgb(0, 0, 0);\n"
                                              "}")
        self.sair_login_Button.setObjectName("sair_login_Button")
        self.senha_lineEdit.raise_()
        self.cpf_lineEdit.raise_()
        self.login_Button.raise_()
        self.nova_conta_Button.raise_()
        self.sair_login_Button.raise_()
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(200, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.cpf_lineEdit, self.senha_lineEdit)
        Login.setTabOrder(self.senha_lineEdit, self.login_Button)
        Login.setTabOrder(self.login_Button, self.nova_conta_Button)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.cpf_lineEdit.setToolTip(_translate("Login", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.cpf_lineEdit.setPlaceholderText(_translate("Login", "username"))
        self.senha_lineEdit.setToolTip(_translate("Login", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.senha_lineEdit.setPlaceholderText(_translate("Login", "Senha"))
        self.login_Button.setText(_translate("Login", "Login"))
        self.nova_conta_Button.setText(_translate("Login", "Criar Conta"))
        self.sair_login_Button.setText(_translate("Login", "Sair"))
        self.label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">LOGIN</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Tela_login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())