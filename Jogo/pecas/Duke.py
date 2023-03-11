import models.Tile as tl
import abc

class Duke(tl.Tile):
    def __init__(self, imagem: str, jogador: str):
        super().__init__(imagem, jogador)
        
    def acharPosicoesPossiveis(self, tamanhoTabuleiro: int) -> None:
        #Limpa a lista de posições posiveis
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            #estado inicial - Move na horizontal
            for n in range(tamanhoTabuleiro):  
                if n != minhaColuna: self.posicoesPossiveis.append([minhaLinha, n])
        elif(self.lado == 1):
            #estado nao-inicial - Move na vertical
            for n in range(tamanhoTabuleiro):
                if n != minhaLinha: self.posicoesPossiveis.append([n, minhaColuna])

        print(self.posicoesPossiveis)

    def informacao(self, tamanhoTabuleiro: int):
        self.__acharPosicoesPossiveis(tamanhoTabuleiro)
        print("-> Duke\n    Pode se mover para", self.posicoesPossiveis)