def ch_difficulty(pl_name):
    # define a dificuldade do jogo
    print(f'{pl_name}, escolha de acordo com os números a dificuldade do jogo:')
    difficulty = input('1 - Fácíl \n2 - Médio \n3 - Difícil \n4 - Insano\n')
    #identifica se a dificuldade dgitada é um número
    if difficulty.isnumeric():
        #identifica se a dificuldade selecionada está entre as disponiveis
        if 1 >= int(difficulty) or int(difficulty) <= 4:
            return difficulty
        else:
            print(f'Desculpe {pl_name}, mas o valor digitado não esta entre as opções de dificuldade')
            ch_difficulty(pl_name)
    else:
        print(f'Desculpe {pl_name}, mas o valor digitado não é um número')
        ch_difficulty(pl_name)



def play (drawn_n, pl_name, opportunity, attempts, points):
    #print(drawn_n)
    ch_number = input(f'{pl_name}, ESCOLHA SEU NÚMERO ENTRE 1 e 50\n')
    attempts.append(ch_number)
    #identifica se o número escolhido pelo usuário é o número sorteado
    if int(ch_number) == drawn_n:
        print(f'PARABÉNS {pl_name}!!!!\n'
              f'Você acertou o número sorteado e fez {points} pontos')
        exit()
    else:
        #caso o usuário erre o número identifica se é maior ou menor que o escolhido
        if int(ch_number) > drawn_n:
            print(f'{pl_name}, seu número é maior que o número sorteado')
            print(f'Suas tentativas foram {attempts}')
            opportunity -= 1
            return opportunity
        else:
            print(f'{pl_name}, seu número é menor que o número sorteado')
            print(f'Suas tentativas foram {attempts}')
            opportunity -= 1
            return opportunity
