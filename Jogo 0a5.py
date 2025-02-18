from random import randint
from time import sleep
computador = randint(0, 5) # Faz o Computador "Pensar"
print('-=-' *10)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta advinhar
print('Processando...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Voçê conseguiu me vencer! Eu pensei no número {}!'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

