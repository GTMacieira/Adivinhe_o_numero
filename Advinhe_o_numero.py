#importar a biblioteca random
import random
#importar funções de arquivo apartado
from functions import ch_difficulty
from functions import play

#solicitar o nome do usuário
pl_name = input ("Olá, qual seu nome?\n").capitalize()

difficulty = int(ch_difficulty(pl_name))

# gerar um número aleatório ente 1 e 50 e salvar na variável drawn_n
drawn_n = random.randrange(1, 50)

#define as chances de acordo com a dificuldade escolhida
if difficulty == 1:
    opportunity = 10
elif difficulty == 2:
    opportunity = 6
elif difficulty == 3:
    opportunity = 4
elif difficulty == 4:
    opportunity = 2

points = 100
lost_points = points / opportunity

print(f'{pl_name}, Vamos  escolher um número para você que esta entre 1 e 100.\n\n'
      f'Você terá {opportunity} chances de acertar o nosso número secreto ')

#lista para armazenar o chutes do usuário
attempts = []
while opportunity > 0:
    opportunity = play(drawn_n, pl_name, opportunity, attempts, points)
    points -= lost_points

print(f'Não foi dessa vez.... o número sorteado era {drawn_n} \n'
    'Mas vamos tentar de novo!!!')