import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    
    '''
    if vb == 0:
        return np.inf
    return va / vb

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''
    if len(v) == 0:
        return 0
    nova_lista = []
    for elemento in v:
        if isinstance(elemento, int) or isinstance(elemento, float):
            nova_lista.append(elemento)

    return np.mean(nova_lista)
