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