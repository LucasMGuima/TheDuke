import abc

#TODO
#IMPLEMENTAR UMA LOGICA PARA O MOVIMENTO DE ATAQUE

class Tile():
    def __init__(self, imagem: str, jogador: str):
        self.imagem = imagem
        self.posicao = tuple()
        self.lado = 0
        self.jogador = jogador
        #Direcao: False -> Se move pra baixo / True -> Se move pre cima 
        self.direcao: bool = False
        self.posicoesPossiveis = list()

    def imagem(self):
        """
            Retorna a imagem da peca
        """
        return self.imagem

    def mudarLado(self) -> None:
        """
            Muda o lado ativo da peca
        """
        if(self.lado == 0): self.lado = 1
        else: self.lado = 0

    def __aliado(self, peca) -> bool:
        return self.jogador == peca.jogador

    def encontro(self, posicao: tuple , peca) -> bool:
        """
            Recebe a nova posição e o tile que ela representa,
            se ele estiver vazio ("_") apenas salva a pocivel posição
            se não verifica se o tile é do jogador ou não e faz a movimentação devida
            e return true

            ---------
            Param \n
            --------
            posicao -> Tupla da posição a ser checadas\n
            peca -> Tile encontrado na posição

            ---------
            Return \n
            ---------
            True -> Se encontro um tile\n
            False -> Se o tile é vazio
        """

        if(peca.imagem == "_"):
            self.__salvarPosicao(posicao[0], posicao[1])
            return False

        aliado = self.__aliado(peca)
        
        if(aliado == False):
            #econtro um peca e não é alidas
            self.__salvarPosicao(posicao[0], posicao[1])

        return True

    def mover(self, input: tuple, tamanhoTabuleiro: int) -> bool:
        linha = input[0]
        coluna = input[1]
        print(input)
        if([linha, coluna] in self.posicoesPossiveis):
            self.posicao = (linha, coluna)
            self.mudarLado()
            return True
        return False

    def __salvarPosicao(self, linha: int, coluna: int):
        self.posicoesPossiveis.append([linha, coluna])

    @abc.abstractmethod
    def informacao(self):
        """
            Informa os movimentos pociveis da peca
        """
        return

    @abc.abstractmethod
    def acharPosicoesPossiveis(self, tabuleiro) -> None:
        raise "Implementar a logica de encontrar as posicoes possiveis"