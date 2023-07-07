from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_inicial(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(625, 476)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(140, 90, 341, 291))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cadastrar_telainicial__Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_telainicial__Button.setGeometry(QtCore.QRect(90, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_telainicial__Button.setFont(font)
        self.cadastrar_telainicial__Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_telainicial__Button.setStyleSheet("QPushButton{\n"
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
        self.cadastrar_telainicial__Button.setObjectName("cadastrar_telainicial__Button")
        self.cadastrar_usuario_telainicial_Button_2 = QtWidgets.QPushButton(self.frame)
        self.cadastrar_usuario_telainicial_Button_2.setGeometry(QtCore.QRect(90, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cadastrar_usuario_telainicial_Button_2.setFont(font)
        self.cadastrar_usuario_telainicial_Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastrar_usuario_telainicial_Button_2.setStyleSheet("QPushButton{\n"
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
        self.cadastrar_usuario_telainicial_Button_2.setObjectName("cadastrar_usuario_telainicial_Button_2")
        self.buscar_tarefa_telainicial_Button = QtWidgets.QPushButton(self.frame)
        self.buscar_tarefa_telainicial_Button.setGeometry(QtCore.QRect(90, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buscar_tarefa_telainicial_Button.setFont(font)
        self.buscar_tarefa_telainicial_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscar_tarefa_telainicial_Button.setStyleSheet("QPushButton{\n"
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
        self.buscar_tarefa_telainicial_Button.setObjectName("buscar_tarefa_telainicial_Button")
        self.buscar_tarefa_telainicial_Button_2 = QtWidgets.QPushButton(self.frame)
        self.buscar_tarefa_telainicial_Button_2.setGeometry(QtCore.QRect(90, 190, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buscar_tarefa_telainicial_Button_2.setFont(font)
        self.buscar_tarefa_telainicial_Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscar_tarefa_telainicial_Button_2.setStyleSheet("QPushButton{\n"
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
        self.buscar_tarefa_telainicial_Button_2.setObjectName("buscar_tarefa_telainicial_Button_2")
        self.sair_telainicial_Button_5 = QtWidgets.QPushButton(self.frame)
        self.sair_telainicial_Button_5.setGeometry(QtCore.QRect(130, 240, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sair_telainicial_Button_5.setFont(font)
        self.sair_telainicial_Button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sair_telainicial_Button_5.setStyleSheet("QPushButton{\n"
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
        self.sair_telainicial_Button_5.setObjectName("sair_telainicial_Button_5")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(200, 25, 221, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.cadastrar_telainicial__Button.setText(_translate("Cadastro", "Cadastrar Tarefa"))
        self.cadastrar_usuario_telainicial_Button_2.setText(_translate("Cadastro", "Cadastrar Usuario"))
        self.buscar_tarefa_telainicial_Button.setText(_translate("Cadastro", "Buscar Tarefa"))
        self.buscar_tarefa_telainicial_Button_2.setText(_translate("Cadastro", "Encerrar Programa"))
        self.sair_telainicial_Button_5.setText(_translate("Cadastro", "Voltar"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">TELA INICIAL</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_inicial()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())

    