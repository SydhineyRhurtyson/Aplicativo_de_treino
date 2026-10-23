from Exercicio import Exercicio
from time import sleep
class Treino:
    def __init__(self, nome:str, descricao:str, membros:str, descanso:float=None, exercicios:list=Exercicio):
        """Inicializa um novo treino.
            Args:
            nome (str): O nome do treino.
            descricao (str): A descrição do treino.
            membros (str): Os membros do corpo que serão trabalhados no treino.
            descanso (int, optional): O tempo de descanso entre os exercícios, em segundos. padrão de None.
            exercicios (list, optional): A lista de exercícios que compõem o treino. padrão de Exercicio.
        """
        self.nome = nome
        self.membros = membros
        self.descricao = descricao
        self.descanso = descanso
        self.exercicios = exercicios
    def set_exercicios(self, exercicios):
        self.exercicios = exercicios
    def esperar_descanso(self):
        """
        Pausa a execução do programa pelo tempo de descanso definido para o exercício.
        """
        print(f"Descansando por {self.descanso} segundos...")
        sleep(self.descanso)
    def add_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    def to_do(self):
        """
        Executa todos os exercícios do treino, respeitando o tempo de descanso entre eles.
        """
        for exercicio in self.exercicios:
            print(f"Executando {exercicio.nome} por {exercicio.serie} séries de {exercicio.repeticoes} repetições...")
            if exercicio.duracao:
                sleep(exercicio.duracao * 60)
            else:
                sleep(exercicio.serie * exercicio.repeticoes * 2)  # Supondo 2 segundos por repetição
            exercicio.esperar_descanso()