#importação do banco de dados
import mysql.connector
from mysql.connector import Error

# importação das classes
from usuario import Usuario
from tarefa import Tarefa

class Banco:
    """
    Classe responsável por manipular as tarefas.
    """
    def __init__(self):
        """
        Inicializa uma instância da classe ManipulaTarefas.
        """
        self.usuario = None
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

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

    def buscar_usuario(self, username):
        """
        Busca um usuário pelo ID no banco de dados.

        Args:
            id_usuario (int): O ID do usuário a ser buscado.

        Returns:
            Usuario: O objeto de usuário encontrado, ou None se não encontrado.
        """
        try:
            query = "SELECT * FROM usuario WHERE username = %s"
            values = (username,)
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                id_usuario, nome, email, nome_usuario, senha = result
                usuario = Usuario(nome, email, nome_usuario, senha, id_usuario)
                return usuario
            else:
                return None
        except Error as e:
            print(f"Erro ao buscar o usuário: {e}")

    def cadastrar_usuario_bd(self, usuario):
        try:
            # Verificar se o usuário já existe no banco de dados
            usuario_existente = self.buscar_usuario(usuario.username)
            if usuario_existente is None:
                # Inserir o novo usuário na tabela
                query_usuario = "INSERT INTO usuario (nome, email, username, senha) VALUES (%s, %s, %s, %s)"
                values_usuario = (usuario.nome, usuario.email, usuario.username, usuario.senha)
                self.cursor.execute(query_usuario, values_usuario)
                self.connection.commit()
                return True
            else:
                print("Usuário já cadastrado.")
                return False
        except Error as e:
            return False, f"Erro ao cadastrar o usuário: {e}"

    def loginUsuario(self, username, password):
            """
            Faz o login de um usuário.
            """
            try:
                # Buscar o usuário pelo nome de usuário (username) e senha
                query = "SELECT * FROM usuario WHERE username = %s AND password = %s"
                values = (username, password)
                self.cursor.execute(query, values)
                result = self.cursor.fetchone()

                if result:
                    self.usuario = Usuario(result[0], result[1], result[2], result[3], result[4])
                    print("\nLogin bem-sucedido!")
                    # print(usuario)
                    return True
                else:
                    print("\nCredenciais inválidas.")
                    return False
            except Error as e:
                print(f"Erro ao fazer login: {e}")

    def listarTarefas(self):
        try:
            self.cursor = self.connection.cursor()

            # Verificar se o usuário existe no banco de dados
            if self.id_usuario is None:
                print("\nUsuário não encontrado.")
                return False

            # Buscar as tarefas do usuário pelo ID
            query = "SELECT id_tarefa, descricao, prazo FROM tarefa WHERE id_usuario = %s"
            values = (self.id_usuario,)
            self.cursor.execute(query, values)
            results = self.cursor.fetchall()

            if results:
                lista_tarefas = [[str(result[0]), result[1], result[2]] for result in results]
                enviar = ",".join([f"{tarefa[0]} - {tarefa[1] - {tarefa[2]}}" for tarefa in lista_tarefas])
                return enviar
            else:
                return False
            
        except Error as e:
            print(f"Erro ao listar as tarefas: {e}")
            return False

    def excluirTarefa(self, id_tarefa):
        try:
            query = "DELETE FROM tarefa WHERE id_tarefa = %s"
            values = (id_tarefa,)
            self.cursor.execute(query, values)
            self.connection.commit()
            print('excluido')
            return True
        except Error as e:
            print(f"Erro ao excluir a tarefa: {e}")
            return False

    def cadastrar_tarefas(self, tarefa):
        if self.usuario is None:
            print("Usuário não logado.")
            return False
        try:
            # Inserir a nova tarefa na tabela
            query_tarefa = "INSERT INTO tarefa (id_tarefa, descricao, prazo, email, id_usuario) " \
                        "VALUES (%s, %s, %s, %s, %s)"
            values_tarefa = (tarefa.id_tarefa, tarefa.descricao, tarefa.prazo, self.usuario.email, self.usuario.id_usuario)
            self.cursor.execute(query_tarefa, values_tarefa)
            self.connection.commit()
        except Error as e:
            return False, f"Erro ao cadastrar a tarefa: {e}"


if __name__ == "__main__":
    banco = Banco()
    banco.create_connection()
    banco.close_connection()