import models.Board as bd
import models.Tile as tl
import pecas.Duke as pDuke
import pecas.Assasin as pAssasin
import pecas.Bowman as pBowman
import pecas.Footman as pFootman

tamanho = 6

board = bd.Board(6)
duke = pDuke.Duke("D", "J1")
assasin = pAssasin.Assasin("A", "J1", False)
bowman = pBowman.Bowman("B", "J1")
footman = pFootman.Footman("f", "J2", False)

assasin.posicao = (0,4)
duke.posicao = (0,3)
bowman.posicao = (3,2)
footman.posicao = (2,2)

board.iniciarPeca(duke)
board.iniciarPeca(assasin)
board.iniciarPeca(bowman)
board.iniciarPeca(footman)

#print(duke.informacao(6))

#duke.acharPosicoesPossiveis(board)
#assasin.acharPosicoesPossiveis(board)
footman.acharPosicoesPossiveis(board)
#print(board.posicionarPeca((2, 'E'), assasin))
#board.posicionarPeca((2, 'E'), assasin)
#board.posicionarPeca((2, 'B'), bowman)
#espaco = board.posicionarPeca((0,'A'), duke)
board.imprime()