import models.Tile as tl
import models.Board as bd

class Footman(tl.Tile):
    def __init__(self, imagem:str, jogador: str, direcao: bool):
        super().__init__(imagem, jogador)
        self.direcao = direcao

    def acharPosicoesPossiveis(self, tabuleiro: int) -> None:
        tamanhoTabuleiro = tabuleiro.tamanho

        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #estado inicail
            if(minhaColuna+1 <= 5):
                #self.__salvarPosicao(minhaLinha, minhaColuna+1)
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
            if(minhaColuna-1 >= 0):
                #self.__salvarPosicao(minhaLinha, minhaColuna-1)
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
            
            if(minhaLinha+1 <= 5):
                #self.__salvarPosicao(minhaLinha+1, minhaColuna)
                peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                self.encontro((minhaLinha+1, minhaColuna), peca)
                
            if(minhaLinha-1 >= 0):
                #self.__salvarPosicao(minhaLinha-1, minhaColuna)
                peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                self.encontro((minhaLinha-1, minhaColuna), peca)
        elif(self.lado  == 1):
            #estado nao-inicial
            if(minhaLinha+1 <= 5):
                if(minhaColuna+1 <= 5): #self.__salvarPosicao(minhaLinha+1, minhaColuna+1)
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.encontro((minhaLinha+1, minhaColuna+1), peca)
                if(minhaColuna-1 >= 0): #self.__salvarPosicao(minhaLinha+1, minhaColuna-1)
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.encontro((minhaLinha+1, minhaColuna-1), peca)
            
            if(minhaLinha-1 >= 0):
                if(minhaColuna+1 <= 5): #self.__salvarPosicao(minhaLinha-1, minhaColuna+1)
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna+1]
                    self.encontro((minhaLinha-1, minhaColuna+1), peca)
                if(minhaColuna-1 >= 0): #self.__salvarPosicao(minhaLinha-1, minhaColuna-1)
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna-1]
                    self.encontro((minhaLinha-1, minhaColuna-1), peca)

            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-2 <= 0): #self.__salvarPosicao(minhaLinha-2, minhaColuna)
                    peca = tabuleiro.grade[minhaLinha-2][minhaColuna]
                    self.encontro((minhaLinha-2, minhaColuna), peca)
            else:
                #Se move pra baixo
                if(minhaLinha+2 >= 5): #self.__salvarPosicao(minhaLinha+2, minhaColuna) 
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                    self.encontro((minhaLinha+2, minhaColuna), peca)
        print(self.posicoesPossiveis)
            

    def informacao(self):
        return super().informacao()