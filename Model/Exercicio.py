class Exercicio:
    def __init__(self, nome, descricao, duracao,maquina,carga, serie=3,repeticoes=10, descanso=30, observacoes=None):
        self.nome = nome
        self.descricao = descricao
        self.maquina = maquina
        self.carga = carga
        self.serie = serie
        self.repeticoes = repeticoes
        self.descanso = descanso
        self.observacoes = observacoes
        