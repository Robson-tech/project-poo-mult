#importação do banco de dados
import sys
import mysql.connector
from mysql.connector import Error

import threading
# importação das classes
from usuario import Usuario
from tarefa import Tarefa
from login import Login

class Banco:
    """
    Classe responsável por manipular as tarefas.
    """

    def __init__(self, lista=None, id_usuario=None):
        """
        Inicializa uma instância da classe ManipulaTarefas.
        """
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()
        self.lista = lista
        self.id_usuario = id_usuario

        self.lock = threading.Lock()
        
        self.login_atual_usua = ''
        self.senha_atual_usua = ''

    def create_connection(self):
        """
        Cria uma conexão com o banco de dados MySQL.

        Returns:
            obj: Objeto de conexão com o banco de dados.
        """
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='C0mpL3xP@$$',
                database='project_tarefa',
            )
            return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def close_connection(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def get_id_usuario(self):
        """
        Retorna o ID do usuário atualmente logado.

        Returns:
            int: ID do usuário.
        """
        return self.id_usuario

    def listarTarefas(self):
        try:
            self.cursor = self.connection.cursor()

            # Verificar se o usuário existe no banco de dados
            if self.id_usuario is None:
                print("\nUsuário não encontrado.")
                return False

            # Buscar as tarefas do usuário pelo ID
            query = "SELECT descricao, prazo FROM tarefa WHERE id_usuario = %s"
            values = (self.id_usuario,)
            self.cursor.execute(query, values)
            results = self.cursor.fetchall()

            if results:
                lista_tarefas = [[str(result[0]), result[1]] for result in results]
                enviar = ",".join([f"{tarefa[0]} - {tarefa[1]}" for tarefa in lista_tarefas])
                return enviar
            else:
                return False
            
        except Error as e:
            print(f"Erro ao listar as tarefas: {e}")
            return False

    def cadastrar_usuario_bd(self, usuario, login):
        try:
            cursor = self.connection.cursor()

            # Verificar se o usuário já existe no banco de dados
            usuario_existente = self.buscar_usuario_por_id(usuario.id_usuario)
            if usuario_existente is None:
                # Inserir o novo usuário na tabela
                query_usuario = "INSERT INTO usuario (id_usuario, nome, email) VALUES (%s, %s, %s)"
                values_usuario = (usuario.id_usuario, usuario.nome, usuario.email)
                cursor.execute(query_usuario, values_usuario)

                # Inserir o novo login na tabela
                query_login = "INSERT INTO login (id_login, id_usuario, username, password) VALUES (%s, %s, %s, %s)"
                values_login = (usuario.id_usuario, usuario.id_usuario, login.username, login.senha)
                try:
                    # utilizando o cursor para executar a inserção no banco de dados
                    self.cursor.execute(query_login, values_login)
                    #confirmar a inserção
                    self.connection.commit()
                    return True
                except mysql.connector.errors.IntegrityError:
                    return False
            else:
                return False
        except Error as e:
            return False, f"Erro ao cadastrar o usuário: {e}"

    def excluirTarefa(self, descricao, prazo):
        try:
            self.connection.commit()
            selecione = "SELECT descricao, prazo, id_usuario FROM tarefa WHERE descricao = %s AND prazo = %s"
            self.cursor.execute(selecione, (descricao, prazo,))
            resultado = self.cursor.fetchone()
            print('resultado:', resultado)

            if resultado is not None:
                # Armazenar as informações da tarefa excluída na lista exclusoes
                # exclusoes.append(resultado)
                
                # Excluir a tarefa do banco de dados
                query = "DELETE FROM tarefa WHERE descricao = %s AND prazo = %s"
                values = (resultado[0], resultado[1])
                self.cursor.execute(query, values)
                self.connection.commit()
                print('excluido')
                return True
            else:
                return False
        except Error as e:
            print(f"Erro ao excluir a tarefa: {e}")

    def loginUsuario(self, username, password):
        try:
            result = self.fazer_login(username, password)
            self.connection.commit()
            if result:
                self.login_atual_usua = username
                self.senha_atual_usua = password
                return (True,)  # Return a tuple with a single element representing success
            else:
                return (False,)  # Return a tuple with a single element representing failure
        except Exception as e:
            print('Erro do servidor durante o login:', str(e))
            return (False,)  # Return a tuple with a single element representing failur

    def fazer_login(self, username, password):
            """
            Faz o login de um usuário.
            """
            try:
                cursor = self.connection.cursor()

                # Buscar o usuário pelo nome de usuário (username) e senha
                query = "SELECT * FROM login WHERE username = %s AND password = %s"
                values = (username, password)
                cursor.execute(query, values)
                result = cursor.fetchone()

                if result:
                    id_usuario = result[1] # 
                    self.id_usuario = id_usuario # 
                    usuario = self.buscar_usuario_por_id(id_usuario) # 
                    print("\nLogin bem-sucedido!")
                    # print(usuario)
                    return True
                else:
                    print("\nCredenciais inválidas.")
                    return False
            except Error as e:
                print(f"Erro ao fazer login: {e}")  

    def cadastrar_tarefas(self, id_tarefa, descricao, prazo, id_usuario):
        try:
            cursor = self.connection.cursor()
            self.connection.commit()

            # Verificar se o usuário existe no banco de dados
            usuario = self.buscar_usuario_por_id(self.login_atual_usua)
            if usuario is None:
                print("\nUsuário não encontrado.")
                return False
    
            # Inserir a nova tarefa na tabela
            query_tarefa = "INSERT INTO tarefa (id_tarefa, descricao, prazo, email, id_usuario) " \
                        "VALUES (%s, %s, %s, %s, %s)"
            values_tarefa = (id_tarefa, descricao, prazo, usuario.email, id_usuario)
            try:
                # utilizando o cursor para executar a inserção no banco de dados
                self.cursor.execute(query_tarefa, values_tarefa)
                self.connection.commit()
                # confirmar a inserção
                return True
            except mysql.connector.errors.IntegrityError:
                return False
            # else:
            #     enviar = '0'
            #     conexao_servidor.send(enviar.encode())
        except Error as e:
            return False, f"Erro ao cadastrar a tarefa: {e}"

    def buscar_usuario_por_id(self, id_usuario):
        """
        Busca um usuário pelo ID no banco de dados.

        Args:
            id_usuario (int): O ID do usuário a ser buscado.

        Returns:
            Usuario: O objeto de usuário encontrado, ou None se não encontrado.
        """
        try:
            cursor = self.connection.cursor()

            query = "SELECT * FROM usuario WHERE id_usuario = %s"
            values = (id_usuario,)
            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                id_usuario, nome, email = result
                usuario = Usuario(id_usuario, nome, email)
                return usuario
            else:
                return None
        except Error as e:
            print(f"Erro ao buscar o usuário: {e}")