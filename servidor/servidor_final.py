from banco import Banco
from tarefa import Tarefa
from login import Login
from usuario import Usuario

import threading
import socket
bank = Banco()

class usuario(threading.Thread):

    """
    Classe que representa um usuário do banco
    """

    def __init__(self,adress,con) -> None:

        """
        Construtor da classe necessário para criar os atributo ao instanciar um objeto 
        """

        threading.Thread.__init__(self)
        self.con = con
        self.adress = adress

        #print('Nova conexão:',con)

    def run(self):
        lock = threading.Lock()
        while (True):

            msg_cliente = self.con.recv(1024).decode()
            comando = msg_cliente.split(',')

            # login do usuario
            if comando[0] == 'usuario':
                retorno_cliente = bank.loginUsuario(comando[1], comando[2])
                # Other code in the run method
                if retorno_cliente[0]:  # Assuming `retorno_cliente` is the return value of loginUsuario
                    self.con.send('1'.encode())
                else:
                    self.con.send('0'.encode())
                        
            # cadastro usuario
            elif comando[0] == 'cad_usuario':
                usuario = Usuario(id_usuario=comando[1], nome=comando[2], email=comando[3], username=comando[4], senha=comando[5])
                success = bank.cadastrar_usuario_bd(usuario)
                
                if success:
                    self.con.send('1'.encode())
                else:
                    self.con.send('0'.encode())
            
            # listar tarefas
            elif comando[0] == 'abrir':
                with lock:
                    retorno_cliente = bank.listarTarefas()

                if retorno_cliente:
                    self.con.send(retorno_cliente.encode())
                else:
                    self.con.send('0'.encode())

            # cadastro tarefa
            elif comando[0] == 'cad_tarefa':
                id_tarefa = comando[1]
                descricao = comando[2]
                prazo = comando[3]
                id_usuario = bank.get_id_usuario()
                tarefa = Tarefa(id_tarefa=id_tarefa, id_usuario=id_usuario, descricao=descricao, prazo=prazo)
                
                sucess = bank.cadastrar_tarefas(id_tarefa, descricao, prazo, id_usuario)

                if sucess:
                    self.con.send('1'.encode())
                else:
                    self.con.send('3'.encode())

            # excluir tarefa
            elif comando[0] == 'excluir_tarefa':
                sucess = bank.excluirTarefa(descricao=comando[1], prazo=comando[2])

                if sucess:
                    self.con.send('1'.encode())
                else:
                    self.con.send('0'.encode())
            # sair
            elif comando[0] == 'sair':
                self.con.close()
                print(f'Conexão {self.con} ENCERRADA')
                break
            
def iniciar_servidor():
    """
    criação de um socket para o servidor "serv_socket" para receber as solicitações dos usuários e repassar as mesmas para o banco.
    parameters:
        None
    return
        None
    """
    ip = '10.180.47.77'
    port = 9013

    addr = ((ip, port)) # define a tupla de endereço
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(addr)

    """
    Laço de repetição de para que o servidor crie uma nova instancia da conexão sempre que um novo usuário se conectar
    """

    while True:
        serv_socket.listen(10)

        print('aguardando conexão...\n')
        conexao, cliente = serv_socket.accept()
        newthread = usuario(cliente, conexao)
        newthread.start()
        print('\nConectado')

if __name__ == '__main__':
    iniciar_servidor()
    

     
    