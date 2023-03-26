import models.Tile as tl
import models.Board as bd

class Marshall(tl.Tile):
    def __init__(self, imagem: str, jogador: str, direcao: bool):
        super().__init__(imagem, jogador)
        self.direcao = direcao

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        #Limpar as posições antigas
        self.posicoesPossiveis.clear()

        tamanhoTabuleiro = tabuleiro.tamanho

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado ativo
            #Mov horizontal
            for n in range(tamanhoTabuleiro):
                p = n+1
                if(minhaColuna-p >= 0):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna-p]
                    self.encontro((minhaLinha, minhaColuna-p), peca)
                if(minhaColuna+p <= 5):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna+p]
                    self.encontro((minhaLinha, minhaColuna+p), peca)
            
            #Mov. baseado na direção que encara
            if(self.direcao):
                #Se move pra cima no tabuleiro

                #Mov. Vertical
                if(minhaLinha-2 >= 0):
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                    self.encontro((minhaLinha-2, minhaColuna), peca)

                #Mov. Diagonal
                if(minhaLinha+2 <= 5):
                    if(minhaColuna-2 >= 0):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                        self.encontro((minhaLinha+2, minhaColuna-2), peca)
                    if(minhaColuna+2 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna+2]
                        self.encontro((minhaLinha+2, minhaColuna+2), peca)
            else:
                #Se move pra baixo no tabuleiro

                #Mov. Verical
                if(minhaLinha+2 <= 5):
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                    self.encontro((minhaLinha+2, minhaColuna), peca)

                #Mov. Diagonal
                if(minhaLinha-2 >= 0):
                    if(minhaColuna-2 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                        self.encontro((minhaLinha-2, minhaColuna-2), peca)
                    if(minhaColuna+2 <= 5):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                        self.encontro((minhaLinha-2, minhaColuna+2), peca)
        elif(self.lado == 1):
            #Lado não ativo
            #TODO Logica de comando
            #Mov. Horizontal
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
                #So pode chegar no -2 se passar pelo -1, Anada até o -2
                if(minhaColuna-2 >= 0):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna-2]
                    self.encontro((minhaLinha, minhaColuna-2), peca)
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
                #So pode chegar no +2 se passar pelo +1, Anda até o +2
                if(minhaColuna+2 <= 5):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna+2]
                    self.encontro((minhaLinha, minhaColuna+2), peca)
            
            #Mov dependente da direção
            if(self.direcao):
                #Se move para cima no tabuleiro
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
            else:
                #Se move para baixo no tabuleiro
                if(minhaLinha+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    self.encontro((minhaLinha+1, minhaColuna), peca)
            
            #Mov. Diagonal
            if(minhaLinha-1 >= 0):
                if(minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.encontro((minhaLinha-1, minhaColuna-1), peca)
                if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                    self.encontro((minhaLinha-1, minhaColuna+1), peca)
            if(minhaLinha+1 <= 5):
                if(minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.encontro((minhaLinha+1, minhaColuna-1), peca)
                if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.encontro((minhaLinha+1, minhaColuna+1), peca)

    def regiaoDeComando(self, tabuleiro: bd.Board) -> None:
        #limpa a antiga regiao
        self.pecasComandaveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        #Depende da direção
        if(self.direcao):
            #Se move para cima
            if(minhaLinha-1 >= 0):
                peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.comandavel(peca)
                if(minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.comandavel(peca)
                if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                    self.comandavel(peca)
        else:
            #Se move para baixo
            if(minhaLinha+1 <= 5):
                peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                self.comandavel(peca)
                if(minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.comandavel(peca)
                if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.comandavel(peca)