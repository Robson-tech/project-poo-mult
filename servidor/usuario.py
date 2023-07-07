class Usuario:
    def __init__(self, nome, username, email, senha, id_usuario=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.username = username
        self.email = email
        self.senha = senha