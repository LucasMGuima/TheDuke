import models.Tile as tl
import models.Board as bd

class Wizard(tl.Tile):
    def __init__(self, imagem: str, jogador):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado ativo
            if(minhaLinha-1 >= 0):
                peca: tl.Tile = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.__encotro((minhaLinha-1, minhaColuna), peca)
            if(minhaLinha+1 <= 5): 
                peca: tl.Tile = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.__encotro((minhaLinha-1, minhaColuna), peca)
            
            if(minhaColuna-1 >= 0): 
                peca: tl.Tile = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.__encotro((minhaLinha, minhaColuna-1), peca)
            if(minhaColuna+1 <= 5): 
                peca: tl.Tile = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.__encotro((minhaLinha, minhaColuna+1), peca)

            if(minhaLinha-1 >= 0):
                if(minhaColuna-1 >= 0): 
                    peca: tl.Tile = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.__encotro((minhaLinha-1, minhaColuna-1), peca)
                if(minhaColuna+1 <= 5): self.__salvarPosicao(minhaLinha-1, minhaColuna+1)
            if(minhaLinha+1 <= 5):
                if(minhaColuna-1 >= 0): self.__salvarPosicao(minhaLinha+1, minhaColuna-1)
                if(minhaColuna+1 <= 5): self.__salvarPosicao(minhaLinha+1, minhaColuna+1)
        elif(self.lado == 1):
            #Lado não-ativo
            if(minhaLinha-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)
            if(minhaLinha+2 <= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna)
            
            if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha, minhaColuna-2)
            if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha, minhaColuna+2)

            if(minhaLinha-2 >= 0):
                if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna-2)
                if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
            
            if(minhaLinha+2 <= 0):
                if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha+2, minhaColuna-2)
                if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna+2)