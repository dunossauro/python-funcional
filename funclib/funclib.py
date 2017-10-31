"""
Nossas funções super especiais.

Do vídeo 7
"""


def tail(seq, n=1, key=None):
    """
    Pega n elementos do fim da sequência.

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
    Pega n elementos do inicio da sequência.

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


def twice(val, func, _iter=False):
    """
    Executa duas vezes a mesma função.

    Evita casos como func(func(val)).

    Args:
        - val: Valor a ser aplicada a função
        - func: Função a ser executada duas vezes em val
        - _iter: Decide se a iteração vai ser aplicada (com map) ou não

    >>> mul_2 = lambda x: x * 2
    >>> twice(10, mul_2)
    40

    >>> twice([1, 2, 3], mul_2)
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

    >>> twice([1, 2, 3], mul_2, True)
    <map at ...>

    >>> list(twice([1, 2, 3], mul_2, True))
    [4, 8, 12]
    """
    from functools import partial
    if not _iter:
        return func(func(val))
    else:
        map_part = partial(map, func)
        return map_part(map_part(val))


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
Função emprestada da lib [toolz](https://github.com/pytoolz/tool
"""


def pipe(seq, *funcs):
    """
    Executa um iterável de funções em uma sequência.

    Args:
        - seq: Sequência a ser processada
        - *funcs: lista de funções a processarem seq

    EX:
    >>> from functools import partial
    >>> soma_2 = partial(map, lambda x: x + 2)
    >>> mul_2 = partial(map, lambda x: x * 2)

    >>> pipe([1, 2, 3], soma_2)
    [3, 4, 5]

    >>> pipe([1, 2, 3], mul_2)
    [2, 4, 6]

    >>> pipe([1, 2, 3], soma_2, mul_2)
    [6, 8, 10]
    """
    for func in funcs:
        seq = func(seq)
    return seq
