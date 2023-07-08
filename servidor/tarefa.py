class Tarefa:
    """
    Classe que representa uma tarefa.
    """

    def __init__(self, titulo, descricao, prazo, id_usuario, id_tarefa=None):
        """
        Inicializa uma instância da classe Tarefa.

        Args:
            id_tarefa (int): O ID da tarefa.
            descricao (str): A descrição da tarefa.
            prazo (str): O prazo da tarefa.
            id_usuario (str): O ID do usuário associado à tarefa.
        """
        
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.id_usuario = id_usuario

    def __str__(self):
        return f"ID: {self.id_tarefa}, Descrição: {self.descricao}, Prazo: {self.prazo}, ID do Usuário: {self.id_usuario}"