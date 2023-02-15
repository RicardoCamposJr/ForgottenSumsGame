#EXIBIÇÃO DO(S) TABULEIRO(S) AOS JOGADORES:
def EXIBIÇÃO(tabuleiro_oculto,linhas_colunas):
    print()
    print('\t\t\t\033[1;32mTABULEIRO DA RODADA\033[m')
    print()
    print('-=' * 35)
    print()
    for l_exibicao in range(linhas_colunas):
        for c_exibicao in range(linhas_colunas):
            print(f'{tabuleiro_oculto[l_exibicao][c_exibicao]:^9}', end='')
        print() 
    print('-=' * 35)

#FUNÇÃO QUE EXIBE NA TELA O JOGADOR QUE OBTEVE PONTUAÇÃO NA RODADA, OU SEJA, O QUE MAIS SE APROXIMOU DA SOMA:
def PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2):
    print(f'\n\033[1;32mPONTO PARA.........\033[m')
    if tupla_aproximacao[0] < tupla_aproximacao[1]:
        print(f'{jogador1}\033[1;32m!!!!!!!!!!\033[m')
        print(f'\n{jogador1} \033[1;32mteve uma aproximação maior da soma da \033[m{tupla_resp_j1[0]}\033[1;32m!\033[m')
        retorno = 'J1'
        
    if tupla_aproximacao[0] == tupla_aproximacao[1]:
        print(f'{jogador1}\033[1;32m e \033[m{jogador2}\033[1;32m!!!!!!!!!!\033[m')
        print('\n\033[1;32mAmbos os jogadores tiveram a mesma aproximação!\033[m')
        retorno = 'AMBOS'

    if tupla_aproximacao[0] > tupla_aproximacao[1]:
        print(f'{jogador2}\033[1;32m!!!!!!!!!!\033[m')
        print(f'\n{jogador2} \033[1;32mteve uma aproximação maior da soma da \033[m{tupla_resp_j2[0]}\033[1;32m!\033[m')
        retorno = 'J2'
        
    return retorno    #RETORNO DO JOGADOR QUE OBTEVE A PONTUAÇÃO NA RODADA.

#PLACAR DA RODADA:
def PONTUACAO_PLACAR(jogador1, jogador2, pontos_jogador1, pontos_jogador2):
    print('-=' * 35)
    print('\t\t\t\t\033[1;32mPONTOS\033[m')
    print('-=' * 35)
    print(f'\n{jogador1} -- {sum(pontos_jogador1)}\n\n{jogador2} -- {sum(pontos_jogador2)}')
    print('-=' * 35)


#EXIBIÇÃO DO HISTÓRICO AOS JOGADORES:
def HISTORICO(lista_historico):
    print('\t\t\t\033[1;32mHISTÓRICO DAS RODADAS\033[m')
    print('-=' * 35)
    for i in lista_historico:
        print(i)
    print('-=' * 35)

#EXIBIÇÃO DO TABULEIRO COM AS SOMAS, AO FINAL DA PARTIDA:
def TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador):
    print()
    print('-=' * 35)
    print('\n\t\t\t\033[1;32mFIM DA PARTIDA!\033[m\n')
    print('-=' * 35)
    cont = 0
    print(f'\n\033[1;32mTABULEIRO DE {jogador} \033[1;32mCOM AS SOMAS:\033[m\n')
    if linhas_colunas == 3:
        print('                             SOMA:')
    if linhas_colunas == 4:
        print('                                      SOMA:')
    if linhas_colunas == 5:
        print('                                               SOMA:')
    for linha in tabuleiro_oculto:
        for elemento in linha:
            print(f'{tabuleiro_oculto[tabuleiro_oculto.index(linha)][linha.index(elemento)]:^9}', end='')
        if cont == 0:
            print(f'  {sum(tabuleiro[0])}')
        elif cont == 1:
            print(f'  {sum(tabuleiro[1])}')
        elif cont == 2:
            print(f'  {sum(tabuleiro[2])}')
        elif cont == 3:
            print(f'  {sum(tabuleiro[3])}')
        elif cont== 4:
            print(f'  {sum(tabuleiro[4])}')
        print()
        cont += 1
    if linhas_colunas == 3:
        print(f'    {tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0]}       {tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1]}       {tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2]}     SOMA')
    if linhas_colunas == 4:
        print(f'    {tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0] + tabuleiro[3][0]}      {tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1] + tabuleiro[3][1]}     {tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2] + tabuleiro[3][2]}      {tabuleiro[0][3] + tabuleiro[1][3] + tabuleiro[2][3] + tabuleiro[3][3]}      SOMA')
    if linhas_colunas == 5:
        print(f'    {tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0] + tabuleiro[3][0] + tabuleiro[4][0]}      {tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1] + tabuleiro[3][1] + tabuleiro[4][1]}     {tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2] + tabuleiro[3][2] + tabuleiro[4][2]}      {tabuleiro[0][3] + tabuleiro[1][3] + tabuleiro[2][3] + tabuleiro[3][3] + tabuleiro[4][3]}     {tabuleiro[0][4] + tabuleiro[1][4] + tabuleiro[2][4] + tabuleiro[3][3] + tabuleiro[4][4]}       SOMA')

#EXIBIÇÃO DO JOGADOR VENCEDOR, OU JOGADORES EM CASO DE EMPATE:
def VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2):
    print('-=' * 35)
    print('\t\t\t\033[1;32mVENCEDOR DA PARTIDA:\033[m')
    print('-=' * 35)
    if sum(pontos_jogador1) > sum(pontos_jogador2):
        print(f'\t\t\t{jogador1}!!!')
    if sum(pontos_jogador1) < sum(pontos_jogador2):
        print(f'\t\t\t{jogador2}!!!')
    if sum(pontos_jogador1) == sum(pontos_jogador2):
        print('\t\t\t\t\033[1;32mEMPATE\033[m')
        print(f'\t\t\t{jogador}!!!')
    print('-=' * 35)
    print()