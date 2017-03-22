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


def insert():
    pass


def order_insert():
    pass


"""
Funções que pegamos emprestadas, e adaptamos ao nosso nível de conhecimento,
 da lib fn.py (https://github.com/kachayev/fn.py/)
"""


def take(n, seq):
    """
    Pega n elementos de um sequência.

    Args:
        - n: Número de elementos retirados da sequência
        - seq: Sequência da qual os números serão usados
    """
    _iter = iter(seq)
    for el in range(n):
        yield next(_iter)


def drop(n, seq):
    """
    Remove n elementos de um sequência.

    Args:
        - n: Número de elementos retirados da sequência
        - seq: Sequência da qual os números serão removidos
    """
    _iter = iter(seq)
    for i, el in enumerate(seq):
        if i < n:
            next(_iter)
        else:
            yield next(_iter)


"""
Funções que pegamos emprestadas, e adaptamos ao nosso nível de conhecimento,
 da lib [toolz](https://github.com/pytoolz/tool
"""


def pipe(seq, *funcs):
    for func in funcs:
        seq = func(seq)
    return seq
