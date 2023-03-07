import abc

#TODO
#IMPLEMENTAR UMA LOGICA PARA O MOVIMENTO DE ATAQUE

class Tile():
    def __init__(self, imagem):
        self.imagem = imagem
        self.posicao = tuple()
        self.lado = 0
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

    def mover(self, input: tuple, tamanhoTabuleiro: int) -> bool:
        linha = input[0]
        coluna = input[1]
        self.__acharPosicoesPossiveis(tamanhoTabuleiro)
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
    def __acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        raise "Implementar a logica de encontrar as posicoes possiveis"