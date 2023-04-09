import pecas.Assasin as Assasin
import pecas.Bowman as Bowman
import pecas.Champion as Champion
import pecas.Dragoon as Dragoon
import pecas.Duke as Duke
import pecas.Footman as Footman
import pecas.General as General
import pecas.Knight as Knight
import pecas.LongBowman as LongBowman
import pecas.Marshall as Marshall
import pecas.Pikeman as Pikeman
import pecas.Priest as Priest
import pecas.Seer as Seer
import pecas.Wizard as Wizard

import Board as bd
import Tile as tl

class Jogador():
    def __init__(self, jogador: str, direcao: bool) -> None:
        self.nome = jogador
        self.direcao = direcao
        
        #Duke do jogador
        self.Duke

        #pecas em jogo
        self.pecas = []

        #inicia o saco de peças
        self.saco = [
            #1 Footman
            Footman.Footman("F", self.nome, self.direcao),
            #3 Pikeman
            Pikeman.Pikeman("p", self.nome, self.direcao),
            Pikeman.Pikeman("p", self.nome, self.direcao),
            Pikeman.Pikeman("p", self.nome, self.direcao),
            #Knight
            Knight.Knight("K", self.nome, self.direcao),
            #Wizrad
            Wizard.Wizard("W", self.nome, self.direcao),
            #Seer
            Seer.Seer("S", self.nome, self.direcao),
            #General
            General.General("G", self.nome, self.direcao),
            #Priest
            Priest.Priest("P", self.nome, self.direcao),
            #Champion
            Champion.Champion("C", self.nome, self.direcao),
            #Marshall
            Marshall.Marshall("M", self.nome, self.direcao),
            #Bowman
            Bowman.Bowman("B", self.nome, self.direcao),
            #Dragoon
            Dragoon.Dragoon("d", self.nome, self.direcao),
            #Assasin
            Assasin.Assasin("A", self.nome, self.direcao),
            #Longbowman
            LongBowman.LongBowman("L", self.nome, self.direcao),
        ]

    def colocar_duke(self, tabuleiro: bd.Board, peca: Duke.Duke) -> None:
        if(self.direcao):
            #Começa em baixo, logo pode ser colocado nos tiles (5,2) e (5,3)
            print("Escolha onde o Duke ira ser colocado: ")
            print("1. Linha 5, Coluna 2")
            print("2. Linha 5, Coluna 3")
            op = int(input("Entre com o número da opção"))
            while(op != 1 and op != 2):
                print("---------OPÇÃO INVALIDA----------")
                op = int(input("ENTRE COM UMA OPÇÃO VALIDA"))

            if(op == 1):
                peca.posicao = (5,2)
            if(op == 2):
                peca.posicao = (5,3)
            tabuleiro.iniciarPeca(peca)  
        else:
            #Começa em cima, logo pode ser colocado nos tiles (0,2) e (0,3)
            print("Escolha onde o Duke ira ser colocado: ")
            print("1. Linha 0, Coluna 2")
            print("2. Linha 0, Coluna 3")
            op = int(input("Entre com o número da opção"))
            while(op != 1 and op != 2):
                print("---------OPÇÃO INVALIDA----------")
                op = int(input("ENTRE COM UMA OPÇÃO VALIDA"))

            if(op == 1):
                peca.posicao = (0,2)
            if(op == 2):
                peca.posicao = (0,3)
            tabuleiro.iniciarPeca(peca)

        self.Duke = peca
    
    def colocar_peca(self, tabuleiro:bd.Board, peca:tl.Tile, posicao: tuple) -> bool:
        dukeLinha = self.Duke.posicao[0]
        dukeColuna = self.Duke.posicao[1]

        colocarLinha = posicao[0]
        colocarColuna = posicao[1]

        #verifica se a posicao foi selecionada da peca do duke direita 
        if((dukeLinha+1 == colocarLinha) & (dukeColuna == colocarColuna)):
            if(tabuleiro.posicionarPeca(posicao,peca)):
                print(f"Peca posicionada: {posicao}")
                #esquerda
        elif((dukeLinha-1 == colocarLinha) & (dukeColuna == colocarColuna)):
            if(tabuleiro.posicionarPeca(posicao,peca)):
                print(f"Peca posicionada: {posicao}")  
                #baixo
        elif((dukeColuna+1 == colocarColuna) & (dukeLinha == colocarLinha)):
            if(tabuleiro.posicionarPeca(posicao,peca)):
                print(f"Peca posicionada: {posicao}")
        elif((dukeColuna-1 == colocarColuna) & (dukeLinha == colocarLinha)):
            if(tabuleiro.posicionarPeca(posicao,peca)):
                print(f"Peca posicionada: {posicao}")
        else:
            print("Não foi possivel colocar a peca")
            return False

        #Salva a peca na lista de pecas ativas
        self.__salvarPeca(peca)
        return True

    def moverPeca(self, tabuleiro:bd.Board) -> bool:
        """
            Permite ao jogador escolher uma peca para mover, se a peça foi movida com sucesso retona True se não retorna False.
            Se a peca terminar a posiçao sobre uma peca inimiga, ela é capiturada
        """
        #Mostra as pecas que o jogador tem em jogo
        cont = 0
        for peca in self.pecas:
            print(cont + ": " + type(peca))
            cont += 1

        peca: tl.Tile
        #Escolhe a peca, repete se o valor entrado não foi valido
        while True:
            entrada = input("Entre com o numero da peca escolhida: ")
            try:
                num_entrada = int(entrada)
                peca = self.peca[num_entrada]
                break
            except:
                print("O valor entrado não é valido")

        peca.acharPosicoesPossiveis()
        cont = 0
        for posicao in peca.posicoesPossiveis:
            print(cont +": "+ posicao)
            cont += 1

        posicao: tuple
        while True:
            entrada = input("Entre com o numero da posicao escolhida")
            try:
                num_entrada = int(entrada)
                posicao = peca.posicoesPossiveis[num_entrada]
                break
            except:
                print("O valor entrado não é valido")
    
        return peca.mover(posicao, tabuleiro)

    def __salvarPeca(self, peca:tl.Tile) -> None:
        self.pecas.append(peca)
        return
