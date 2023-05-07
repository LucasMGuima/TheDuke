import models.Tile as tl
import models.Board as bd

class Seer(tl.Tile):
    def __init__(self, imagem: str, jogador):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        #Limpar as posições
        self.posicoesPossiveis.clear()
        
        tamanhoTabuleiro = tabuleiro.tamanho

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado Ativo
            #Mov. Horizontal
            if(minhaColuna-2 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-2]
                self.encontro((minhaLinha, minhaColuna-2), peca)
            if(minhaColuna+2 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+2]
                self.encontro((minhaLinha, minhaColuna+2), peca)
            #Mov. Vertical
            if(minhaLinha-2 >= 0):
                peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                self.encontro((minhaLinha-2, minhaColuna), peca)
            if(minhaLinha+2 <= 0):
                peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                self.encontro((minhaLinha+2, minhaColuna), peca)

            #Mov. Diagonal
            if(minhaLinha-1 >= 0):
                if(minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.encontro((minhaLinha-1, minhaColuna-1), peca)
                if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
            if(minhaLinha+1 <= 5):
                if(minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.encontro((minhaLinha+1, minhaColuna-1), peca)
                if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.encontro((minhaLinha+1, minhaColuna+1), peca)
        elif(self.lado == 1):
            #Lado não ativo
            #Mov. Horizontal
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha, minhaColuna]
                self.encontro((minhaLinha, minhaColuna+1), peca)

            #Mov. Vertical
            if(minhaLinha-1 >= 0):
                peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.encontro((minhaLinha-1, minhaColuna), peca)
            if(minhaLinha+1 <= 5):
                peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                self.encontro((minhaLinha+1, minhaColuna), peca)

            #Mov. Diagonal
            if(minhaLinha-2 >= 0):
                if(minhaColuna-2 >= 0):
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                    self.encontro((minhaLinha-2, minhaColuna-2), peca)
                if(minhaColuna+2 <= 5):
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                    self.encontro((minhaLinha-2, minhaColuna+2), peca)
            if(minhaLinha+2 <= 5):
                if(minhaColuna-2 >= 0):
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                    self.encontro((minhaLinha+2, minhaColuna-2), peca)
                if(minhaColuna+2 <= 5):
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna+2]
                    self.encontro((minhaLinha+2, minhaColuna+2), peca)
