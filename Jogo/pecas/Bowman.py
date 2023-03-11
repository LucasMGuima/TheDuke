import models.Tile as tl
import models.Board as bd

class Bowman(tl.Tile):
    def __init__(self, imagem):
        super().__init__(imagem)

    
    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        tamanhoTabuleiro = tabuleiro.tamanho

        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Estado inicial
            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-1 >= 0): self.__salvarPosicao(minhaLinha-1, minhaColuna)
                if(minhaLinha+2 <= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna)
            else:
                #Se move pra baixo
                if(minhaLinha+1 <= 5): self.__salvarPosicao(minhaLinha+1, minhaColuna)
                if(minhaLinha-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)

            if(minhaColuna+1 <= 5): self.__salvarPosicao(minhaLinha, minhaColuna+1)
            if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha, minhaColuna+2)
            if(minhaColuna-1 >= 5): self.__salvarPosicao(minhaLinha, minhaColuna-1)
            if(minhaColuna-2 >= 5): self.__salvarPosicao(minhaLinha, minhaColuna-2)
        elif(self.lado == 1):
            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-1 >= 0): self.__salvarPosicao(minhaLinha-1, minhaColuna)


    def informacao(self):
        return super().informacao()