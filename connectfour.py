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
    
    
    def showTabuleiro(self):
        print("\n  0 1 2 3 4 5 6")
        print(" +-------------+")
        
        for linha in self.tabuleiro:
            print(f"| {' '.join(linha)} |") 
            
        print(" +-------------+")


    def fazer_jogada(self, linha, coluna, peca):
        self.tabuleiro[linha][coluna] = peca

    
tab1 = Tabuleiro()
tab1.showTabuleiro()

class Jogador():
    def __init__(self, nome, peca, tipo='humano'):
        pass

        
    