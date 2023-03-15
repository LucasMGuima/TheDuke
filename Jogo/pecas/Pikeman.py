import models.Tile as tl
import models.Board as bd

class Pikeman(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)
    
    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        self.posicoesPossiveis.clear()

        tamanhoTabuleiro = tabuleiro.tamanho()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if self.lado == 0:
        # Estado inicial
            if self.direcao:
                # Se move para cima
                if minhaLinha-1 >= 0:
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
                
            else:
                # Se move para baixo
                if minhaLinha+2 <= tamanhoTabuleiro-1:
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                    self.encontro((minhaLinha+2, minhaColuna), peca)

        elif self.lado == 1:
            if self.direcao:
                # diagonal superior esquerda
                if minhaLinha-1 >= 0 and minhaColuna-1 >= 0:
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.encontro((minhaLinha-1, minhaColuna-1), peca)
                # diagonal superior esquerda 2 vezes
                if minhaLinha-2 >= 0 and minhaColuna+2 <= 5:
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                    self.encontro((minhaLinha-2, minhaColuna-2), peca)
                # diagonal superior direita 1 vez
                if minhaLinha-1 >= 0 and minhaColuna+1 <= 5:
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                    self.encontro((minhaLinha-1, minhaColuna+1), peca)
                # diagonal superior direita 2 vezes
                if minhaLinha-2 >= 0 and minhaColuna+2 <= 5:
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                    self.encontro((minhaLinha-2, minhaColuna+2), peca)
            else:
                pass

    def informacao(self):
        return super().informacao()