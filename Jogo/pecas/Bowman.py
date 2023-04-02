import models.Tile as tl
import models.Board as bd

class Bowman(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)

    
    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        tamanhoTabuleiro = tabuleiro.tamanho

        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 1):
            #Estado inicial
            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-1 <= 5): 
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
                
            else:
                #Se move pra baixo
                #
                if(minhaLinha+2 <= 5): 
                    peca = tabuleiro.grade[minhaLinha+2][minhaColuna]
                    self.encontro((minhaLinha+2, minhaColuna), peca)
                

                
                

#direita
            if(minhaColuna+1 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
            if(minhaColuna+2 <= 5):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+2), peca)

#esquerda
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)
            if(minhaColuna-2 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-2), peca)
           
#outro lado
        elif(self.lado == 0):
            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
            else:
                #diagonal baixo direita
                if((minhaLinha+1 <= 5) & (minhaColuna+1 <= 5)):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.encontro((minhaLinha+1, minhaColuna+1), peca)
#esquerda
                if((minhaLinha+1 >= 0) & (minhaColuna-1 >= 0)):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.encontro((minhaLinha+1, minhaColuna-1), peca)
        print(self.posicoesPossiveis)
        

    def acharAlcanceAtaque(self)->None:
        #Limpa a lista de posições de ataque
        self.alcanceAtaque.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 1):
            #Só ataca no lado não-ativo
            #Depende da direção de movimento
            if(self.direcao):
                #Ataca para cima
                if(minhaLinha-1 >= 0):
                    if(minhaColuna-1 >= 0):
                        self.alcanceAtaque.append((minhaLinha-1, minhaColuna-1))
                    if(minhaColuna+ 1 <= 5):
                        self.alcanceAtaque.append((minhaLinha-1, minhaColuna+1))
                if(minhaLinha-2 >= 0):
                    self.alcanceAtaque.append((minhaLinha-2, minhaColuna))
            else:
                #Ataca para baixo
                if(minhaLinha+1 <= 5):
                    if(minhaColuna-1 >= 0):
                        self.alcanceAtaque.append((minhaLinha+1, minhaColuna-1))
                    if(minhaColuna+ 1 <= 5):
                        self.alcanceAtaque.append((minhaLinha+1, minhaColuna+1))
                if(minhaLinha+2 <= 5):
                    self.alcanceAtaque.append((minhaLinha+2, minhaColuna))

    def informacao(self):
        return super().informacao()