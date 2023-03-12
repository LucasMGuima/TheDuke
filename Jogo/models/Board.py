import models.Tile as tl

class Board():
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.colunas = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5
        }
        self.grade = [tl.Tile("_", "")]*self.tamanho
        for n in range(self.tamanho):
            self.grade[n] = [tl.Tile("_","")]*self.tamanho

    def __limpaEspaco(self, posicao: tuple) -> None:
        """
            Limpa um espaco especifico do tabuleiro
        """
        self.grade[posicao[0]][posicao[1]] = tl.Tile("_", "")
    
    def __capturar(self, peca: tl.Tile):
        peca.__del__()

    def imprime(self):
        """
            Imprime a situacao autal do tabuleiro
        """
        print("  A B C D E F") #nome das colunas
        for linha in range(len(self.grade)): #linhas
            novaLinha =  str(linha) + " "
            for tile in self.grade[linha]: #espaco na linha
                novaLinha += tile.imagem + " "
            print(novaLinha)

    def iniciarPeca(self, peca: tl.Tile) -> None:
        linha = peca.posicao[0]
        coluna = peca.posicao[1]

        self.grade[linha][coluna] = peca

    def posicaoVazia(self, posicao: tuple) -> bool:
        """
            Verifica se uma determinada posicao esta vazia no tabuleiro

            Parametros:
                posicao -> Tupla representando a posicao a ser checada

            Retorno:
                True -> Se a posicao esta vazia \n
                False -> Se a posicao esta ocupada
        """
        coluna = self.colunas[posicao[1]]
        linha = posicao[0]
        tile = self.grade[linha][coluna]
        if(tile.imagem == '_'):
            return True
        return False

    def posicionarPeca(self, posicao: tuple, peca: tl.Tile):
        """
            Coloca/Move uma peca especifica no tabuleiro

            Parametros:
                posicao -> Tupla com a nova posicao da peca \n
                tile -> Tile a ser movido para aquela posicao
            
            Retorno:
                True -> Se foi pocivel colocar a peca no local\n
                Se não foi pocivel colocar a peça retorna a peça que está no local
        """
        coluna = self.colunas[posicao[1]]
        linha = posicao[0]

        if(self.posicaoVazia(posicao)):
            #não ha nada na posição
            ultimaPoseTile = peca.posicao
            print(type(peca))
            if(peca.mover((linha, coluna), self)): 
                self.__limpaEspaco(ultimaPoseTile)
                self.grade[linha][coluna] = peca
                return True
            else: return False
        else:
            pecaNoLocal: tl.Tile = self.grade[linha][coluna]
            if(peca.jogador != pecaNoLocal.jogador):
                #Captura a peca do oponente
                peca.mover((linha, coluna), self)
                self.__capturar(pecaNoLocal)
            elif(peca.jogador == pecaNoLocal):
                #Remove essa movimentação
                return
