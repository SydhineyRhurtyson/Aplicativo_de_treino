from time import sleep
class Exercicio:
    def __init__(self, nome:str, descricao:str, maquina:str, carga:float, serie:int=3, repeticoes:int=10, descanso:int=30, observacoes:str=None, duracao:int=None):
        """
        Inicializa um novo exercício.

        Args:
            nome (str): O nome do exercício.
            descricao (str): A descrição do exercício.
            maquina (str): A máquina utilizada no exercício.
            carga (float): A carga utilizada no exercício.
            serie (int, optional): O número de séries. padrão  3.
            repeticoes (int, optional): O número de repetições. padrão  10.
            descanso (int, optional): O tempo de descanso entre séries, em segundos. padrão de 30.
            observacoes (str, optional): Observações sobre o exercício. padrão de None.
            duracao (int, optional): A duração do exercício, em minutos. padrão de None.
        """
        self.nome = nome
        self.descricao = descricao
        self.maquina = maquina
        self.carga = carga
        self.serie = serie
        self.repeticoes = repeticoes
        self.descanso = descanso
        self.observacoes = observacoes
        self.duracao = duracao
    def esperar_descanso(self):
        """
        Pausa a execução do programa pelo tempo de descanso definido para o exercício.
        """
        print(f"Descansando por {self.descanso} segundos...")
        sleep(self.descanso)
