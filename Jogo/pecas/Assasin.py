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

        completoDir1 = False
        completoDir2 = False
        completoDir3 = False

        if(self.lado == 0):
            for p in range(tamanhoTabuleiro):
                n = p+2
                if(self.direcao):
                    #se move para cima
                    if(minhaLinha-n >= 0 and not completoDir1):
                        peca: tl.Tile = tabuleiro.grade[minhaLinha-n][minhaColuna]
                        completoDir1 = self.encontro((minhaLinha-n, minhaColuna), peca)

                    if(minhaLinha+n <= 5):
                        if(minhaColuna-n >= 0 and not completoDir2): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+n][minhaColuna-n]
                            completoDir2 = self.encontro((minhaLinha+n, minhaColuna-n), peca)
                        
                        if(minhaColuna+n <= 5 and not completoDir3): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+n][minhaColuna+n]
                            completoDir3 = self.encontro((minhaLinha+n, minhaColuna+n), peca)
                else:
                    #se move pra baixo
                    if(minhaLinha+n <= 5 and not completoDir1):
                        peca: tl.Tile = tabuleiro.grade[minhaLinha+n][minhaColuna]
                        completoDir1 = self.encontro((minhaLinha+n, minhaColuna), peca)

                    if(minhaLinha-n >= 0):
                        if(minhaColuna-n >= 0 and not completoDir2):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-n][minhaColuna-n]
                            completoDir2 = self.encontro((minhaLinha-n, minhaColuna-n), peca)
                        
                        if(minhaColuna+n <= 5 and not completoDir3):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-n][minhaColuna+n]
                            completoDir3 = self.encontro((minhaLinha-n, minhaColuna+n), peca)
        elif(self.lado == 1):
            for p in range(tamanhoTabuleiro):
                n = p+2
                if(self.direcao):
                    if(minhaLinha+2 <= 5 and not completoDir1): 
                        peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna]
                        completoDir1 = self.encontro((minhaLinha+2, minhaColuna), peca)

                    if(minhaLinha-2 >= 0):
                        if(minhaColuna-2 >= 0 and not completoDir2):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna-2]
                            completoDir2 = self.encontro((minhaLinha-2, minhaColuna-2), peca)
                        
                        if(minhaColuna+2 <= 5 and not completoDir3):
                            peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna+2]
                            completoDir3 = self.encontro((minhaLinha-2, minhaColuna+2), peca)
                else:
                    if(minhaLinha-2 >= 0 and not completoDir1):
                        peca: tl.Tile = tabuleiro.grade[minhaLinha-2][minhaColuna]
                        completoDir1 = self.encontro((minhaLinha-2, minhaColuna), peca)

                    if(minhaLinha+2 <= 5):
                        if(minhaColuna-2 >= 0 and not completoDir2): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna-2]
                            completoDir2 = self.encontro((minhaLinha+2, minhaColuna-2), peca)
                        
                        if(minhaColuna+2 <= 5 and not completoDir3): 
                            peca: tl.Tile = tabuleiro.grade[minhaLinha+2][minhaColuna+2]
                            completoDir3 = self.encontro((minhaLinha+2, minhaColuna+2), peca)
        print(self.posicoesPossiveis)