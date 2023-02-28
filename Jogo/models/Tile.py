import abc

class Tile():
    def __init__(self, imagem):
        self.imagem = imagem
        self.posicao = tuple()
        self.lado = 0
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

    @abc.abstractmethod
    def mover(self, input: tuple, tamanhoTabuleiro: int) -> bool:
        """
            O metodo mover recebe uma tupla representando a posicao no tabuleiro que a peca sera movida,
            verifica se a posição é valida e aplica a mesma se for

            Parametros:
                input -> Tupla representando a nova posicao da peca\n
                ramanhoTabuleiro -> Tamanho do tabuleiro, exemplo 6x6 -> tamanhoTabuleiro = 6

            Retorno:
                True -> Se a peca foi capaz de se mover pro local\n
                False -> Se a peca não foi capaz de se mover pro local     
        """
        raise "Implementar movimentacao"

    @abc.abstractmethod
    def informacao(self):
        """
            Informa os movimentos pociveis da peca
        """
        return

    @abc.abstractmethod
    def __acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        raise "Implementar a logica de encontrar as posicoes possiveis"