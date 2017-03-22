## Nossa primeira biblioteca de funções

O objetivo desse vídeo é construir uma gama de funções simples para que possamos exercitar tudo que aprendemos. Vamos fazer 8 funções legais de usar e que podem ajudar em muitos casos. Patiu? vem comigo.


### `tail()`

Vamos tentar fazer uma função que pode ser uma HOF ou não? parecida com aquelas do python, que recebem `key`?

```Python
def tail(seq, n=1, key=None):
    return seq[-n:] if not key else key(seq[-n:])
```

Pode parecer uma função extremamente simples, mas ela é bem legal. Dá pra conseguir muitos resultados legais com ela:

```Python
'Por padrão vai retornar só o ultimo'
tail([1,2,3,4]) # [4]

'Aqui usamos n, que nesse caso retorna os ultimos 3 elementos'
tail([1,2,3,4], 3) # [2, 3, 4]

'O resultado reverso'
tail([1,2,3,4], 3, reversed) # <list_reverseiterator at xpto>

list(tail([1,2,3,4], 3, reversed)) # [4, 3, 2]

'Uma aplicação complexa'
list(tail([1,2,3,4], 2, partial(map, lambda x: x**2))) # [9, 16]
```

### `head()`

Aqui vamos fazer a mesma coisa, só para o começo da sequência:

```Python
def head(seq, n=1, key=None):
    return seq[:n] if not key else key(seq[:n])
```

Se você parar pra pensar, a única coisa que mudou aqui foi o slice ([-n:] -> [:n]). Então, vamos fazer as mesmas operações:

```Python
'Por padrão vai retornar só o primeiro'
head([1,2,3,4]) # [1]

'O resultado reverso'
head([1,2,3,4], 3, reversed) # <list_reverseiterator at xpto>

'Uma aplicação complexa'
list(head([1,2,3,4], 2, partial(map, lambda x: x**2))) # [1, 4]
```

### `take()`

A função take é uma função muito legal implementada na lib [fn.py](https://github.com/kachayev/fn.py) e eu gosto muito dela. Vamos ver como ela funciona?

```Python
list(take(4, [1,2,3,4,5])) # [1,2,3,4]
```

Deu pra perceber que ela é bem poderosa, não? Em qualquer sequência podemos pegar n elementos. Uma coisa legal é que podemos consumir parcialmente os geradores e isso é uma coisa linda.

```Python
def gen():
    yield 1
    yield 2
    yield 3
    yield 4

list(take(2, gen())) # [1, 2]

func_gen = gen()
list(take(2, func_gen)) # [1, 2]
list(take(2, func_gen)) # [3, 4]
```

Vamos implementar uma função dessa?

```Python
def take(n, seq):
    """
    Pega n elementos de um sequência

    Args:
        - n: Número de elementos retirados da sequência
        - seq: Sequência da qual os números serão removidos
    """
    _iter = iter(seq)
    for el in range(n):
        yield next(_iter)

list(take(2, [1, 2, 3])) # [1, 2]
```

Agora que você já sabe tudo que foi usado nessa função (iter, yield, next) as coisas ficam tão simples de entender, não?

Vamos testar com um gerador outra vez, usando o mesmo código do exemplo passado:

```Python
def gen():
    yield 1
    yield 2
    yield 3
    yield 4

list(take(2, gen())) # [1, 2]

func_gen = gen()
list(take(2, func_gen)) # [1, 2]
list(take(2, func_gen)) # [3, 4]
```

Olha só que mágico, não? A função implementada na biblioteca fn não é construída exatamente dessa maneira, eles usam uma função mágica do módulo `itertools` chamada `islice` que vamos ver em um vídeo futuro dedicado especialmente ao itertools. Mas vai dizer que não ficou simples?

Jaber diz: `Mas a função take não faz a mesma coisa que a função head???`

Sim e não. Se você pensar em sequências que aceitam slice (seq[]) ela, `head()` é uma função bem legal. Resolve problemas de listas etc... Ela é uma função que pode ser legal em iterações, em pegar o primeiro elemento em alguns casos. A função `take()` é MUITO mais poderosa, mas também não é bala de prata. Apesar do fato de ela consumir geradores, o que almenta seu poder, ela também retorna um gerador, o que faz com que não possamos usar o `len()` dela, embora você saiba o tamanho que pediu no primeiro argumento. O retorno não pode ser acessado por posição e tem que ser constrido com alguma outra função, como (`list()`, `tuple()`, `set` ...). Mas a diferença mais gritante é que `take()` consome parcialmente iteráves e a função `head()` é uma HOF que aceita uma função pra processar a cabeça da lista. Com isso, elas exibem retornos completamente diferentes.

### `drop()`

Drop também é uma função que vamos pegar emprestado de [fn.py](https://github.com/kachayev/fn.py), embora também não vamos usar sua implementação oficial. Vamos ver como ela funciona:

```Python
list(drop(4, [1,2,3,4,5,6,7,8,9])) # [5, 6, 7, 8, 9]
```

### `insert()`

### `order_insert()`

### `pipe()`

Função emprestada da biblioteca [toolz](https://github.com/pytoolz/toolz)
