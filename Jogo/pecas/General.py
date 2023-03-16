import models.Tile as tl
import models.Board as bd

class General(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        #Limpa as posicoes antigas
        self.posicoesPossiveis.clear()

        tamanhoTabuleiro = tabuleiro.tamanho

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado ativo
            #TODO
            return