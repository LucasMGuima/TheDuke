import models.Tile as tl

class Pikeman(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)
    
    def acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if self.lado == 0:
        # Estado inicial
            if self.direcao:
                # Se move para cima
                if minhaLinha-1 >= 0:
                    self.__salvarPosicao(minhaLinha-1, minhaColuna)
                
            else:
                # Se move para baixo
                if minhaLinha+2 <= tamanhoTabuleiro-1:
                    self.__salvarPosicao(minhaLinha+2, minhaColuna)

        elif self.lado == 1:
            if self.direcao:
                # diagonal superior esquerda
                if minhaLinha-1 >= 0 and minhaColuna-1 >= 0:
                    self.__salvarPosicao(minhaLinha-1, minhaColuna-1)
                # diagonal superior esquerda 2 vezes
                if minhaLinha-2 >= 0 and minhaColuna+2 <= 5:
                    self.__salvarPosicao(minhaLinha-2, minhaColuna-2)
                # diagonal superior direita 1 vez
                if minhaLinha-1 >= 0 and minhaColuna+1 <= 5:
                    self.__salvarPosicao(minhaLinha-1, minhaColuna+1)
                # diagonal superior direita 2 vezes
                if minhaLinha-2 >= 0 and minhaColuna+2 <= 5:
                    self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
            else:
                pass

    def informacao(self):
        return super().informacao()