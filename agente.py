
import random
import time

class RoboAspirador:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicao = (0, 0)  # Começa no canto superior esquerdo
        self.movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direções: direita, baixo, esquerda, cima
    
    def exibir_ambiente(self):
        # Exibe o ambiente, incluindo bordas e a posição do robô
        print("+" + "-" * (2 * len(self.ambiente[0]) + 1) + "+")
        for i, linha in enumerate(self.ambiente):
            linha_com_robo = linha[:]
            if i == self.posicao[0]:
                linha_com_robo[self.posicao[1]] = "A"
            print("| " + " ".join(linha_com_robo) + " |")
        print("+" + "-" * (2 * len(self.ambiente[0]) + 1) + "+\n")


    def detectar_sujeira(self):
        x, y = self.posicao
        return self.ambiente[x][y] == "D"

    def limpar(self):
        x, y = self.posicao
        self.ambiente[x][y] = " "  # Remove a sujeira
        print(f"Limpei a sujeira em {self.posicao}!")

    def mover(self):
        movimentos_validos = []
        for dx, dy in self.movimentos:
            nova_posicao = (self.posicao[0] + dx, self.posicao[1] + dy)
            if self.verificar_limite(nova_posicao):
                movimentos_validos.append(nova_posicao)
        
        if movimentos_validos:
            self.posicao = random.choice(movimentos_validos)

    def verificar_limite(self, posicao):
        x, y = posicao
        return 0 <= x < len(self.ambiente) and 0 <= y < len(self.ambiente[0]) and self.ambiente[x][y] != "#"

    def executar(self):
        print("Iniciando limpeza!")
        start_time = time.perf_counter()
        while any("D" in linha for linha in self.ambiente):
            self.exibir_ambiente()
            if self.detectar_sujeira():
                self.limpar()
            else:
                self.mover()
            time.sleep(1)
        end_time = time.perf_counter()  
        elapsed_time = end_time - start_time
        print(f"Limpeza concluída em {elapsed_time:.2f} segundos!")
        self.exibir_ambiente()

# Criando o ambiente
def criar_ambiente(linhas, colunas, sujeira, paredes):
    ambiente = [[" " for _ in range(colunas)] for _ in range(linhas)]
    
    # Adicionando sujeira
    for _ in range(sujeira):
        while True:
            x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
            if ambiente[x][y] == " ":
                ambiente[x][y] = "D"
                break

    # Adicionando paredes
    for _ in range(paredes):
        while True:
            x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
            if ambiente[x][y] == " ":
                ambiente[x][y] = "#"
                break
    
    return ambiente

# Configurações do ambiente
linhas, colunas = 6, 6
sujeira = 8
paredes = 6

ambiente = criar_ambiente(linhas, colunas, sujeira, paredes)
robo = RoboAspirador(ambiente)
robo.executar()
