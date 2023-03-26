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
            #Mov. Horizontal
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                encontro = self.encontro((minhaLinha, minhaColuna-1), peca)
                if(not encontro):
                    if(minhaColuna-2 >= 0):
                        peca = tabuleiro.grade[minhaLinha][minhaColuna-2]
                        self.encontro((minhaLinha, minhaColuna-2), peca)
            if(minhaColuna+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                    encontro = self.encontro((minhaLinha, minhaColuna+1), peca)
                    if(not encontro):
                        if(minhaColuna+2 <= 0):
                            peca = tabuleiro.grade[minhaLinha][minhaColuna+2]
                            self.encontro((minhaLinha, minhaColuna+2), peca)
            
            #Mov. Vertical
            if(minhaLinha-1 >= 0):
                peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.encontro((minhaLinha-1, minhaColuna), peca)
            if(minhaLinha+1 <= 5):
                peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                self.encontro((minhaLinha+1, minhaColuna), peca)
            
            #Mov. Diagonal
            #Varia com adireção
            if(self.direcao):
                #Se move para cima
                if(minhaLinha-2 >= 0):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna-1]
                        self.encontro((minhaLinha-2, minhaColuna-1), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna+1]
                        self.encontro((minhaLinha-2, minhaColuna+1), peca)
            else:
                #Se move para baixo
                if(minhaLinha+2 <= 5):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna-1]
                        self.encontro((minhaLinha+2, minhaColuna-1), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna+1]
                        self.encontro((minhaLinha+2, minhaColuna+1), peca)
        elif(self.lado == 1):
            #Lado não ativo
            #Mov. Horizontal
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                econtro = self.encontro((minhaLinha, minhaColuna-1), peca)
                #Anda até o -2
                if(not encontro and minhaColuna-2 >= 0):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna-2]
                    self.encontro((minhaLinha, minhaColuna-2), peca)
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                econtro = self.encontro((minhaLinha, minhaColuna+1), peca)
                #Anda até o +2
                if(not encontro and minhaColuna+2 >= 0):
                    peca = tabuleiro.grade[minhaLinha][minhaColuna+2]
                    self.encontro((minhaLinha, minhaColuna+2), peca)
            
            #Mov dependendo da direção
            if(self.direcao):
                #Se move pra cima
                #Mov. Horizontal
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
                
                #Mov. Diagonal
                if(minhaLinha-2 >= 0):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna-1]
                        self.encontro((minhaLinha-2, minhaColuna-1), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna+1]
                        self.encontro((minhaLinha-2, minhaColuna+1), peca)
            else:
                #Se move para baixo
                #Mov. Horizontal
                if(minhaLinha+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    self.encontro((minhaLinha+1, minhaColuna), peca)

                #Mov. Diagonal
                if(minhaLinha+2 <= 5):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna-1]
                        self.encontro((minhaLinha+2, minhaColuna-1), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna+1]
                        self.encontro((minhaLinha+2, minhaColuna+1), peca)

    def regiaoDeComando(self, tabuleiro: bd.Board) -> None:
        #Limpa a lsita de comandaveis
        self.pecasComandaveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 1):
            #Só comando no estado não-ativo
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.comandavel(peca)
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.comandavel(peca)

            #Depende da driecao
            if(self.direcao):
                # Se move par cima 
                if(minhaLinha+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    self.comandavel(peca)
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                        self.comandavel(peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                        self.comandavel(peca)
            else:
                #Peca se move para baixo
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.comandavel(peca)
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                        self.comandavel(peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                        self.comandavel(peca)