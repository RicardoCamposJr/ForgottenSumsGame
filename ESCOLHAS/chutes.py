from VALIDAÇÃO.validações import *

def RESPOSTA(linhas_colunas,jogador,tabuleiro_oculto):
    resp_jogador = VALIDAR_ESCOLHA(linhas_colunas,jogador)
    resp_jogador = LIBERAÇÃO_LINHAxCOLUNA(linhas_colunas,jogador,resp_jogador,tabuleiro_oculto)
    chute_jogador = int(VALIDAR_CHUTE(resp_jogador,jogador))
    return resp_jogador,chute_jogador