#importar a biblioteca random
import random

#gerar um número aleatório ente 1 e 100 e salvar na variável n_sorteado
drawn_n = random.randrange(1,100)
print(drawn_n)

difficulty = ""

#solicitar o nome do usuário
pl_name = input ("Olá, qual seu nome?\n")
print(f'{pl_name}, ja escolhemos um número para você advinhar de 1,100')
print(f'{pl_name}, escolha de acordo com os números a dificuldade do jogo:')

while not difficulty.isnumeric():
    #define a dificuldade do jogo
    difficulty = input('1 - facíl \n2 - médio \n3 - difícil \n4 - insano\n')
    #caso usuário não digite um número retorna para a escolha de dificuldade
    if not difficulty.isnumeric():
        print(f'{pl_name}, você não digitou um número, por favor digite um número de 1 a 4\n'
              f'para escolher qual a dificuldade do jogo')

# if difficulty == '1':
#     print('vamos lá, você terá 5 chances de acertar o nosso número secreto')
