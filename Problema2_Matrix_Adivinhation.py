'''*******************************************************************************
Autor: Ricardo Campos de Oliveira Júnior
Componente Curricular: MI - Algoritmos
Concluido em: 22/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''  

from PROCESSAMENTO.processos import *
from ESCOLHAS.menu import *
from ESCOLHAS.chutes import *
from EXIBIÇÃO.exibições import *
from VALIDAÇÃO.validações import * 

tabuleiro = []  #LISTA PARA A FORMAÇÃO DO TABULEIRO DOS DOIS JOGADORES (OU DO JOGADOR 1 NO MODO COM 2 TABULEIROS).
tabuleiro_j2 = []   #TABULEIRO DO JOGADOR 2 NO MODO COM 2 TABULEIROS.
tabuleiro_oculto = []  #TABULEIRO COM OS VALORES OCULTOS MOSTRADO AOS JOGADORES.
tabuleiro_oculto_j2 = []   #TABULEIRO COM OS VALORES OCULTOS DO JOGADOR 2, NO MODO COM 2 TABULEIROS.
rodadas = 1   
pontos_jogador1 = [] 
pontos_jogador2 = []
lista_numeros_exibidos = []   #LISTA PARA O CONHECIMENTO DE QUAIS NÚMEROS JÁ FORAM REVELADOS NO TABULEIRO.
lista_numeros_exibidos_j2 = []   #LISTA PARA O CONHECIMENTO DE QUAIS NÚMEROS JÁ FORAM REVELADOS NO TABULEIRODO JOGADOR 2, NO MODO DE 2 TABULEIROS.
lista_historico = []   #LISTA PARA ARMAZENAMENTO DAS JOGADAS NO HISTÓRICO EXIBIDO A CADA PARTIDA.
lista_vencedor = []   #LISTA PARA O ARMAZENAMENTO DAS RESPOSTAS DO JOGADOR QUE PONTUOU NA RODADA.
lista_vencedorj2 = []   #LISTA PARA O ARMAZENAMENTO DAS RESPOSTAS DO JOGADOR 2 QUE PONTUOU NA RODADA, PARA O MODO COM 2 TABULEIROS.
lista_exibidos_1volta = []   #LISTA PARA O ARMAZENAMENTO DOS NUMEROS EXIBIDOS PELO JOGADOR 1 EM CASO DE EMPATE.
casas_reveladas = []   #NÚMERO DE CASAS REVELADAS NO MODO COM 1 TABULEIRO.
casas_reveladas_j2 = []   #NÚMERO DE CASAS REVELADAS NO MODO COM 2 TABULEIROS.

#INÍCIO DO JOGO 
APRESENTAÇÃO()
print('\n\033[1;34m1° JOGADOR\033[m')
jogador1 = f'\033[1;34m{VALIDAR_JOGADOR()}\033[m'
print('\n\033[1;31m2° JOGADOR\033[m')
jogador2 = f'\033[1;31m{VALIDAR_JOGADOR()}\033[m'
jogador = f'{jogador1}\033[1;32m e {jogador2}\033[m'

escolha_tab = ESCOLHA_TABULEIROS()   #ESCOLHA DO NÚMERO DE TABULEIROS.
if escolha_tab == '1':
    nivel = ESCOLHA_NIVEL()   #ESCOLHA DO NÍVEL.
    if nivel == '1':
        linhas_colunas = 3   #A AREA DO TABULEIRO.
        intervalo = 31   #O INTERVALO DE POSSÍVEIS NUMEROS PRESENTES NO TABULEIRO.
        termino = ESCOLHA_TERMINO()   #ESCOLHA DO MODO DE TÉRMINO DA PARTIDA.
        if termino == '1':
            num_rodadas = int(VALIDAR_RODADAS())
            TABELA(linhas_colunas,intervalo,tabuleiro)     #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)    #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES.
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)        #EXIBIÇÃO DO TABULEIRO AOS JOGADORES.
            while num_rodadas != 0 and sum(casas_reveladas) != 9:
                '''NO CASO DE ENCERRAMENTO POR NÚMERO DE RODADAS, A PARTIDA TEM FIM QUANDO O NÚMERO DE RODADAS
                ALCANÇA O VALOR INSERIDO PELO USUÁRIO, OU, MESMO QUE AINDA NÃO TENHA-SE PASSADO A QUANTIDADE
                DE RODADAS, O TABULEIRO ESTEJA TOTALMETE PREENCHIDO, POIS NÃO RESTARIAM POSSÍVEIS JOGADAS.'''
                
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto) 
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)   #RETORNA E PRINTA NA TELA QUEM PONTUOU NA RODADA.
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)   #ALIMENTA A LISTA DO JOGADOR VENCEDOR.
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute = MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)   #ADICIONA ORDEM DO CHUTE NA LISTA DO VENCEDOR DA RODADA.
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                rodadas += 1 
                lista_vencedor = [] #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                num_rodadas -= 1
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador)   
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
                
            '''A PARTIR DESTE PONTO, AS FUNÇÕES UTILIZADAS NO CASO ACIMA SÃO AS MESMAS, VARIANDO SOMENTE 
            A SEQUÊNCIA DE CHAMADAS, PARÂMENTROS E CASOS DE ENCERRAMENTO.'''

        elif termino == '2': 
            TABELA(linhas_colunas,intervalo,tabuleiro)     
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)   
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO TODAS A CASAS JÁ FORAM REVELADAS'''       
            while sum(casas_reveladas) != 9:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto)  
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)    
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute = MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                    OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)    #PONTUAÇÃO DOS JOGADORES NO PLACAR  
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador)
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.



    elif nivel == '2':
        linhas_colunas = 4  #A AREA DO TABULEIRO.
        intervalo = 61      #O INTERVALO DE POSSÍVEIS NUMEROS PRESENTES NO TABULEIRO.                
        termino = ESCOLHA_TERMINO()   
        if termino == '1':          
            num_rodadas = int(VALIDAR_RODADAS())
            TABELA(linhas_colunas,intervalo,tabuleiro)       #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)   #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES.
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)        #EXIBIÇÃO DO TABULEIRO AOS JOGADORES.
            while num_rodadas != 0 and sum(casas_reveladas) != 16:
                '''NO CASO DE ENCERRAMENTO POR NÚMERO DE RODADAS, A PARTIDA TEM FIM QUANDO O NÚMERO DE RODADAS
                ALCANÇA O VALOR INSERIDO PELO USUÁRIO, OU, MESMO QUE AINDA NÃO TENHA-SE PASSADO A QUANTIDADE
                DE RODADAS, O TABULEIRO ESTEJA TOTALMETE PREENCHIDO, POIS NÃO RESTARIAM POSSÍVEIS JOGADAS.'''
                
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto) 
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)   
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute = MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)    #PONTUAÇÃO DOS JOGADORES NO PLACAR  
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                num_rodadas -= 1
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador)
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.

        
        elif termino == '2':   
            TABELA(linhas_colunas,intervalo,tabuleiro)        #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)    #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES.
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)         #EXIBIÇÃO DO TABULEIRO AOS JOGADORES.
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO TODAS A CASAS JÁ FORAM REVELADAS'''
            while sum(casas_reveladas) != 16:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto)  
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)    
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute = MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                    OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR  
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador)
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.



    elif nivel == '3':
        linhas_colunas = 5    #A AREA DO TABULEIRO.
        intervalo = 101       #O INTERVALO DE POSSÍVEIS NUMEROS PRESENTES NO TABULEIRO.
        termino = ESCOLHA_TERMINO()
        if termino == '1':
            num_rodadas = int(VALIDAR_RODADAS())
            TABELA(linhas_colunas,intervalo,tabuleiro)          #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)      #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES.
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)           #EXIBIÇÃO DO TABULEIRO AOS JOGADORES.
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO A SOMA DA PONTUAÇÃO
            DOS DOIS JOGADORES FOR IGUAL A ÁREA DO(S) TABULEIRO(S), O QUE SIGNIFICA QUE TODAS A CASAS JÁ FORAM REVELADAS'''
            while num_rodadas != 0 and sum(casas_reveladas) != 25:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto)  
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)    
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute = MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR 
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                num_rodadas -= 1
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador)
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
        


        elif termino == '2':  
            TABELA(linhas_colunas,intervalo,tabuleiro)         #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)     #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES.
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)          #EXIBIÇÃO DO TABULEIRO AOS JOGADORES.
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO TODAS A CASAS JÁ FORAM REVELADAS'''
            while sum(casas_reveladas) != 25:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto) 
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)   
                pont =PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute = MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                    OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR   
                HISTORICO(lista_historico)    #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador)
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.

#MODO DE JOGO COM 2 TABULEIROS:
'''A PARTIR DESTE PONTO, ALGUMAS FUNÇÕES POSSUEM DUAS CHAMADAS PELO FATO DO MODO DE JOGO CONTÊR DOIS TABULEIROS,
LOGO, É PRECISO CHAMÁ-LAS MAIS DE UMA VEZ, PORÉM, COM PARÂMETROS DIFERENTES PARA QUE A FUNÇÃO SE ADEQUE PARA AMBOS OS TABULEIROS.'''
if escolha_tab == '2':
    nivel = ESCOLHA_NIVEL()
    if nivel == '1':
        linhas_colunas = 3    #A AREA DO TABULEIRO.          
        intervalo = 31        #O INTERVALO DE POSSÍVEIS NUMEROS PRESENTES NO TABULEIRO.                
        termino = ESCOLHA_TERMINO()
        if termino == '1':  
            num_rodadas = int(VALIDAR_RODADAS())
            TABELA(linhas_colunas,intervalo,tabuleiro)        #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS DO JOGADOR 1.
            TABELA(linhas_colunas,intervalo,tabuleiro_j2)     #FORMAÇÃO DO TABULEIRO COM OS VALORES REAIS DO JOGADOR 2.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)        #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 1.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto_j2)     #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 2.
            print(f'TABULEIRO DE {jogador1}')
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)             #EXIBIÇÃO DO TABULEIRO DO JOGADOR 1 AOS JOGADORES.
            print(f'\nTABULEIRO DE {jogador2}')  
            EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)          #EXIBIÇÃO DO TABULEIRO DO JOGADOR 2 AOS JOGADORES.
            while num_rodadas != 0 and sum(casas_reveladas) != 9 and sum(casas_reveladas_j2) != 9:
                '''PARA O TÉRMINO DA PARTIDA POR NÚMERO DE RODADAS NO MODO COM 2 TABULEIROS, A PARTIDA SE ENCERRA QUANDO É ATINGIDO O VALOR
                PARA O NÚMERO DE RODADAS INSERIDO PELOS USUÁRIOS, MAS TAMBÉM, QUANDO O TABULEIRO DE ALGUM DOS DOIS JOGADORES É TOTALMENTE 
                COMPLETO, OU SEJA,QUANDO O NÚMERO DE CASAS REVELADAS DE ALGUM DOS JOGADORES FOR IGUAL A ÁREA DO TABULEIRO.'''
                
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto)  
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto_j2)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)   
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute =  MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR  
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                print(f'TABULEIRO DE {jogador1}')
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                print(f'\nTABULEIRO DE {jogador2}') 
                EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                lista_vencedorj2 = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                num_rodadas -= 1
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador1)    #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 1.
            TABULEIRO_RESPOSTA(tabuleiro_j2,tabuleiro_oculto_j2,linhas_colunas,jogador2)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 2.
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
        
        elif termino == '2':
            TABELA(linhas_colunas,intervalo,tabuleiro)      #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS DO JOGADOR 1.
            TABELA(linhas_colunas,intervalo,tabuleiro_j2)   #FORMAÇÃO DO TABULEIRO COM OS VALORES REAIS DO JOGADOR 2. 
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)      #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 1.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto_j2)   #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 2.
            print(f'TABULEIRO DE {jogador1}')
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)           #EXIBIÇÃO DO TABULEIRO DO JOGADOR 1 AOS JOGADORES.
            print(f'\nTABULEIRO DE {jogador2}') 
            EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)        #EXIBIÇÃO DO TABULEIRO DO JOGADOR 2 AOS JOGADORES.
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO TODAS A CASAS 
            DO TABULEIRO DE ALGUM DOS JOGADORES JÁ FORAM REVELADAS'''
            while sum(casas_reveladas) != 9 and sum(casas_reveladas_j2) != 9:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto) 
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto_j2)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)  
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)   
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute =  MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                    OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)    #PONTUAÇÃO DOS JOGADORES NO PLACAR 
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                print(f'TABULEIRO DE {jogador1}')
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                print(f'\nTABULEIRO DE {jogador2}') 
                EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                lista_vencedorj2 = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador1)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 1.
            TABULEIRO_RESPOSTA(tabuleiro_j2,tabuleiro_oculto_j2,linhas_colunas,jogador2)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 2.
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
    
    elif nivel == '2':
        linhas_colunas = 4   #A AREA DO TABULEIRO.          
        intervalo = 61       #O INTERVALO DE POSSÍVEIS NUMEROS PRESENTES NO TABULEIRO.          
        termino = ESCOLHA_TERMINO()
        if termino == '1':
            num_rodadas = int(VALIDAR_RODADAS())
            TABELA(linhas_colunas,intervalo,tabuleiro)          #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS DO JOGADOR 1.
            TABELA(linhas_colunas,intervalo,tabuleiro_j2)       #FORMAÇÃO DO TABULEIRO COM OS VALORES REAIS DO JOGADOR 2.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)        #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 1.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto_j2)     #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 2.
            print(f'TABULEIRO DE {jogador1}')
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)             #EXIBIÇÃO DO TABULEIRO DO JOGADOR 1 AOS JOGADORES.
            print(f'\nTABULEIRO DE {jogador2}') 
            EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)          #EXIBIÇÃO DO TABULEIRO DO JOGADOR 2 AOS JOGADORES.
            while num_rodadas != 0 and sum(casas_reveladas) != 16 and sum(casas_reveladas_j2) != 16:
                '''PARA O TÉRMINO DA PARTIDA POR NÚMERO DE RODADAS NO MODO COM 2 TABULEIROS, A PARTIDA SE ENCERRA QUANDO É ATINGIDO O VALOR
                PARA O NÚMERO DE RODADAS INSERIDO PELOS USUÁRIOS, MAS TAMBÉM, QUANDO O TABULEIRO DE ALGUM DOS DOIS JOGADORES É TOTALMENTE 
                COMPLETO, OU SEJA,QUANDO O NÚMERO DE CASAS REVELADAS DE ALGUM DOS JOGADORES FOR IGUAL A ÁREA DO TABULEIRO.'''
                
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto)  
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto_j2)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)  
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute =  MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR   
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                print(f'TABULEIRO DE {jogador1}')
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                print(f'\nTABULEIRO DE {jogador2}') 
                EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                lista_vencedorj2 = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                num_rodadas -= 1
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador1)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 1.
            TABULEIRO_RESPOSTA(tabuleiro_j2,tabuleiro_oculto_j2,linhas_colunas,jogador2)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 2.
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
        
        elif termino == '2':
            TABELA(linhas_colunas,intervalo,tabuleiro)          #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS DO JOGADOR 1.
            TABELA(linhas_colunas,intervalo,tabuleiro_j2)       #FORMAÇÃO DO TABULEIRO COM OS VALORES REAIS DO JOGADOR 2.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)         #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 1.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto_j2)      #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 2.
            print(f'TABULEIRO DE {jogador1}')
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)              #EXIBIÇÃO DO TABULEIRO DO JOGADOR 1 AOS JOGADORES.
            print(f'\nTABULEIRO DE {jogador2}') 
            EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)           #EXIBIÇÃO DO TABULEIRO DO JOGADOR 2 AOS JOGADORES.
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO TODAS A CASAS 
            DO TABULEIRO DE ALGUM DOS JOGADORES JÁ FORAM REVELADAS'''
            while sum(casas_reveladas) != 16 and sum(casas_reveladas_j2) != 16:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto) 
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto_j2)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)   
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)    
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute =  MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                    OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR    
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                print(f'TABULEIRO DE {jogador1}')
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                print(f'\nTABULEIRO DE {jogador2}') 
                EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                lista_vencedorj2 = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador1)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 1.
            TABULEIRO_RESPOSTA(tabuleiro_j2,tabuleiro_oculto_j2,linhas_colunas,jogador2)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 2.
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
    
    elif nivel == '3':
        linhas_colunas = 5   #A AREA DO TABULEIRO. 
        intervalo = 101      #O INTERVALO DE POSSÍVEIS NUMEROS PRESENTES NO TABULEIRO.   
        termino = ESCOLHA_TERMINO()
        if termino == '1':
            num_rodadas = int(VALIDAR_RODADAS())
            TABELA(linhas_colunas,intervalo,tabuleiro)          #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS DO JOGADOR 1.
            TABELA(linhas_colunas,intervalo,tabuleiro_j2)       #FORMAÇÃO DO TABULEIRO COM OS VALORES REAIS DO JOGADOR 2.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)         #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 1.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto_j2)      #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 2.
            print(f'TABULEIRO DE {jogador1}')
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)              #EXIBIÇÃO DO TABULEIRO DO JOGADOR 1 AOS JOGADORES.
            print(f'\nTABULEIRO DE {jogador2}') 
            EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)           #EXIBIÇÃO DO TABULEIRO DO JOGADOR 2 AOS JOGADORES.
            while num_rodadas != 0 and sum(casas_reveladas) != 25 and sum(casas_reveladas_j2) != 25:
                '''PARA O TÉRMINO DA PARTIDA POR NÚMERO DE RODADAS NO MODO COM 2 TABULEIROS, A PARTIDA SE ENCERRA QUANDO É ATINGIDO O VALOR
                PARA O NÚMERO DE RODADAS INSERIDO PELOS USUÁRIOS, MAS TAMBÉM, QUANDO O TABULEIRO DE ALGUM DOS DOIS JOGADORES É TOTALMENTE 
                COMPLETO, OU SEJA,QUANDO O NÚMERO DE CASAS REVELADAS DE ALGUM DOS JOGADORES FOR IGUAL A ÁREA DO TABULEIRO.'''
                
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto) 
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto_j2)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)  
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)   
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute =  MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)   #PONTUAÇÃO DOS JOGADORES NO PLACAR    
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                print(f'TABULEIRO DE {jogador1}')
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                print(f'\nTABULEIRO DE {jogador2}') 
                EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                lista_vencedorj2 = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                num_rodadas -= 1
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador1)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 1.
            TABULEIRO_RESPOSTA(tabuleiro_j2,tabuleiro_oculto_j2,linhas_colunas,jogador2)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 2.
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
        
        elif termino == '2':
            TABELA(linhas_colunas,intervalo,tabuleiro)          #FORMAÇÃO DO TABULEIRO COM OS NÚMEROS REAIS DO JOGADOR 1.
            TABELA(linhas_colunas,intervalo,tabuleiro_j2)       #FORMAÇÃO DO TABULEIRO COM OS VALORES REAIS DO JOGADOR 2.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto)         #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 1.
            TABELA_OCULTA(linhas_colunas,tabuleiro_oculto_j2)      #FORMAÇÃO DO TABULEIRO MOSTRADO AOS JOGADORES DO JOGADOR 2.
            print(f'TABULEIRO DE {jogador1}')
            EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)              #EXIBIÇÃO DO TABULEIRO DO JOGADOR 1 AOS JOGADORES.
            print(f'\nTABULEIRO DE {jogador2}') 
            EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)           #EXIBIÇÃO DO TABULEIRO DO JOGADOR 2 AOS JOGADORES.
            '''NO CASO DE ENCERRAMENTO POR TABULEIRO(S) REVELADO(S), O TÉRMINO DA PARTIDA OCORRE QUANDO TODAS A CASAS 
            DO TABULEIRO DE ALGUM DOS JOGADORES JÁ FORAM REVELADAS'''
            while sum(casas_reveladas) != 25 and sum(casas_reveladas_j2) != 25:
                '''LOGO ABAIXO, FUNÇÃO DE RECEBIMENTO DA RESPOSTA DO JOGADOR, RETORNANDO A POSIÇÃO QUE FOI ESCOLHIDA E O CHUTE DO MESMO EM UMA TUPLA.'''
                tupla_resp_j1 = RESPOSTA(linhas_colunas,jogador1,tabuleiro_oculto)  
                tupla_resp_j2 = RESPOSTA(linhas_colunas,jogador2,tabuleiro_oculto_j2)
                '''NA LINHA ABAIXO, FUNÇÃO QUE RETORNA EM UMA TUPLA A APROXIMAÇÃO DOS JOGADORES E A SOMA REFERENTE A LINHA OU COLUNA QUE FOI ESCOLHIDA.'''
                tupla_aproximacao = APROXIMACAO(escolha_tab,tupla_resp_j1,tupla_resp_j2,tabuleiro,tabuleiro_j2)   
                pont = PONTUACAO(jogador1,jogador2,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2)   
                LISTA_VENCEDOR(escolha_tab,tupla_aproximacao,tupla_resp_j1,tupla_resp_j2,lista_vencedor,lista_vencedorj2)
                '''ABAIXO, RETORNA A ORDEM DO CHUTE DADO PELOS JOGADORES EM UMA TUPLA.'''
                tupla_ordem_chute =  MAIOR_MENOR_EXATO(jogador1,jogador2,tupla_resp_j1,tupla_resp_j2,tupla_aproximacao,lista_historico,rodadas)
                ADIÇÃO_LISTA_VENCEDOR(pont,escolha_tab,lista_vencedor,lista_vencedorj2,tupla_ordem_chute)
                '''NA LINHA ABAIXO, FUNÇÃO QUE REALIZA AS SUBSTITUIÇÕES DOS VALORES REAIS NO TABULEIRO COM 
                    OS VALORES OCULTOS (MOSTRADO AO JOGADORES)DE ACORDO COM AS INFORMAÇÕES ARMAZENADAS ATÉ ESSA PARTE DO CÓDIGO'''
                SUBSTITUICAO(casas_reveladas,casas_reveladas_j2,lista_exibidos_1volta,escolha_tab,pont,tabuleiro,tabuleiro_j2,tabuleiro_oculto,tabuleiro_oculto_j2, lista_vencedor,lista_vencedorj2,lista_numeros_exibidos,lista_numeros_exibidos_j2,pontos_jogador1,pontos_jogador2)
                PONTUACAO_PLACAR(jogador1, jogador2,pontos_jogador1,pontos_jogador2)    #PONTUAÇÃO DOS JOGADORES NO PLACAR  
                HISTORICO(lista_historico)   #EXIBE NA TELA O HISTÓRICO DE RODADAS NA PARTIDA.
                print(f'TABULEIRO DE {jogador1}')
                EXIBIÇÃO(tabuleiro_oculto,linhas_colunas)
                print(f'\nTABULEIRO DE {jogador2}') 
                EXIBIÇÃO(tabuleiro_oculto_j2,linhas_colunas)
                rodadas += 1
                lista_vencedor = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
                lista_vencedorj2 = []   #RESET DA LISTA DO VENCEDOR PARA AS PRÓXIMAS JOGADAS.
            '''NA LINHA ABAIXO, FUNÇÃO QUE EXIBE NA TELA, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS TOTAIS AO LADO DE CADA LINHA E ABAIXO DE CADA COLUNA.'''
            TABULEIRO_RESPOSTA(tabuleiro,tabuleiro_oculto,linhas_colunas,jogador1)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 1.
            TABULEIRO_RESPOSTA(tabuleiro_j2,tabuleiro_oculto_j2,linhas_colunas,jogador2)   #EXIBE, AO FINAL DA PARTIDA, O TABULEIRO COM AS SOMAS DO JOGADOR 2.
            VENCEDOR(jogador,jogador1,jogador2,pontos_jogador1,pontos_jogador2)   #EXIBE, AO FINAL DA PARTIDA, O JOGADOR VENCEDOR.
        