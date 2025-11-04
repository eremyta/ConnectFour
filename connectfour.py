import random

class Tabuleiro():
    def __init__(self):
        self.NUM_LINHAS = 6
        self.NUM_COLUNAS = 7
        self.PECA_VAZIA = '.'
        self.tabuleiro = [
            [self.PECA_VAZIA for _ in range(self.NUM_COLUNAS)] 
            for _ in range(self.NUM_LINHAS)
        ]
    def getLinhalivre(self, coluna):
        for linha in range(self.NUM_LINHAS - 1, -1, -1):
            
            if self.tabuleiro[linha][coluna] == self.PECA_VAZIA:
                return linha
        
        return -1
    
    def tabuleiro_cheio(self):
        linha_topo = self.tabuleiro[0]
        for i in linha_topo:
            if i == self.PECA_VAZIA:
                return False    
        return True

    
    def show_tabuleiro(self):
        print("\n  0 1 2 3 4 5 6")
        print(" +-------------+")
        
        for linha in self.tabuleiro:
            print(f"| {' '.join(linha)} |") 
            
        print(" +-------------+")


    def fazer_jogada(self, linha, coluna, peca):
        self.tabuleiro[linha][coluna] = peca

    def verificar_vitoria(self, linha, coluna, peca):
        if (self._checar_horizontal(linha, peca) or 
            self._checar_vertical(coluna, peca) or
            self._checar_diagonal_principal(linha, coluna, peca) or
            self._checar_diagonal_secundaria(linha, coluna, peca)):
            
            return True
        
        return False
    
    def _checar_horizontal(self,linha,peca):
        contador = 0
        for c in range(self.NUM_COLUNAS):
            if self.tabuleiro[linha][c] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
        return False
    
    def _checar_vertical(self,coluna,peca):
        contador = 0
        for c in range(self.NUM_LINHAS):
            if self.tabuleiro[c][coluna] == peca:
                contador += 1

        

    

class Jogador():
    def __init__(self, nome, peca, tipo='humano'):
        self.nome = nome
        self.peca = peca
        self.tipo = tipo
    
    def obter_jogada(self, tabuleiro):
        pass

class Jogo():
    def __init__(self):
        self.tab = Tabuleiro()
        self.jogador1 = None
        self.jogador2 = None
        self.quemJoga = None
    
    def startJogo(self):
        print("Bem-vindo ao Connect Four (Quatro em Linha)!")
        
        while True:
            try:
                modo = int(input("Escolha o modo de jogo (1: Humano x Humano, 2: Humano x Computador): "))
                modos_aceitos = {
                    1: ('Humano X', 'humano', 'Humano O', 'humano'),
                    2: ('Humano X', 'humano', 'Computador O', 'computador')}
                if modo not in modos_aceitos:
                    raise ValueError('Opção inválida')
                print(f'Iniciando partida {modos_aceitos[modo]}')
                setup = modos_aceitos[modo]
                self.jogador1 = Jogador(setup[0], 'X', setup[1])
                self.jogador2 = Jogador(setup[2], 'O', setup[3])
                print(f"\nPartida iniciada: {self.jogador1.nome} ('X') vs {self.jogador2.nome} ('O')")
                break
            except ValueError as e:
                print(f'Erro {e}. Tente Novamente')
            


        
    
