import models.Tile as tl
import models.Board as bd

#TODO
#ATAQUE

class Champion(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado ativo
            if(minhaLinha+1 <= 5): 
                peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                self.encontro((minhaLinha+1, minhaColuna), peca)
            if(minhaLinha+2 <= 5):
                peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                self.encontro((minhaLinha+2, minhaColuna), peca)
            if(minhaLinha-1 >= 0):
                peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.encontro((minhaLinha-1, minhaColuna), peca)
            if(minhaLinha-2 >= 0):
                peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                self.encontro((minhaLinha-2, minhaColuna), peca)

            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaLinha+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
            if(minhaColuna+2 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaLinha+2]
                self.encontro((minhaLinha, minhaColuna+2), peca)
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
            if(minhaColuna-2 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaLinha-2]
                self.encontro((minhaLinha, minhaColuna-2), peca)
        
        elif(self.lado == 1):
            #Lado não-ativo
            if(minhaLinha+2 <= 5):
                peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                self.encontro((minhaLinha+2, minhaColuna), peca)
            if(minhaLinha-2 >= 0):
                peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                self.encontro((minhaLinha-2, minhaColuna), peca)

            if(minhaColuna+2 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+2]
                self.encontro((minhaLinha, minhaColuna+2), peca)
            if(minhaColuna-2 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-2]
                self.encontro((minhaLinha, minhaColuna-2), peca)