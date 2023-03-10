import models.Tile as tl

class Priest(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)

    def acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #lado ativo
            for p in range(tamanhoTabuleiro):
                n = p+1
                if(minhaLinha - n >= 0):
                    if(minhaColuna - n >= 0): self.__salvarPosicao(minhaLinha-n, minhaColuna-n)
                    if(minhaColuna + n <= 5): self.__salvarPosicao(minhaLinha-n, minhaColuna+n)
                if(minhaLinha + n <= 5):
                    if(minhaColuna - n >= 0): self.__salvarPosicao(minhaLinha+n, minhaColuna-n)
                    if(minhaColuna + n <= 5): self.__salvarPosicao(minhaLinha+n, minhaColuna+n)
        elif(self.lado == 1):
            #Lado não ativo
            if(minhaLinha - 1 >= 0):
                if(minhaColuna - 1 >= 0): self.__salvarPosicao(minhaLinha-1, minhaColuna-1)
                if(minhaColuna + 1 <= 5): self.__salvarPosicao(minhaLinha-1, minhaColuna+1)
            if(minhaLinha + 1 <= 5):
                if(minhaColuna - 1 >= 0): self.__salvarPosicao(minhaLinha+1, minhaColuna-1)
                if(minhaColuna + 1 <= 5): self.__salvarPosicao(minhaLinha+1, minhaColuna+1)

            if(minhaLinha - 2 >= 0):
                if(minhaColuna - 2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna-2)
                if(minhaColuna + 2 <= 5): self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
            if(minhaLinha + 2 <= 5):
                if(minhaColuna - 2 >= 0): self.__salvarPosicao(minhaLinha+2, minhaColuna-2)
                if(minhaColuna + 2 <= 5): self.__salvarPosicao(minhaLinha+2, minhaColuna+2)