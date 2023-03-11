import models.Tile as tl
import models.Board as bd

class Assasin(tl.Tile):
    def __init__(self, imagem: str, jogador: str, direcao: bool):
        super().__init__(imagem, jogador)
        self.direcao = direcao

    def acharPosicoesPossiveis(self, tabuleiro: bd.Board) -> bool:
        tamanhoTabuleiro = tabuleiro.tamanho
        self.posicoesPossiveis.clear()

        minhaLinha = self.posicao[0]
        minhaColuna = self.posicao[1]

        if(self.lado == 0):
            completoDir1 = False
            completoDir2 = False
            completoDir3 = False

            for n in range(tamanhoTabuleiro):
                if(self.direcao):
                    #se move para cima
                    if(minhaLinha-2 >= 0 and not completoDir1):
                        peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna]
                        completoDir1 = self.__encotro((minhaLinha-2, minhaColuna), peca)

                    if(minhaLinha+2 <= 5):
                        if(minhaColuna-2 >= 0 and not completoDir2): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                            completoDir2 = self.__encotro((minhaLinha+2, minhaColuna-2), peca)
                        
                        if(minhaColuna+2 <= 5 and not completoDir3): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna+2]
                            completoDir3 = self.__encotro((minhaLinha+2, minhaColuna+2), peca)
                else:
                    #se move pra baixo
                    if(minhaLinha+2 <= 5 and not completoDir1): 
                        peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna]
                        completoDir1 = self.__encotro((minhaLinha+2, minhaColuna), peca)

                    if(minhaLinha-2 >= 0):
                        if(minhaColuna-2 >= 0 and not completoDir2):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                            completoDir2 = self.__encotro((minhaLinha-2, minhaColuna-2), peca)
                        
                        if(minhaColuna+2 <= 5 and not completoDir3):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                            completoDir3 = self.__encotro((minhaLinha-2, minhaColuna+2), peca)

        elif(self.lado == 1):
            for n in range(tamanhoTabuleiro):
                if(self.direcao):
                    if(minhaLinha+2 <= 5 and not completoDir1): 
                        peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna]
                        completoDir1 = self.__encotro((minhaLinha+2, minhaColuna), peca)

                    if(minhaLinha-2 >= 0):
                        if(minhaColuna-2 >= 0 and not completoDir2):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                            completoDir2 = self.__encotro((minhaLinha-2, minhaColuna-2), peca)
                        
                        if(minhaColuna+2 <= 5 and not completoDir3):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                            completoDir3 = self.__encotro((minhaLinha-2, minhaColuna+2), peca)
                else:
                    if(minhaLinha-2 >= 0 and not completoDir1):
                        peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna]
                        completoDir1 = self.__encotro((minhaLinha-2, minhaColuna), peca)

                    if(minhaLinha+2 <= 5):
                        if(minhaColuna-2 >= 0 and not completoDir2): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                            completoDir2 = self.__encotro((minhaLinha+2, minhaColuna-2), peca)
                        
                        if(minhaColuna+2 <= 5 and not completoDir3): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna+2]
                            completoDir3 = self.__encotro((minhaLinha+2, minhaColuna+2), peca)
        
        elif(self.lado == 1):
            return