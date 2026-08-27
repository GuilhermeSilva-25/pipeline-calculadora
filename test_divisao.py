from calculadora import divisao


def test_divisao():
    assert divisao(10, 2) == 5


def test_divisao_por_zero():
    assert divisao(10, 0) == "Não é possível dividir por zero."
