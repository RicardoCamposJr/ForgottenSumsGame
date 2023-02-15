def VALIDAR_JOGADOR():   #FUNÇÃO QUE VALIDA A ENTRADA DO NOME DO JOGADOR. 
    jogador = input('\n\033[1;32mNome do jogador: \033[m')
    while not jogador.strip():
        print('\n\033[1;31;41mPor favor, informe como o jogador quer ser referenciado no game.\033[m')
        jogador = input('\n\033[1;32mNome do jogador: \033[m')
    return jogador


def VALIDAR_TAB():   #FUNÇÃO QUE VALIDA A ESCOLHA DO MODO DE JOGO (1 OU 2 TABULEIROS).
    escolha_tabuleiros = input('\n\033[1;32m[1] - 1 Tabuleiro\n[2] - 2 Tabuleiros\n\nOpção: \033[m')
    while escolha_tabuleiros != '1' and escolha_tabuleiros != '2':
        print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
        escolha_tabuleiros = input('\n\033[1;32m[1] - 1 Tabuleiro\n[2] - 2 Tabuleiros\n\nOpção: \033[m')
    return escolha_tabuleiros

def VALIDAR_NIVEL():   #FUNÇÃO QUE VALIDA A ESCOLHA DO NÍVEL DO JOGO.
    nivel = input('\n\033[1;32m[1] - NÍVEL FÁCIL   -> Tabuleiro 3x3\n[2] - NÍVEL MÉDIO   -> Tabuleiro 4X4\n[3] - NÍVEL DIFÍCIL -> Tabuleiro 5x5\n\nOpção: \033[m')
    while nivel != '1' and nivel != '2' and nivel != '3':
        print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
        nivel = input('\n\033[1;32m[1] - NÍVEL FÁCIL   -> Tabuleiro 3x3\n[2] - NÍVEL MÉDIO   -> Tabuleiro 4X4\n[3] - NÍVEL DIFÍCIL -> Tabuleiro 5x5\n\nOpção: \033[m')
    return nivel

def VALIDAR_TERMINO():   #FUNÇÃO QUE VALIDA A ESCOLHA DE MODO DE TÉRMINO DA PARTIDA.
    termino = input('\n\033[1;32m[1] - Número de partidas\n[2] - Tabuleiro(s) reveledo(s)\n\nOpção: \033[m')
    while termino != '1' and termino != '2':
        print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
        termino = input('\n\033[1;32m[1] - Número de partidas\n[2] - Tabuleiro(s) reveledo(s)\n\nOpção: \033[m')
    print('-=' * 35)
    return termino

def VALIDAR_RODADAS():   #FUNÇÃO QUE VALIDA O NÚMERO DE RODADAS PARA SOMENTE NÚMEROS ÍMPARES.
    num_rodadas = input('\n\033[1;32mDigite o numero de rodadas (somente ímpares, abaixo de 100): \033[m')
    while num_rodadas.isdigit() == False or int(num_rodadas)%2 == 0 or int(num_rodadas) > 100:
        print('\n\033[1;31;41mDigite um valor ímpar válido.\033[m')
        num_rodadas = input('\n\033[1;32mDigite o numero de rodadas (somente ímpar, abaixo de 100): \033[m')
    print('-=' * 35)
    return num_rodadas

#FUNÇÃO QUE VALIDA A ESCOLHA DA LINHA OU COLUNA ONDE O JOGADOR VAI REALIZAR O SEU CHUTE DE ACORDO COM O NÍVEL DO JOGO:
def VALIDAR_ESCOLHA(linhas_colunas,jogador):   
    resp_jogador = input(f'\n\033[1;32mInforme qual linha ou coluna\033[m {jogador} \033[1;32mquer chutar: \nExemplo: LINHA 1 = L1 | COLUNA 1 = C1 | ...\n\nOpção: \033[m').upper()
    if linhas_colunas == 3:
        while resp_jogador != 'L1' and resp_jogador != 'L2' and resp_jogador != 'L3' and resp_jogador != 'C1' and resp_jogador != 'C2' and resp_jogador != 'C3':
            print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
            resp_jogador = input(f'\n\033[1;32mInforme qual linha ou coluna\033[m {jogador} \033[1;32mquer chutar: \nExemplo: LINHA 1 = L1 | COLUNA 1 = C1 | ...\n\nOpção: \033[m').upper()
        return resp_jogador
    if linhas_colunas == 4:
        while resp_jogador != 'L1' and resp_jogador != 'L2' and resp_jogador != 'L3' and resp_jogador != 'L4' and resp_jogador != 'C1' and resp_jogador != 'C2' and resp_jogador != 'C3'and resp_jogador != 'C4':
            print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
            resp_jogador = input(f'\n\033[1;32mInforme qual linha ou coluna\033[m {jogador} \033[1;32mquer chutar: \nExemplo: LINHA 1 = L1 | COLUNA 1 = C1 | ...\n\nOpção: \033[m').upper()
        return resp_jogador
    if linhas_colunas == 5:
        while resp_jogador != 'L1' and resp_jogador != 'L2' and resp_jogador != 'L3' and resp_jogador != 'L4' and resp_jogador != 'L5'  and resp_jogador != 'C1' and resp_jogador != 'C2' and resp_jogador != 'C3'and resp_jogador != 'C4' and resp_jogador != 'C5':
            print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
            resp_jogador = input(f'\n\033[1;32mInforme qual linha ou coluna\033[m {jogador} \033[1;32mquer chutar: \nExemplo: LINHA 1 = L1 | COLUNA 1 = C1 | ...\n\nOpção: \033[m').upper()
        return resp_jogador

#FUNÇÃO QUE VERIFICA SE É POSSÍVEL A JOGADA NA LINHA OU COLUNA ESCOLHIDA (SE AQUELA LINHA OU COLUNA CONTÉM CASAS OCULTAS):
def LIBERAÇÃO_LINHAxCOLUNA(linhas_colunas,jogador,resp_jogador,tabuleiro_oculto):
    confirmação = 'NAO'   #VARIÁVEL PARA A CONDIÇÃO DO LAÇO WHILE A SEGUIR SE INICIAR.
    while confirmação == 'NAO':
        if resp_jogador[0] == 'L':
            #NA LINHA ABAIXO, VERIFICA SE HÁ CASAS OCULTAS NA LINHA ESCOLHIDA NO TABULEIRO MOSTRADO AO JOGADOR.
            if ' [  X  ] ' not in tabuleiro_oculto[int(resp_jogador[1]) - 1]:   
                print('\n\033[1;31;41mNão é possivel jogar nessa linha pois está completa.\033[m')
                print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
                resp_jogador = VALIDAR_ESCOLHA(linhas_colunas,jogador)   #VOLTA PARA A VALIDAÇÃO DA NOVA ENTRADA DO JOGADOR.
            else:
                confirmação = 'SIM'   #MODIFICAÇÃO DA VARIÁVEL DE CONDIÇÃO CASO EXISTA POSSIBILIDADE DE CHUTAR NAQUELA LINHA.
        if resp_jogador[0] == 'C':
            coluna_escolhida = []  
            for linha in tabuleiro_oculto:
                cont = 0
                for elemento in linha:
                    if cont == int(resp_jogador[1]) - 1:
                        coluna_escolhida.append(elemento)
                    cont += 1

            #NA LINHA ABAIXO, VERIFICA SE HÁ CASAS OCULTAS NA COLUNA ESCOLHIDA NO TABULEIRO MOSTRADO AO JOGADOR.
            if ' [  X  ] ' not in coluna_escolhida:
                print('\n\033[1;31;41mNão é possivel jogar nessa coluna pois está completa.\033[m')
                print('\n\033[1;31;41mEscolha uma opção válida.\033[m')
                resp_jogador = VALIDAR_ESCOLHA(linhas_colunas,jogador)
            else:
                confirmação = 'SIM'   #MODIFICAÇÃO DA VARIÁVEL DE CONDIÇÃO CASO EXISTA POSSIBILIDADE DE CHUTAR NAQUELA LINHA.
    return resp_jogador

def VALIDAR_CHUTE(resp_jogador,jogador):   #FUNÇÃO QUE VALIDA O CHUTE DO JOGADOR.
    chute_jogador = input(f'\n\033[1;32mSeu chute para a {resp_jogador}, {jogador}: ')
    while chute_jogador.isdigit() == False or int(chute_jogador)<0:
        print('\n\033[1;31;41mDigite um valor válido.\033[m')
        chute_jogador = input(f'\n\033[1;32mSeu chute para a\033[m {resp_jogador}, {jogador}: ')
    return chute_jogador