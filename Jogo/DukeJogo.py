import models.Board as bd
import models.Tile as tl

tamanho = 6

board = bd.Board(6)
board.posicionarPeca(('A',1), tl.Tile("⬜"))
board.imprime()