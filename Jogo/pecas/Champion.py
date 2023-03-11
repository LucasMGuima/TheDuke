import models.Tile as tl

#TODO
#ATAQUE

class Champion(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #Lado ativo
            if(minhaLinha+1 <= 5): self.__salvarPosicao(minhaLinha+1, minhaColuna)
            if(minhaLinha+2 <= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna)
            if(minhaLinha-1 >= 0): self.__salvarPosicao(minhaLinha-1, minhaColuna)
            if(minhaLinha-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)

            if(minhaColuna+1 <= 5): self.__salvarPosicao(minhaLinha, minhaColuna+1)
            if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha, minhaColuna+2)
            if(minhaColuna-1 >= 0): self.__salvarPosicao(minhaLinha, minhaColuna-1)
            if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha, minhaColuna-2)
        
        elif(self.lado == 1):
            #Lado não-ativo
            if(minhaLinha+2 <= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna)
            if(minhaLinha-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)

            if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha, minhaColuna+2)
            if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha, minhaColuna-2)