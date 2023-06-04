import models.Board as bd
import models.Jogador as jg
from pecas.Pikeman import Pikeman
from pecas.Duke import Duke

class JogoDuke():
    def __init__(self) -> None:
        self.board = bd.Board(6)
        self.jogador1 = jg.Jogador("Jogoadr 1", True)
        self.jogador2 = jg.Jogador("Jogoadr 2", False)

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

    def __oponentePerdeu(self, oponente)->bool:
        for peca in oponente.pecas:
            if(type(peca) == Duke): return True
        return False

    def loopJogo(self) -> bool:
        # Comeco rodada, returna false se o jogo acabou
        #jogador1
        escolha = self.__escolherAcao()
        if(escolha == 1):
            #pegar peca
            self.jogador1.novaPeca(self.board)
        elif(escolha == 2):
            #mover uma peca
            self.jogador1.moverPeca(self.board)

        #Chega se o jogador2 perdeu o duke
        if(self.__oponentePerdeu(self.jogador2)):
            return False
        
        #jogador2
        escolha = self.__escolherAcao()
        if(escolha == 1):
            #pegar peca
            self.jogador2.novaPeca(self.board)
        elif(escolha == 2):
            #mover uma peca
            self.jogador2.moverPeca(self.board)

        #Chega se o jogador1 perdeu o duke
        if(self.__oponentePerdeu(self.jogador1)):
            return False
        
        return True

    def __escolherAcao(self) -> int:
        # opcoes
        print("Ações:")
        print("1 - Pegar nova peça")
        print("2 - Mover peça")
        op = input("Número da opção escolhida: ")
        return op
