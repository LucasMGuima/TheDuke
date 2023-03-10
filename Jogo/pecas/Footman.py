import models.Tile as tl
import models.Board as bd

class Footman(tl.Tile):
    def __init__(self, imagem:str, jogador: str, direcao: bool):
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

    def __acharPosicoesPossiveis(self, ttamanhoTabuleiro: int) -> None:
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