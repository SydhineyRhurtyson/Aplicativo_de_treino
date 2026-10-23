from time import sleep
from os import system
class Cardio:
    def __init__(self, nome:str, descricao:str=None, duracao:float=5, quantidade:int=0, intensidade:str="moderada"):
        """
        Inicializa um novo exercício cardiovascular.

        Args:
            nome (str): O nome do exercício. exemplo: corrida, bicicleta, natação, escada
            descricao (str): A descrição do exercício.
            duracao (int): A duração do exercício, em minutos.
            quantidade (int): A quantidade de vezes que o exercício será realizado na semana .
            intensidade (str): A intensidade do exercício.
        """
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.quantidade = quantidade
        self.intensidade = intensidade
    def executar(self):
        """
        Executa o exercício cardiovascular.
        """
        print(f"Executando {self.nome} por {self.duracao} minutos...")
        sleep(self.duracao * 60)
        