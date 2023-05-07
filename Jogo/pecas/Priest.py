import models.Tile as tl
import models.Board as bd

class Priest(tl.Tile):
    def __init__(self, imagem: str, jogador):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        self.posicoesPossiveis.clear()

        tamanhoTabuleiro = tabuleiro.tamanho

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #lado ativo
            for p in range(tamanhoTabuleiro):
                n = p+1
                if(minhaLinha - n >= 0):
                    if(minhaColuna - n >= 0): 
                        peca = tabuleiro.grade[minhaLinha-n][minhaColuna-n]
                        self.encontro((minhaLinha-n, minhaColuna-n), peca)
                    if(minhaColuna + n <= 5): 
                        peca = tabuleiro.grade[minhaLinha-n][minhaColuna+n]
                        self.encontro((minhaLinha-n, minhaColuna+n), peca)
                if(minhaLinha + n <= 5):
                    if(minhaColuna - n >= 0): 
                        peca = tabuleiro.grade[minhaLinha+n][minhaColuna-n]
                        self.encontro((minhaLinha+n, minhaColuna-n), peca)
                    if(minhaColuna + n <= 5): 
                        peca = tabuleiro.grade[minhaLinha+n][minhaColuna+n]
                        self.encontro((minhaLinha+n, minhaColuna+n), peca)
        elif(self.lado == 1):
            #Lado não ativo
            if(minhaLinha - 1 >= 0):
                if(minhaColuna - 1 >= 0): 
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.encontro((minhaLinha-1, minhaColuna-1), peca)
                if(minhaColuna + 1 <= 5): 
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                    self.encontro((minhaLinha-1, minhaColuna+1), peca)
            if(minhaLinha + 1 <= 5):
                if(minhaColuna - 1 >= 0): 
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.encontro((minhaLinha+1, minhaColuna-1), peca)
                if(minhaColuna + 1 <= 5): 
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.encontro((minhaLinha+1, minhaColuna+1), peca)

            if(minhaLinha - 2 >= 0):
                if(minhaColuna - 2 >= 0): 
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                    self.encontro((minhaLinha-2, minhaColuna-2), peca)
                if(minhaColuna + 2 <= 5): 
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                    self.encontro((minhaLinha-2, minhaColuna+2), peca)
            if(minhaLinha + 2 <= 5):
                if(minhaColuna - 2 >= 0): 
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                    self.encontro((minhaLinha+2, minhaColuna-2), peca)
                if(minhaColuna + 2 <= 5): 
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna+2]
                    self.encontro((minhaLinha+2, minhaColuna+2), peca)