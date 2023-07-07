from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_tarefa(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(604, 542)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(110, 160, 381, 311))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cadastrar_telainicial__Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_telainicial__Button.setGeometry(QtCore.QRect(110, 70, 161, 51))
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
        self.buscar_tarefa_telainicial_Button = QtWidgets.QPushButton(self.frame)
        self.buscar_tarefa_telainicial_Button.setGeometry(QtCore.QRect(110, 130, 161, 51))
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
        self.sair_telainicial_Button_5 = QtWidgets.QPushButton(self.frame)
        self.sair_telainicial_Button_5.setGeometry(QtCore.QRect(150, 200, 81, 21))
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
        self.label.setGeometry(QtCore.QRect(170, 100, 271, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.cadastrar_telainicial__Button.setText(_translate("Cadastro", "Tarefas Recentes"))
        self.buscar_tarefa_telainicial_Button.setText(_translate("Cadastro", "Todas as Tarefas"))
        self.sair_telainicial_Button_5.setText(_translate("Cadastro", "Voltar"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Menu Tarefas</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_tarefa()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())