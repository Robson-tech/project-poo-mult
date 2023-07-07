import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from tela_cadastro_tarefa import Tela_cadastroTarefa
from tela_cadastro_usuario import Tela_cadastroUsuario
from tela_login import Tela_login
from tela_inicial import Tela_inicial
from tela_buscar_tarefa import Tela_buscar_tarefa
from datetime import datetime

import socket
ip = '10.180.47.77'
port = 9013
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)

class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack0)

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack1)

        self.tela_cadastro_usuario = Tela_cadastroUsuario()
        self.tela_cadastro_usuario.setupUi(self.stack2)

        self.tela_cadastro_tarefa = Tela_cadastroTarefa()
        self.tela_cadastro_tarefa.setupUi(self.stack3)

        self.tela_buscar_tarefa = Tela_buscar_tarefa()
        self.tela_buscar_tarefa.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)

class Main(QMainWindow, Ui_main):
    def __init__(self, login_atual=None): 
        super(Main, self).__init__()
        self.setupUi(self)
        self.login_atual = login_atual
        self.id_usuario = None

        self.tela_login.login_Button.clicked.connect(self.loginUser)
        self.tela_login.nova_conta_Button.clicked.connect(self.abrir_tela_cadastro_usuario)
        self.tela_login.sair_login_Button.clicked.connect(self.sair)
        
        self.tela_inicial.cadastrar_telainicial__Button.clicked.connect(self.abrir_tela_cadastro_tarefa)
        self.tela_inicial.pushButton.clicked.connect(self.receberMensagemServidor)
        self.tela_inicial.buscar_tarefa_telainicial_Button.clicked.connect(self.abrir_tela_buscar_tarefa)
        self.tela_inicial.sair_telainicial_Button_5.clicked.connect(self.abrir_tela_login)
        self.tela_inicial.buscar_tarefa_telainicial_Button_2.clicked.connect(self.sair)

        self.tela_cadastro_usuario.cadastrar_Button.clicked.connect(self.cadastrar_usuario)
        self.tela_cadastro_usuario.voltar_Button.clicked.connect(self.abrir_tela_login)
        
        self.tela_cadastro_tarefa.cadastrar_tarefa_Button.clicked.connect(self.cadastrar_tarefa)
        self.tela_cadastro_tarefa.voltar_tarefa_Button.clicked.connect(self.abrir_tela_inicial)
        
        self.tela_buscar_tarefa.excluir_tarefa_Button.clicked.connect(self.excluir_tarefa_linha)
        self.tela_buscar_tarefa.excluir_tarefa_Button_2.clicked.connect(self.abrir_tela_inicial)

    def abrir_tela_inicial(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_cadastro_tarefa(self):
        self.QtStack.setCurrentIndex(3)

    def abrir_tela_cadastro_usuario(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_login(self):
        self.QtStack.setCurrentIndex(0)
    
    # Função de buscar a tarefa - botao
    def abrir_tela_buscar_tarefa(self):
        self.QtStack.setCurrentIndex(4)
        self.tela_buscar_tarefa.campo_list_widget.clear()  # Limpa a lista de itens

        # Send a message to the server indicating the intention to open the "buscar_tarefa" screen
        mensagem = "abrir"
        cliente_socket.send(mensagem.encode())

        # Receive the list of tasks from the server
        recebida = cliente_socket.recv(1024).decode()
        print(recebida)
        
        if recebida == '0':
            QMessageBox.warning(self, "Buscar Tarefa", "Erro ao obter a lista de tarefas.")
        else:
            lista = recebida.split(",")
            for item in lista:
                self.tela_buscar_tarefa.campo_list_widget.addItem(item)
                        
    def sair(self):
        mensagem = 'sair'
        cliente_socket.send(mensagem.encode())
        print('mensagem enviada')
        if mensagem == 'sair':
            cliente_socket.close()
            print('ENCERRADO Conexao Cliente')
            sys.exit()

    def receberMensagemServidor(self):
        try:
            # Mensagem do cliente
            mensagem = f'quant_tarefa'
            cliente_socket.send(mensagem.encode()) #  utilizado para codificar a string da mensagem em bytes
            print('mensagem enviada')

            mensagem = cliente_socket.recv(1024).decode()
            if mensagem:
                print("Mensagem recebida do servidor:", mensagem)
                if mensagem.startswith("Quantidade de tarefas:"):
                    quantidade_tarefas = int(mensagem.split(":")[1].strip())
                    print("Quantidade de tarefas:", quantidade_tarefas)
                    # Exibe a quantidade de tarefas em um QMessageBox
                    QtWidgets.QMessageBox.information(None, 'interface', f'Quantidade de tarefas: {quantidade_tarefas}')
            else:
                # Imprime uma mensagem de erro
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro ao informar a quantidade de tarefas.')
        except Exception as e:
                QtWidgets.QMessageBox.information(None, 'interface', f'Erro: {str(e)}')

    def cadastrar_usuario(self):
        id_usuario = self.tela_cadastro_usuario.id_usuario_lineEdit_2.text()
        nome = self.tela_cadastro_usuario.nome_lineEdit.text()
        email = self.tela_cadastro_usuario.email_lineEdit.text()
        username = self.tela_cadastro_usuario.username_lineEdit.text()
        senha = self.tela_cadastro_usuario.password_lineEdit.text()

        # Verificar se todos os dados foram preenchidos
        if not (id_usuario == '' or nome == '' or email == '' or username == '' or senha == ''):
            # Mensagem do cliente
            try:
                mensagem = f'cad_usuario,{id_usuario},{nome},{email},{username},{senha}'
                cliente_socket.send(mensagem.encode())
                print('mensagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    # Limpar os dados
                    self.tela_cadastro_usuario.id_usuario_lineEdit_2.setText('')
                    self.tela_cadastro_usuario.nome_lineEdit.setText('')
                    self.tela_cadastro_usuario.email_lineEdit.setText('')
                    self.tela_cadastro_usuario.username_lineEdit.setText('')
                    self.tela_cadastro_usuario.password_lineEdit.setText('')
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'id já cadastrado!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente-servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: id já cadastrado!')
        else:
            # Imprime uma mensagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! Informe todos os campos.')

    def cadastrar_tarefa(self):
        id_tarefa = self.tela_cadastro_tarefa.idtarefa_lineEdit.text()
        descricao = self.tela_cadastro_tarefa.descricao_textEdit.toPlainText()
        prazo = self.tela_cadastro_tarefa.prazo_lineEdit.text() 

        # Verificar se todos os dados foram preenchidos
        if id_tarefa and descricao and prazo:
            try:
                # Verificar o formato da data
                try: 
                    datetime.strptime(prazo, "%Y-%m-%d") 
                except ValueError:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Formato de prazo inválido! Utilize o formato "yyyy-mm-dd".')
                    return

                # Mensagem do cliente
                mensagem = f'cad_tarefa,{id_tarefa},{descricao},{prazo}'
                cliente_socket.send(mensagem.encode()) #  utilizado para codificar a string da mensagem em bytes
                print('mensagem enviada')
                recebida = cliente_socket.recv(1024).decode()

                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    # Limpar os dados
                    self.tela_cadastro_tarefa.idtarefa_lineEdit.setText('')
                    self.tela_cadastro_tarefa.descricao_textEdit.setPlainText('')
                    self.tela_cadastro_tarefa.prazo_lineEdit.setText('')
                # elif recebida == '0':
                # QtWidgets.QMessageBox.information(None, 'interface', 'ID já cadastrado!')
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de integridade. Banco de Dados!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente-servidor!')

            except Exception as e:
                QtWidgets.QMessageBox.information(None, 'interface', f'Erro: {str(e)}')
        else:
            # Imprime uma mensagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! Informe todos os campos.')

    def excluir_tarefa_linha(self):
        item_selecionado = self.tela_buscar_tarefa.campo_list_widget.currentItem()

        if item_selecionado is not None:
            descricao_prazo = item_selecionado.text().split(" - ")
            descricao = descricao_prazo[0]
            prazo = descricao_prazo[1]

            mensagem = f"excluir_tarefa,{descricao},{prazo}"
            cliente_socket.send(mensagem.encode())

            # Receive response from the server
            recebida = cliente_socket.recv(1024).decode()
            if recebida == '1':
                self.tela_buscar_tarefa.campo_list_widget.takeItem(self.tela_buscar_tarefa.campo_list_widget.row(item_selecionado))
                QMessageBox.information(self, "Excluir Tarefa", "Tarefa excluída com sucesso!")
            else:
                QMessageBox.warning(self, "Excluir Tarefa", "Erro ao excluir a tarefa.")
        else:
            QMessageBox.warning(self, "Excluir Tarefa", "Selecione uma tarefa para excluí-la.")
    
    def loginUser(self):
        username =  self.tela_login.cpf_lineEdit.text()
        senha = self.tela_login.senha_lineEdit.text()

        if not(username=='' or senha==''):
            # menssagem do cliente
            try:
                menssagem =  f'usuario,{username},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrir_tela_inicial()
                    # limpar os dados
                    self.tela_login.cpf_lineEdit.text()
                    senha = self.tela_login.senha_lineEdit.text()
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Usuario cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
