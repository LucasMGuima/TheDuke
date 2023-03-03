import models.Tile as tl

class Footman(tl.Tile):
    def __init__(self, imagem, direcao: bool):
        super().__init__(imagem)
        self.direcao = direcao

    def __acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #estado inicail
            if(minhaColuna+1 <= 5):
                self.__salvarPosicao(minhaLinha, minhaColuna+1)
            if(minhaColuna-1 >= 0):
                self.__salvarPosicao(minhaLinha, minhaColuna-1)
            
            if(minhaLinha+1 <= 5):
                self.__salvarPosicao(minhaLinha+1, minhaColuna)
            if(minhaLinha-1 >= 0):
                self.__salvarPosicao(minhaLinha-1, minhaColuna)
        elif(self.lado  == 1):
            #estado nao-inicial
            if(minhaLinha+1 <= 5):
                if(minhaColuna+1 <= 5): self.__salvarPosicao(minhaLinha+1, minhaColuna+1)
                if(minhaColuna-1 >= 0): self.__salvarPosicao(minhaLinha+1, minhaColuna-1)
            
            if(minhaLinha-1 >= 0):
                if(minhaColuna+1 <= 5): self.__salvarPosicao(minhaLinha-1, minhaColuna+1)
                if(minhaColuna-1 >= 0): self.__salvarPosicao(minhaLinha-1, minhaColuna-1)

            if(self.direcao):
                #Se move pra cima
                if(minhaLinha-2 <= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)
            else:
                #Se move pra baixo
                if(minhaLinha+2 >= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna) 

    def informacao(self):
        return super().informacao()