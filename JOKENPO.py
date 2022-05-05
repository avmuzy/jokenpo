from random import randint
import time
print('#' * 30)
print('Bem vindo ao JOKENPO')
print('#' * 30)
print('''Escolha uma das opcoes
[0] pedra
[1] papel
[2] tesoura''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual a sua jogada?:'))
comp = randint(0, 2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=-'*11)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*11)
if comp == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('JOGADA INVALIDA')

elif comp == 1:
    if jogador == 1:
        print('EMPATOU')
    elif jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVALIDA')

elif comp == 2:
    if jogador == 2:
        print('EMPATOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 0:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVALIDA')
