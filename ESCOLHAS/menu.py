from VALIDAÇÃO.validações import *

def APRESENTAÇÃO():
    print('-=' * 40)
    print('\t\t\t\t\033[1;32mBEM VINDO AO:\033[m')
    print('-=' * 40)
    print('\t\t\t\033[1;32mJOGO DAS SOMAS ESQUECIDAS\033[m')
    print('-=' * 40)

# FUNÇÕES DE MENU DO INÍCIO DO JOGO:

def ESCOLHA_TABULEIROS():
    print('-=' * 35)
    print('\t\t\t\033[1;32mNúmero de tabuleiros\033[m')
    print('-=' * 35)
    escolha_tabuleiros = VALIDAR_TAB()
    return escolha_tabuleiros

def ESCOLHA_NIVEL():
    print()
    print('-=' * 35)
    print('\t\t\t\t\033[1;32mNível\033[m')
    print('-=' * 35)
    nivel = VALIDAR_NIVEL()
    return nivel

def ESCOLHA_TERMINO():
    print()
    print('-=' * 35)
    print('\t\t\t\033[1;32mTérmino da partida\033[m')
    print('-=' * 35)
    termino = VALIDAR_TERMINO()
    return termino