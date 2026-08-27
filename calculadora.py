GITHUB_TOKEN = "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        return a / b
