
class Tabuleiro():
    def __init__(self) -> None:
        self.NUM_LINHAS = 6
        self.NUM_COLUNAS = 7
        self.PECA_VAZIA = '.'
        self.tabuleiro = [
            [self.PECA_VAZIA for _ in range(self.NUM_COLUNAS)] 
            for _ in range(self.NUM_LINHAS)
        ]
    def obter_linha_livre(self, coluna: int) -> int:
        for linha in range(self.NUM_LINHAS - 1, -1, -1):
            
            if self.tabuleiro[linha][coluna] == self.PECA_VAZIA:
                return linha
        
        return -1
    
    def tabuleiro_cheio(self) -> bool:
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


    def fazer_jogada(self, linha:int, coluna:int, peca:str):
        self.tabuleiro[linha][coluna] = peca

    def verificar_vitoria(self, linha:int, coluna:int, peca:str) -> bool:
        if (self._checar_horizontal(linha, peca) or 
            self._checar_vertical(coluna, peca) or
            self._checar_diagonal_principal(linha, coluna, peca) or
            self._checar_diagonal_secundaria(linha, coluna, peca)):
            
            return True
        
        return False
    
    def _checar_horizontal(self,linha:int,peca:str) -> bool:
        contador = 0
        for c in range(self.NUM_COLUNAS):
            if self.tabuleiro[linha][c] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
        return False
    
    def _checar_vertical(self,coluna:int,peca:str) -> bool:
        contador = 0
        for c in range(self.NUM_LINHAS):
            if self.tabuleiro[c][coluna] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
        return False
    
    def _checar_diagonal_principal(self,coluna:int,linha:int,peca:str) -> bool:
        temp_lin, temp_col = linha, coluna
        
        while temp_lin > 0 and temp_col > 0:
            temp_lin -= 1
            temp_col -= 1
        
      
        contador = 0

        while temp_lin < self.NUM_LINHAS and temp_col < self.NUM_COLUNAS:
            
            if self.tabuleiro[temp_lin][temp_col] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
            
           
            temp_lin += 1
            temp_col += 1
            
        return False
    
    def _checar_diagonal_secundaria(self,coluna:int,linha:int,peca:str) -> bool:
        pass