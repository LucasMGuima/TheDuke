import models.Tile as tl

class Priest(tl.Tile):
    def __init__(self, imagem):
        super().__init__(imagem)

    def mover(self, input: tuple, tamanhoTabuleiro: int) -> bool:
        linha = input[0]
        coluna = input[1]
        self.__acharPosicoesPossiveis(tamanhoTabuleiro)
        print(input)
        if([linha, coluna] in self.posicoesPossiveis):
            self.posicao = (linha, coluna)
            self.mudarLado()
            return True
        return False

    def __acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #lado ativo
            for n in range(tamanhoTabuleiro):
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