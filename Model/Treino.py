class Treino:
    def __init__(self, nome, descricao, duracao, exercicios):
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.exercicios = exercicios
    def set_exercicios(self, exercicios):
        self.exercicios = exercicios