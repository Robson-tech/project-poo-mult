# pyuic5 tela_login2.ui -o tela_login2.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_inicial(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(672, 569)
        Cadastro.setStyleSheet("background-color: rgb(0, 70, 112);")
        self.frame = QtWidgets.QFrame(Cadastro)
        self.frame.setGeometry(QtCore.QRect(140, 160, 381, 311))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cadastrar_telainicial__Button = QtWidgets.QPushButton(self.frame)
        self.cadastrar_telainicial__Button.setGeometry(QtCore.QRect(110, 40, 161, 51))
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
        self.buscar_tarefa_telainicial_Button.setGeometry(QtCore.QRect(110, 100, 161, 51))
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
        self.buscar_tarefa_telainicial_Button_2.setGeometry(QtCore.QRect(110, 160, 161, 51))
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
        self.sair_telainicial_Button_5.setGeometry(QtCore.QRect(150, 230, 81, 21))
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
        self.label.setGeometry(QtCore.QRect(200, 60, 271, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Cadastro)
        self.pushButton.setGeometry(QtCore.QRect(540, 50, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 112, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 112, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 70, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Cadastro)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Form"))
        self.cadastrar_telainicial__Button.setText(_translate("Cadastro", "Cadastrar Tarefa"))
        self.buscar_tarefa_telainicial_Button.setText(_translate("Cadastro", "Buscar Tarefa"))
        self.buscar_tarefa_telainicial_Button_2.setText(_translate("Cadastro", "Encerrar Programa"))
        self.sair_telainicial_Button_5.setText(_translate("Cadastro", "Voltar"))
        self.label.setText(_translate("Cadastro", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Menu de Opções</span></p></body></html>"))
        # self.pushButton.setStyleSheet("QPushButton { color: rgb(255, 255, 255); }")
        self.pushButton.setText(_translate("Cadastro", "🔔 (1)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Tela_inicial()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())
