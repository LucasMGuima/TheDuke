import models.Board as bd
from models.Jogador import Jogador as jogador
from pecas.Pikeman import Pikeman

class Jogo():
    def __init__(self) -> None:
        self.board = bd.Board(6)
        self.jogador1 = jogador("Jogoadr 1", True)
        self.jogador2 = jogador("Jogoadr 2", False)

    def iniciarJogo(self) -> None:
        # Jogadores colocam o duke no tabuleiro e dois pikeman
        self.jogador1.colocar_duke(self.board)
        self.jogador2.colocar_duke(self.board)

        pikeman = Pikeman("p", self.jogador1)
        self.jogador1.colocar_peca(self.board, pikeman, self.jogador1.direcao)
        pikeman = Pikeman("p", self.jogador2)
        self.jogador2.colocar_peca(self.board, pikeman, self.jogador2.direcao)
        pikeman = Pikeman("p", self.jogador1)
        self.jogador1.colocar_peca(self.board, pikeman, self.jogador1.direcao)
        pikeman = Pikeman("p", self.jogador2)
        self.jogador2.colocar_peca(self.board, pikeman, self.jogador2.direcao)