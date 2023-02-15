import random

#CRIAÇÃO DO TABULEIRO DE ACORDO COM O NÍVEL:
def TABELA(linhas_colunas,intervalo,tabuleiro):
    lista_num_possiveis = []                
    for a in range(1,intervalo):   #GERA UM INTERVALO DE POSSÍVEIS NUMEROS QUE PODEM ESTAR NO TABULEIRO DE ACORDO COM O NÍVEL DO JOGO.
        lista_num_possiveis.append(a) 
    for l in range(linhas_colunas):
        linha = []
        for c in range(linhas_colunas):
            numero_aleatorio = random.choice(lista_num_possiveis)
            linha.append(numero_aleatorio)
            lista_num_possiveis.remove(numero_aleatorio)
        tabuleiro.append(linha)

#CRIAÇÃO DO TABULEIRO OCULTO (MOSTRADO AOS JOGADORES):
def TABELA_OCULTA(linhas_colunas,tabuleiro_oculto):
    for l_oculta in range(linhas_colunas):
        linha_oculta = []
        for c_oculta in range(linhas_colunas):
            linha_oculta.append(' [  X  ] ')
        tabuleiro_oculto.append(linha_oculta)
       

#SOMA TOTAL DAS LINHAS E COLUNAS ESCOLHIDAS:
def SOMA_LINHA(tabuleiro,indice_linha):
    soma_linha = sum(tabuleiro[indice_linha -1 ]) # (-1) PORQUE O INDICE DA LISTA NA MATRIZ É SEMPRE UM NÚMERO ANTERIOR.
    return soma_linha

def SOMA_COLUNA(tabuleiro,indice_coluna):
    soma_coluna = 0
    for b in tabuleiro:
        for c in b:
            if b.index(c) == indice_coluna - 1:
                soma_coluna += c
    return soma_coluna

#APROXIMAÇÃO PARA SABER QUEM PONTUA:
def APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2):
    if tupla_resp_j1[0][0] == 'L':
        indice_linha = int(tupla_resp_j1[0][1])
        soma_escolha_j1 = SOMA_LINHA(tabuleiro,indice_linha)
        aproximacao_jogador1 = (soma_escolha_j1 - tupla_resp_j1[1])**2     #ELEVADO AO QUADRADO PARA NÃO HAVER RESULTADOS NEGATIVOS
    elif tupla_resp_j1[0][0] == 'C':
        indice_coluna = int(tupla_resp_j1[0][1])
        soma_escolha_j1 = SOMA_COLUNA(tabuleiro,indice_coluna)
        aproximacao_jogador1 = (soma_escolha_j1 - tupla_resp_j1[1])**2   

    if escolha_tab == '1':
        if tupla_resp_j2[0][0] == 'L':
            indice_linha = int(tupla_resp_j2[0][1])
            soma_escolha_j2 = SOMA_LINHA(tabuleiro,indice_linha)
            aproximacao_jogador2 = (soma_escolha_j2 - tupla_resp_j2[1])**2     
        elif tupla_resp_j2[0][0] == 'C':
            indice_coluna = int(tupla_resp_j2[0][1])
            soma_escolha_j2 = SOMA_COLUNA(tabuleiro,indice_coluna)
            aproximacao_jogador2 = (soma_escolha_j2 - tupla_resp_j2[1])**2    
    if escolha_tab == '2':
        if tupla_resp_j2[0][0] == 'L':
            indice_linha = int(tupla_resp_j2[0][1])
            soma_escolha_j2 = SOMA_LINHA(tabuleiro_j2,indice_linha)
            aproximacao_jogador2 = (soma_escolha_j2 - tupla_resp_j2[1])**2     
        elif tupla_resp_j2[0][0] == 'C':
            indice_coluna = int(tupla_resp_j2[0][1])
            soma_escolha_j2 = SOMA_COLUNA(tabuleiro_j2,indice_coluna)
            aproximacao_jogador2 = (soma_escolha_j2 - tupla_resp_j2[1])**2    
    
    '''RETORNA SUAS APROXIMAÇÕES COM RELAÇÃO AOS SEUS CHUTES, ASSIM COMO, SUAS SOMAS
    PARA O REAPROVEITAMENTO DESSA INFORMAÇÃO EM OUTRAS FUNÇÕES'''
    return aproximacao_jogador1, aproximacao_jogador2, soma_escolha_j1, soma_escolha_j2 


#FUNÇÃO QUE ARMAZENA AS INFORMAÇÕES DO JOGADOR QUE PONTUOU NA RODADA.
def LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2):
    if tupla_aproximacao[0] < tupla_aproximacao[1]:
        for i in tupla_resp_j1:   #REGISTRA E ARMAZENA AS INFORMAÇÕES O JOAGADOR QUE PONTUOU EM UMA LISTA PARA USO POSTERIOR.
            lista_vencedor.append(i)
    if tupla_aproximacao[0] == tupla_aproximacao[1]:
        for i in tupla_resp_j1:
            lista_vencedor.append(i)
        if escolha_tab == '1':    
            for j in tupla_resp_j2:
                lista_vencedor.append(j)
        if escolha_tab == '2':    
            for j in tupla_resp_j2:
                lista_vencedorj2.append(j)   #LISTA DO JOGADOR VENCEDOR MUDA PARA O CASO DE 2 TABULEIROS.
    if tupla_aproximacao[0] > tupla_aproximacao[1]:
        if escolha_tab == '1':    
            for j in tupla_resp_j2:    
                lista_vencedor.append(j)
        if escolha_tab == '2':    
            for j in tupla_resp_j2:   
                lista_vencedorj2.append(j)    #LISTA DO JOGADOR VENCEDOR MUDA PARA O CASO DE 2 TABULEIROS


#FUNÇÃO PARA DEFINIR A ORDEM DO CHUTE, SE FOI MAIOR, MENOR OU EXATAMENTE A SOMA. COLOCANDO ESSAS INFORMAÇÕES NA LISTA DE HISTÓRICO.
def MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas):
    lista_historico.append(f'\033[1;32mRODADA: {rodadas}')
    if tupla_resp_j1[1] > tupla_aproximacao[2]:  #SE O JOGADOR 1 SE APROXIMOU MAIS DA SOMA E SE O CHUTE DELE FOI MAIOR QUE A SOMA DA LINHA OU COLUNA QUE ELE ESCOLHEU
        ordem_chute_j1 = 'MAIOR'
        lista_historico.append(f'\033[1;32m- {jogador1}\033[1;32m chutou {tupla_resp_j1[1]}\033[1;32m para a {tupla_resp_j1[0]}\033[1;32m e foi {ordem_chute_j1}\033[1;32m que a soma!\033[m')
    
    elif tupla_resp_j1[1] == tupla_aproximacao[2]:  #SE FOI EXATO
        ordem_chute_j1 = 'EXATO'   
        lista_historico.append(f'\033[1;32m- {jogador1}\033[1;32m chutou {tupla_resp_j1[1]}\033[1;32m para a {tupla_resp_j1[0]}\033[1;32m e foi {ordem_chute_j1}\033[1;32m que a soma!\033[m')
    
    elif tupla_resp_j1[1] < tupla_aproximacao[2]:   #SE FOI MENOR
        ordem_chute_j1 = 'MENOR'
        lista_historico.append(f'\033[1;32m- {jogador1}\033[1;32m chutou {tupla_resp_j1[1]}\033[1;32m para a {tupla_resp_j1[0]}\033[1;32m e foi {ordem_chute_j1}\033[1;32m que a soma!\033[m')

    if tupla_resp_j2[1] > tupla_aproximacao[3]:  #SE O JOGADOR 2 SE APROXIMOU MAIS DA SOMA E SE O CHUTE DELE FOI MAIOR QUE A SOMA DA LINHA OU COLUNA QUE ELE ESCOLHEU
        ordem_chute_j2 = 'MAIOR'
        lista_historico.append(f'\033[1;32m- {jogador2}\033[1;32m chutou {tupla_resp_j2[1]}\033[1;32m para a {tupla_resp_j2[0]}\033[1;32m e foi {ordem_chute_j2}\033[1;32m que a soma!\033[m')
    
    elif tupla_resp_j2[1] == tupla_aproximacao[3]:  #SE FOI EXATO
        ordem_chute_j2 = 'EXATO'
        lista_historico.append(f'\033[1;32m- {jogador2}\033[1;32m chutou {tupla_resp_j2[1]}\033[1;32m para a {tupla_resp_j2[0]}\033[1;32m e foi {ordem_chute_j2}\033[1;32m que a soma!\033[m')
    
    elif tupla_resp_j2[1] < tupla_aproximacao[3]:    #SE FOI MENOR
        ordem_chute_j2 = 'MENOR'
        lista_historico.append(f'\033[1;32m- {jogador2}\033[1;32m chutou {tupla_resp_j2[1]}\033[1;32m para a {tupla_resp_j2[0]}\033[1;32m e foi {ordem_chute_j2}\033[1;32m que a soma!\033[m')
    

    return ordem_chute_j1, ordem_chute_j2   #RETORNO DA ORDEM DO CHUTE.

#FUNÇÃO PARA A ADIÇÃO DAS INFORMAÇÕES REFERENTES A ORDEM DO CHUTE NA LISTA DO JOGADOR VENCEDOR DA RODADA.
def ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute):
    if pont == 'J1':
        lista_vencedor.append(tupla_ordem_chute[0])
    if pont == 'J2':
        if escolha_tab == '1':
            lista_vencedor.append(tupla_ordem_chute[1])
        if escolha_tab == '2':
            lista_vencedorj2.append(tupla_ordem_chute[1])
    if pont == 'AMBOS':
        if escolha_tab == '1':
            lista_vencedor.insert(2,tupla_ordem_chute[0])
            lista_vencedor.append(tupla_ordem_chute[1])
        if escolha_tab == '2':
            lista_vencedor.append(tupla_ordem_chute[0])
            lista_vencedorj2.append(tupla_ordem_chute[1])

#FUNÇÃO QUE ALIMENTA AS PONTUAÇÕES DOS JOGADORES NAS RODADAS.
def PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont):
    if pont == 'J1':
        pontos_jogador1.append(1)
    if pont == 'J2':
        pontos_jogador2.append(1)
    if pont == 'AMBOS':
        if cont == 0:   #VARIÁVEL CONTADORA CRIADA NA FUNÇÃO SUBSTITUIÇÃO() PARA O CÓDIGO SABER DE QUEM É A JOGADA.
            pontos_jogador1.append(1)
        if cont != 0:
            pontos_jogador2.append(1)




'''AS LÓGICAS DE SUBSTITUIÇÕES A SEGUIR FORAM APRESENTADAS PELO INTEGRANTE PEDRO HENRIQUE NA SESSÃO TUTORIAL DA DATA
   11/05/2022 EM CONTRIBUIÇÃO AO SOLUCIONAMENTO DO PROBLEMA, CONTUDO, O SISTEMA DE PONTUAÇÃO FOI IMPLEMENTADO POR PARTE DO AUTOR DO PRESENTE CÓDIGO'''

#FUNÇÕES DE SUBSTITUIÇÃO DOS VALORES REAIS NO TABULEIRO MOSTRADO AOS JOGADORES, ADICIONANDO SUAS RESPECTIVAS PONTUAÇÕES:
def SUBSTITUIR_LINHA_MAIOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2):
    linha_acerto = tabuleiro[int(vencedor[0][1]) - 1][:]  #CÓPIA DA LINHA ESCOLHIDA PARA FAZER A MANIPULAÇÃO SEM ERRO DE ÍNDICE.
    for num in lista_numeros_exibidos:  #VERIFICA SE O NÚMERO JÁ FOI MOSTRADO AOS JOGADORES.
        if num in linha_acerto:
            linha_acerto.remove(num)
    if len(linha_acerto):
        maior = max(linha_acerto)
        casas_reveladas.append(1)
    else:
        maior = lista_numeros_exibidos.pop()   #PARA CASOS DE EMPATE, É NECESSÁRIO LOCALIZAR O ÚLTIMO NÚMERO SUBSTITUÍDO NA TABELA, PARA A PREVENÇÃO DE ERROS.
    tabuleiro_oculto[int(vencedor[0][1]) - 1][tabuleiro[int(vencedor[0][1]) - 1].index(maior)] = maior  #IMPLEMENTAÇÃO DO MAIOR NÚMERO NA TABELA APRESENTADA AOS JOGADORES.
    lista_numeros_exibidos.append(maior)
    #A PONTUAÇÃO OCORRE A CADA SUBSTITUIÇÃO NA TABELA APRESENTADA AOS JOGADORES:
    PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)
    
'''A MESMA LÓGICA SEGUE PARA AS DEMAIS FUNÇÕES DE SUBSTITUIÇÃO A SEGUIR:'''

def SUBSTITUIR_COLUNA_MAIOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2):
    coluna_acerto = []
    for lin in tabuleiro:         #LOCALIZAÇÃO DA COLUNA ESCOLHIDA PELO JOGADOR.
        for col in lin:
            if lin.index(col) == int(vencedor[0][1]) - 1:
                coluna_acerto.append(col)

    for t in lista_numeros_exibidos:     #VERIFICA SE O NÚMERO JÁ FOI MOSTRADO AOS JOGADORES.
        if t in coluna_acerto:
            coluna_acerto.remove(t)
    
    if len(coluna_acerto):
        maior = max(coluna_acerto)
        casas_reveladas.append(1)
    else:
        maior = lista_numeros_exibidos.pop()

    coluna_acerto = []    #RESET DA COLUNA ESCOLHIDA PARA O ÍNDICE DO ELEMENTO NA LISTA DE NÚMEROS REAIS PERMANECER CORRETO.
    for lin in tabuleiro:         #PARA LOCALIZAR A COLUNA QUE O JOGADOR ESCOLHEU.
        for col in lin:
            if lin.index(col) == int(vencedor[0][1]) - 1:
                coluna_acerto.append(col)

    tabuleiro_oculto[coluna_acerto.index(maior)][int(vencedor[0][1]) - 1] = maior   #SUBSTITUIÇÃO DO MAIOR NÚMERO NO TABULEIRO MOSTRADO AOS JOGADORES
    lista_numeros_exibidos.append(maior)
    #A PONTUAÇÃO OCORRE A CADA SUBSTITUIÇÃO NA TABELA APRESENTADA AOS JOGADORES:
    PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)


def SUBSTITUIR_LINHA_MENOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2):
    linha_acerto = tabuleiro[int(vencedor[0][1]) - 1][:]  
    for num in lista_numeros_exibidos:
        if num in linha_acerto:
            linha_acerto.remove(num)
    if len(linha_acerto):
        menor = min(linha_acerto)
        casas_reveladas.append(1)
    else:
        menor = lista_numeros_exibidos.pop()     
    tabuleiro_oculto[int(vencedor[0][1]) - 1][tabuleiro[int(vencedor[0][1]) - 1].index(menor)] = menor  
    lista_numeros_exibidos.append(menor)
    #A PONTUAÇÃO OCORRE A CADA SUBSTITUIÇÃO NA TABELA APRESENTADA AOS JOGADORES:
    PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)


def SUBSTITUIR_COLUNA_MENOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2):
    coluna_acerto = []
    for lin in tabuleiro:         
        for col in lin:
            if lin.index(col) == int(vencedor[0][1]) - 1:
                coluna_acerto.append(col)

    for t in lista_numeros_exibidos:     
        if t in coluna_acerto:
            coluna_acerto.remove(t)
    
    if len(coluna_acerto):
        menor = min(coluna_acerto)
        casas_reveladas.append(1)
    else:
        menor = lista_numeros_exibidos.pop()

    coluna_acerto = []    
    for lin in tabuleiro:         
        for col in lin:
            if lin.index(col) == int(vencedor[0][1]) - 1:
                coluna_acerto.append(col)

    tabuleiro_oculto[coluna_acerto.index(menor)][int(vencedor[0][1]) - 1] = menor   
    lista_numeros_exibidos.append(menor)
    #A PONTUAÇÃO OCORRE A CADA SUBSTITUIÇÃO NA TABELA APRESENTADA AOS JOGADORES:
    PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)


def SUBSTITUIR_LINHA(casas_reveladas,lista_exibidos_1volta,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2):
    linha_acerto = tabuleiro[int(vencedor[0][1]) - 1][:]  
    for num in linha_acerto:
        if num not in lista_numeros_exibidos:
            tabuleiro_oculto[int(vencedor[0][1]) - 1][linha_acerto.index(num)] = num
            lista_numeros_exibidos.append(num)
            #A PONTUAÇÃO OCORRE A CADA SUBSTITUIÇÃO NA TABELA APRESENTADA AOS JOGADORES:
            PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)
            '''NA LÓGICA ABAIXO, PARA CASOS DE EMPATE, É NECESSÁRIO CONHECER QUAIS NÚMEROS FORAM SUBSTITUÍDOS NO TABULEIRO
            OCULTO NA VEZ DO JOGADOR 1 PARA ADICIONAR A MESMA QUANTIDADE DE PONTOS AO JOGADOR 2, JÁ QUE O EMPATE OCORREU.'''
            if cont == 0:
                lista_exibidos_1volta.append(num)
                casas_reveladas.append(1)
            if cont != 0:
                casas_reveladas.append(1)
        elif num in lista_numeros_exibidos and cont != 0:
            if num in lista_exibidos_1volta:
                PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)
        




def SUBSTITUIR_COLUNA(casas_reveladas,lista_exibidos_1volta,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2):
    coluna_acerto = []
    for lin in tabuleiro:         
        for col in lin:
            if lin.index(col) == int(vencedor[0][1]) - 1:
                coluna_acerto.append(col)
    for num in coluna_acerto:
        if num not in lista_numeros_exibidos:
            tabuleiro_oculto[coluna_acerto.index(num)][int(vencedor[0][1]) - 1] = num
            lista_numeros_exibidos.append(num)
            #A PONTUAÇÃO OCORRE A CADA SUBSTITUIÇÃO NA TABELA APRESENTADA AOS JOGADORES:
            PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)
            '''NA LÓGICA ABAIXO, PARA CASOS DE EMPATE, É NECESSÁRIO CONHECER QUAIS NÚMEROS FORAM SUBSTITUÍDOS NO TABULEIRO
            OCULTO NA VEZ DO JOGADOR 1 PARA ADICIONAR A MESMA QUANTIDADE DE PONTOS AO JOGADOR 2, JÁ QUE O EMPATE OCORREU.'''
            if cont == 0:
                lista_exibidos_1volta.append(num)
                casas_reveladas.append(1)
            if cont != 0:
                casas_reveladas.append(1)
        elif num in lista_numeros_exibidos and cont != 0:
            if num in lista_exibidos_1volta:
                PONTUAÇÃO_JOGADORES(pont,pontos_jogador1,pontos_jogador2,cont)


#FUNÇÃO COM ESTRUTURA PARA AS SUBSTITUIÇÕES NO TABULEIRO MOSTRADO AOS JOGADORES.
def SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2):
    '''NA LÓGICA A SEGUIR, OS ELEMENTOS DA LISTA DO(S) VENCEDOR(ES) FORAM TRANSFORMADOS EM TUPLAS
       SEPARADAS PARA O APROVEITAMENTO DA LÓGICA DE SUBSTITUIÇÃO NOS CASOS DE EMPATE TAMBÉM.'''
    if len(lista_vencedor) > 3:
        tupla1 = tuple(lista_vencedor[:3])
        tupla2 = tuple(lista_vencedor[3:])
        lista_vencedor = []
        lista_vencedor.append(tupla1)
        lista_vencedor.append(tupla2)
        '''AO FINAL DA LÓGICA ACIMA, O RESULTADO É UMA LISTA COM DUAS TUPLAS CONTENDO AS 
        INFORMAÇÕES DOS JOGADORES QUE OBTIVERAM A PONTUAÇÃO.'''
    else:
        tupla3 = tuple(lista_vencedor)
        lista_vencedor = []
        lista_vencedor.append(tupla3)
        '''AO FINAL DA LÓGICA ACIMA, O RESULTADO É UMA LISTA COM UMA TUPLA CONTENDO AS INFORMAÇÕES DO JOGADOR VENCEDOR.'''
    

    #SUBSTITUIÇÃO DOS VALORES REAIS NO TABULEIRO OCULTO (TABULEIRO MOSTRADO AOS JOGADORES):
    lista_exibidos_1volta = []   #RESET DA LISTA PARA CASO DE PONTOS DUPLICADOS.
    cont = 0 #VARIÁVEL PARA CONTABILIZAR O LOOPING DO LAÇO FOR A SEGUIR, PARA CONT = 0, JOGADA DO JOGADOR 1. PARA CONT != 0 JOGADA DO JOGADOR 2.
    if len(lista_vencedor[0]) > 2:
        for vencedor in lista_vencedor:    
            if vencedor[2] == 'MAIOR':
                if vencedor[0][0] == 'L':
                    SUBSTITUIR_LINHA_MAIOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2)
                if vencedor[0][0] == 'C':
                    SUBSTITUIR_COLUNA_MAIOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2)
            if vencedor[2] == 'MENOR':
                if vencedor[0][0] == 'L':
                    SUBSTITUIR_LINHA_MENOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2)
                if vencedor[0][0] == 'C':
                    SUBSTITUIR_COLUNA_MENOR(casas_reveladas,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2)
            if vencedor[2] == 'EXATO':
                if vencedor[0][0] == 'L':
                    SUBSTITUIR_LINHA(casas_reveladas,lista_exibidos_1volta,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2)
                if vencedor[0][0] == 'C':
                    SUBSTITUIR_COLUNA(casas_reveladas,lista_exibidos_1volta,cont,pont,tabuleiro, tabuleiro_oculto, vencedor, lista_numeros_exibidos,pontos_jogador1,pontos_jogador2)
            cont += 1
    if escolha_tab == '2':
        if pont == 'J2' or pont == 'AMBOS':
            if lista_vencedorj2[2] == 'MAIOR':
                if lista_vencedorj2[0][0] == 'L':
                    SUBSTITUIR_LINHA_MAIOR(casas_reveladas_j2,cont,pont,tabuleiro_j2, tabuleiro_oculto_j2, lista_vencedorj2, lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                if lista_vencedorj2[0][0] == 'C':
                    SUBSTITUIR_COLUNA_MAIOR(casas_reveladas_j2,cont,pont,tabuleiro_j2, tabuleiro_oculto_j2, lista_vencedorj2, lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
            if lista_vencedorj2[2] == 'MENOR':
                if lista_vencedorj2[0][0] == 'L':
                    SUBSTITUIR_LINHA_MENOR(casas_reveladas_j2,cont,pont,tabuleiro_j2, tabuleiro_oculto_j2, lista_vencedorj2, lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                if lista_vencedorj2[0][0] == 'C':
                    SUBSTITUIR_COLUNA_MENOR(casas_reveladas_j2,cont,pont,tabuleiro_j2, tabuleiro_oculto_j2, lista_vencedorj2, lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
            if lista_vencedorj2[2] == 'EXATO':
                if lista_vencedorj2[0][0] == 'L':
                    SUBSTITUIR_LINHA(casas_reveladas_j2,lista_exibidos_1volta,cont,pont,tabuleiro_j2, tabuleiro_oculto_j2, lista_vencedorj2, lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                if lista_vencedorj2[0][0] == 'C':
                    SUBSTITUIR_COLUNA(casas_reveladas_j2,lista_exibidos_1volta,cont,pont,tabuleiro_j2, tabuleiro_oculto_j2, lista_vencedorj2, lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
