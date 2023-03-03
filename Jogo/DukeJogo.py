import models.Board as bd
import models.Tile as tl
import pecas.Duke as pDuke

tamanho = 6

board = bd.Board(6)
duke = pDuke.Duke("D")

duke.posicao = (0,3)

#print(duke.informacao(6))

board.posicionarPeca((0,'A'), duke)
board.imprime()
board.posicionarPeca((0,'F'), duke)
board.imprime()

