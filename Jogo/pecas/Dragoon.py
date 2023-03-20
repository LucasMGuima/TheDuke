import models.Tile as tl
import models.Board as bd

#TODO
#ATAQUE

class Dragoon(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)
    
    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        tamanhoTabuleiro = tabuleiro.tamanho

        if(self.lado == 0):
            #Lado ativo
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)

        elif(self.lado == 1):
            #Lado não-ativo
            #Movimento baseado na direção
            if(self.direcao):
                #Se move para cima
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    encontro = self.encontro((minhaLinha-1, minhaColuna), peca)
                    #So se move pro -2 se o -1 estiver livre
                    if(encontro == False and minhaLinha-2 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                        self.encontro((minhaLinha-2, minhaColuna), peca)
                if(minhaLinha-2 >= 0):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna-1]
                        self.encontro((minhaLinha-2, minhaColuna-1))
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha-2][minhaColuna+1]
                        self.encontro((minhaLinha-2, minhaColuna+1), peca)
                #Diagonal 
                for p in range(tamanhoTabuleiro):
                    n = p+1
                    if(minhaLinha+n <= 5):
                        if(minhaColuna-n >= 0):
                            peca = tabuleiro.grade[minhaLinha+n][minhaColuna-n]
                            self.encontro((minhaLinha+n, minhaColuna-n), peca)
                        if(minhaColuna+n <= 5):
                            peca = tabuleiro.grade[minhaLinha+n][minhaColuna+n]
                            self.encontro((minhaLinha+n, minhaColuna+n), peca)

            else:
                #Se move para baixo
                if(minhaLinha+1 <= 5):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    encontro = self.encontro((minhaLinha+1, minhaColuna), peca)
                    #So se move pro +2 se o +1 estiver livre
                    if(encontro == False and minhaLinha+2 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                        self.encontro((minhaLinha+2, minhaColuna), peca)
                if(minhaLinha+2 <= 5):
                    if(minhaColuna-1 >= 0):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna-1]
                        self.encontro((minhaLinha+2, minhaColuna-1))
                    if(minhaColuna+1 <= 5):
                        peca = tabuleiro.grade[minhaLinha+2][minhaColuna+1]
                        self.encontro((minhaLinha+2, minhaColuna+1), peca)
                #Diagonal 
                for p in range(tamanhoTabuleiro):
                    n = p+1
                    if(minhaLinha-n >= 0):
                        if(minhaColuna-n >= 0):
                            peca = tabuleiro.grade[minhaLinha-n][minhaColuna-n]
                            self.encontro((minhaLinha-n, minhaColuna-n), peca)
                        if(minhaColuna+n <= 5):
                            peca = tabuleiro.grade[minhaLinha-n][minhaColuna+n]
                            self.encontro((minhaLinha-n, minhaColuna+n), peca)

    def acharAlcanceAtaque(self) -> None:
        #Limpa a alcance
        self.alcanceAtaque.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Só ataca no lado ativo
            #Depende da direção
            if(self.direcao):
                #Se move para cima
                if(minhaLinha-2 >= 0):
                    self.alcanceAtaque.append((minhaLinha-2, minhaColuna))
                    if(minhaColuna-2 >= 0):
                        self.alcanceAtaque.append((minhaLinha-2, minhaColuna-2))
                    if(minhaColuna+2 <= 5):
                        self.alcanceAtaque.append((minhaLinha-2, minhaColuna+2)) 
            return