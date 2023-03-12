import models.Board as bd
import models.Tile as tl
import pecas.Duke as pDuke
import pecas.Assasin as pAssasin

tamanho = 6

board = bd.Board(6)
duke = pDuke.Duke("D", "J1")
assasin = pAssasin.Assasin("A", "J1", False)

assasin.posicao = (0,4)
duke.posicao = (0,3)

board.iniciarPeca(duke)
board.iniciarPeca(assasin)

#print(duke.informacao(6))

#duke.acharPosicoesPossiveis(board)
assasin.acharPosicoesPossiveis(board)
print(board.posicionarPeca((2, 'E'), assasin))
#espaco = board.posicionarPeca((0,'A'), duke)
board.imprime()