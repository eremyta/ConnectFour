import random
from typing import List, Tuple, Optional
from tabuleiro import Tabuleiro
from jogador import Jogador

class Jogo():
    tab: 'Tabuleiro'
    jogador1: Optional['Jogador'] = None
    jogador2: Optional['Jogador'] = None
    quemJoga: Optional['Jogador'] = None

    def __init__(self) -> None:
        self.tab = Tabuleiro()
    
    def comeca_jogo(self) -> None:
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
    
    def obter_jogada(self) -> Tuple[int,int]:
        jogador = self.quemJoga
        if jogador is None:
            raise ValueError("Erro de lógica: jogador atual não pode ser None no turno.")
        
        if jogador.tipo == 'humano':
            while True:
                try:
                    coluna =  int(input(f'Vez de {jogador.nome}. Escolha uma coluna livre'))
                    if not (0 <= coluna < self.tab.NUM_COLUNAS):
                        print("Erro: Coluna fora do intervalo (0 a 6). Tente novamente.")
                        continue
                    linha_livre = self.tab.obter_linha_livre(coluna)
                    if linha_livre == -1:
                        print('Essa coluna está preenchida. Digite outra coluna')
                        continue

                    return linha_livre,coluna
                except ValueError:
                    print('Entrada inválida, por favor digite um número de 0 a 6')
        elif jogador.tipo == 'computador':
            

   
