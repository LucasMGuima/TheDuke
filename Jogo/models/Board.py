import models.Tile

class Board():
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.colunas = {
            'A': 1,
            'B': 2,
            'C': 3,
            'E': 4,
            'F': 5,
            'G': 6
        }
        self.grade = [["▢" for i in range(self.tamanho)]] * self.tamanho

    def imprime(self):
        print("  A B C D E F") #nome das colunas
        for linha in range(len(self.grade)): #linhas
            novaLinha =  str(linha+1) + " "
            for espaco in self.grade[linha]: #espaco na linha
                novaLinha += espaco + " "
            print(novaLinha)

    def posicionarPeca(self, posicao: tuple, tile: models.Tile.Tile):
        coluna = self.colunas[posicao[0]]
        linha = posicao[1]
        self.grade[linha][coluna] = tile.imagem
        print(self.grade)
        