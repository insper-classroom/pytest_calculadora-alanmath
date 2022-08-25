import numpy as np
import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores


@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1,v2)

@pytest.mark.op_simples
def test_subtrai_2_valores_positivos():
    v1 = 5.0
    v2 = 3.0
    assert 2 == sub(v1,v2)

@pytest.mark.op_simples
def test_multiplica_2_valores_positivos():
    v1 = 5.0
    v2 = 3.0
    assert 15 == multiplicacao(v1,v2)

@pytest.mark.op_simples
def test_divide_2_valores_positivos():
    v1 = 6.0
    v2 = 3.0
    assert 2 == divisao(v1,v2)

@pytest.mark.op_simples
def test_media_lista_valores_positivos():
    v = [5,3]

    assert 4 == media_lista_valores(v)



@pytest.mark.exercicio_1
def test_divisao_por_zero():
    v1 = 2
    v2 = 0
    assert np.inf == divisao(v1,v2)

@pytest.mark.exercicio_1
def test_string_em_vez_de_numero_media_valores():
    v = [2,4,'n']
    assert 3 == media_lista_valores(v)

@pytest.mark.exercicio_1
def test_lista_vazia_media_valores():
    v=[]
    assert 0 == media_lista_valores(v)