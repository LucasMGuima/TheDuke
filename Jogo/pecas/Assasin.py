import models.Tile as tl

class Assasin(tl.Tile):
    def __init__(self, imagem: str, jogador: str, direcao: bool):
        super().__init__(imagem, jogador)
        self.direcao = direcao

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

    def __acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> bool:
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            for n in range(tamanhoTabuleiro):
                if(self.direcao):
                    #se move para cima
                    if(minhaLinha-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)
                    if(minhaLinha+2 <= 5):
                        if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha+2, minhaColuna-2)
                        if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
                else:
                    #se move pra baixo
                    if(minhaLinha+2 <= 0): self.__salvarPosicao(minhaLinha+2, minhaColuna)
                    if(minhaLinha-2):
                        if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna-2)
                        if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
        elif(self.lado == 1):
            for n in range(tamanhoTabuleiro):
                if(self.direcao):
                    if(minhaLinha+2 <= 0): self.__salvarPosicao(minhaLinha+2, minhaColuna)
                    if(minhaLinha-2):
                        if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna-2)
                        if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
                else:
                    if(minhaLinha-2 >= 0): self.__salvarPosicao(minhaLinha-2, minhaColuna)
                    if(minhaLinha+2 <= 5):
                        if(minhaColuna-2 >= 0): self.__salvarPosicao(minhaLinha+2, minhaColuna-2)
                        if(minhaColuna+2 <= 5): self.__salvarPosicao(minhaLinha-2, minhaColuna+2)
        
        elif(self.lado == 1):
            return