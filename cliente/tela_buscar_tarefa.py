from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_buscar_tarefa(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(710, 610)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(70, 100, 581, 461))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.excluir_tarefa_Button = QtWidgets.QPushButton(self.frame)
        self.excluir_tarefa_Button.setGeometry(QtCore.QRect(230, 390, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.excluir_tarefa_Button.setFont(font)
        self.excluir_tarefa_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_tarefa_Button.setStyleSheet("QPushButton{ color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); border-radius: 10px; } QPushButton:hover{ color: rgb(255, 255, 255); background-color: rgb(0, 0, 0); }")
        self.excluir_tarefa_Button.setObjectName("excluir_tarefa_Button")
        self.campo_list_widget = QtWidgets.QListWidget(self.frame)
        self.campo_list_widget.setGeometry(QtCore.QRect(70, 50, 431, 331))
        self.campo_list_widget.setStyleSheet("QListWidget{ background-color: rgb(255, 255, 255); border-radius: 10px; border: 1px solid black; }")
        self.campo_list_widget.setObjectName("campo_list_widget")
        self.excluir_tarefa_Button_2 = QtWidgets.QPushButton(self.frame)
        self.excluir_tarefa_Button_2.setGeometry(QtCore.QRect(500, 430, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.excluir_tarefa_Button_2.setFont(font)
        self.excluir_tarefa_Button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.excluir_tarefa_Button_2.setStyleSheet("QPushButton{ color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); border-radius: 10px; } QPushButton:hover{ color: rgb(255, 255, 255); background-color: rgb(0, 0, 0); }")
        self.excluir_tarefa_Button_2.setObjectName("excluir_tarefa_Button_2")
        self.label = QtWidgets.QLabel(Cadastro)
        self.label.setGeometry(QtCore.QRect(240, 60, 241, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.excluir_tarefa_Button.setText(_translate("Cadastro", "Excluir"))
        self.excluir_tarefa_Button_2.setText(_translate("Cadastro", "Voltar"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">SUAS TAREFAS</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_buscar_tarefa()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())