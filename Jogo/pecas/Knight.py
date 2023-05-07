import models.Tile as tl
import models.Board as bd

class Knight(tl.Tile):
    def __init__(self, imagem: str, jogador):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        #Limpar posições antigas
        self.posicoesPossiveis.clear()

        tamanhoTabuleiro = tabuleiro.tamanho

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado ativo
            #Mov. Horizontal
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha-1, minhaColuna), peca)
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
            
            #Mov que usa como base a direção
            if(self.direcao):
                #Se move para cima
                
                #Mov. para traz
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    encontro = self.encontro((minhaLinha-1, minhaColuna), peca)
                    #So move para o -2 se o -1 estiver livre
                    if(encontro == False and minhaLinha-2 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                        encontro = self.encontro((minhaLinha-1, minhaColuna), peca)
                
                #Salto para a frente
                if(minhaLinha+2 <= 5):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna-1]
                        self.encontro((minhaLinha+2, minhaColuna-1), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna+1]
                        self.encontro((minhaLinha+2, minhaColuna+1), peca)
            else:
                #Se move para baixo

                #Mov. para traz
                if(minhaLinha+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    encontro = self.encontro((minhaLinha+1, minhaColuna), peca)
                    #Se move para o +2 se o +1 estiver livre
                    if(encontro == False and minhaLinha+2 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                        self.encontro((minhaLinha+2, minhaColuna), peca)

                #Salto para frente
                if(minhaLinha-2 >= 0):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna-1]
                        self.encontro((minhaLinha-2, minhaColuna-1), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna+1]
                        self.encontro((minhaLinha-2, minhaColuna+1), peca)
        elif(self.lado == 1):
            #Lado não ativo

            #Mov. depende da direção
            if(self.direcao):
                #Se move pra cima
                for n in range(tamanhoTabuleiro):
                    p = n+1
                    if(minhaLinha-p >= 0):
                        #Percorre o caminho até acabar ou encontrar algo
                        peca = tabuleiro.grade[minhaLinha-p][minhaColuna]
                        encontro = self.encontro((minhaLinha-p, minhaColuna), peca)
                        if(encontro): break
                #Mov na diagonal para traz
                if(minhaLinha+1 <= 5):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                        encontro = self.encontro((minhaLinha+1, minhaColuna-1), peca)
                        #So move para -2 so sé -1 estiver livre
                        if(encontro == False and minhaLinha+2 >= 0):
                            if(minhaColuna-2 >= 0):
                                peca = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                                self.encontro((minhaLinha+2, minhaColuna-2), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                        encontro = self.encontro((minhaLinha+1, minhaColuna+1), peca)
                        #Se mover para +2 so sé +1 estiver livre
                        if(encontro == False and minhaLinha+2 <= 5):
                            if(minhaColuna+2 <= 5):
                                peca = tabuleiro.grade[minhaLinha+2][minhaLinha+2]
                                self.encontro((minhaLinha+2, minhaColuna+2), peca)
            else:
                #Se move para baixo
                for n in range(tamanhoTabuleiro):
                    p = n+1
                    if(minhaLinha+p >= 0):
                        #Perco o caminho até acabar ou econtrar algo
                        peca = tabuleiro.grade[minhaLinha+p][minhaColuna]
                        encontro = self.encontro((minhaLinha+p, minhaColuna), peca)
                        if(encontro): break
                #Mov na diagonal para traz
                if(minhaLinha-1 >= 0):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                        encontro = self.encontro((minhaLinha-1, minhaColuna-1), peca)
                        #So move para -2 so sé -1 estiver livre
                        if(encontro == False and minhaLinha-2 >= 0):
                            if(minhaColuna-2 >= 0):
                                peca = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                                self.encontro((minhaLinha-2, minhaColuna-2), peca)
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                        encontro = self.encontro((minhaLinha-1, minhaColuna+1), peca)
                        #Se mover para +2 so sé +1 estiver livre
                        if(encontro == False and minhaLinha-2 >= 0):
                            if(minhaColuna+2 <= 5):
                                peca = tabuleiro.grade[minhaLinha-2][minhaLinha+2]
                                self.encontro((minhaLinha-2, minhaColuna+2), peca)