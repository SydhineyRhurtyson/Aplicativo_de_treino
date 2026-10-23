from Treino import Treino
from Cardio import Cardio
class ProgramaDeTreino:
    def __init__(self, nome:str, abdominal:str,cardio:Cardio=None,treinos:list=Treino):
        """
        Inicializa um novo programa de treino.

        Args:
            nome (str): O nome do programa de treino.
            abdominal (str): A descrição do exercício abdominal.
            cardio (Cardio, optional): O exercício de cardio. padrão de None.
            treinos (list, optional): A lista de treinos que compõem o programa. padrão de Treino.
        """
        self.nome = nome
        self.treinos = treinos
        self.abdominal = abdominal
        self.cardio = cardio
    def set_treinos(self, treinos):
        self.treinos = treinos
    def add_treino(self, treino):
        self.treinos.append(treino)