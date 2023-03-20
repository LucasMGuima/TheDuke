import models.Tile as tl
import models.Board as bd

class LongBowman(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> None:
        tamanhoTabuleiro = tabuleiro.tamanho

        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            if(self.direcao):
                #Se move para cima
                if(minhaLinha-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha-1][minhaColuna]
                    self.encontro((minhaLinha-1, minhaColuna), peca)
            else:
                #Se move para baixo
                if(minhaLinha+1 < tamanhoTabuleiro):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna]
                    self.encontro((minhaLinha+1, minhaColuna), peca)

            #Se move para a direita
            if(minhaColuna+1 < tamanhoTabuleiro):
                peca = tabuleiro.grade[minhaLinha][minhaColuna+1]
                self.encontro((minhaLinha, minhaColuna+1), peca)
            
            #Se move para a esquerda
            if(minhaColuna-1 >= 0):
                peca = tabuleiro.grade[minhaLinha][minhaColuna-1]
                self.encontro((minhaLinha, minhaColuna-1), peca)

        elif(self.lado == 1):
            if(self.direcao == False):
                 # diagonal baixo esquerda
                if(minhaLinha+1 <= tamanhoTabuleiro-1 and minhaColuna-1 >= 0):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna-1]
                    self.encontro((minhaLinha+1, minhaColuna-1), peca)
                # diagonal baixo direita
                if(minhaLinha+1 <= tamanhoTabuleiro-1 and minhaColuna+1 <= tamanhoTabuleiro-1):
                    peca = tabuleiro.grade[minhaLinha+1][minhaColuna+1]
                    self.encontro((minhaLinha+1, minhaColuna+1), peca)

    def acharAlcanceAtaque(self) -> None:
        #Limpa o alcance antigo do ataque
        self.alcanceAtaque.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 1):
            #Só ataca no estado não-ativo
            if(self.direcao):
                #Se move para cima
                if(minhaLinha-2 >= 0):
                    self.alcanceAtaque.append((minhaLinha-2, minhaColuna))
                if(minhaLinha-3 >= 0):
                    self.alcanceAtaque.append((minhaLinha-3, minhaColuna))
            else:
                #Se move para baixo
                if(minhaLinha+2 <= 5):
                    self.alcanceAtaque.append((minhaLinha+2, minhaColuna))
                if(minhaLinha+3 <= 5):
                    self.alcanceAtaque.append((minhaLinha+3, minhaColuna))

    def informacao(self):
        return super().informacao()
