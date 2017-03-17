"""
Nossa funções super especiais.

Do vídeo 7
"""


def tail(seq, n=1, key=None):
    """
    Pega ao n elementos do fim da sequência.

    Se uma função que retorna lazy for usada em key, o retorno será lazy

    Args:
        - seq: Sequência que será iterada
        - n: Número de elementos que vamos usar do fim da sequência
        - key: função que será implementada a sequência

    >>> tail([1,2,3,4])
    [4]
    >>> list(tail([1,2,3,4], 3, reversed))
    [4, 3, 2]
    >>> list(tail([1,2,3,4], 2, partial(map, lambda x: x**2)))
    [9, 16]
    """
    return seq[-n:] if not key else key(seq[-n:])


def head(seq, n=1, key=None):
    """
    Pega ao n elementos do inicio da sequência.

    Se uma função que retorna lazy for usada em key, o retorno será lazy

    Args:
        - seq: Sequência que será iterada
        - n: Número de elementos que vamos usar do fim da sequência
        - key: função que será implementada a sequência

    >>> head([1,2,3,4])
    [1]
    >>> list(head([1,2,3,4], 3, reversed))
    [3, 2, 1]
    >>> list(head([1,2,3,4], 2, partial(map, lambda x: x**2)))
    [1, 4]
    """
    return seq[:n] if not key else key(seq[:n])
