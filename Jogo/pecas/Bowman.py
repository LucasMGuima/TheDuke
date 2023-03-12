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
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
                if(minhaLinha+2 <= 5): 
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                    self.encontro((minhaLinha+2, minhaColuna), peca)
            else:
                #Se move pra baixo
                if(minhaLinha+1 <= 5): 
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    self.encontro((minhaLinha+1, minhaColuna), peca)
                if(minhaLinha-2 >= 0):
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                    self.encontro((minhaLinha-2, minhaColuna), peca)

            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
            if(minhaColuna+2 <= 5): 
                peca = tabuleiro.grade[minhaLinha][minhaColuna+2]
                self.encontro((minhaLinha, minhaColuna+2), peca)
            if(minhaColuna-1 >= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
            if(minhaColuna-2 >= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-2]
                self.encontro((minhaLinha, minhaColuna-2), peca)
        elif(self.lado == 1):
            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)


    def informacao(self):
        return super().informacao()