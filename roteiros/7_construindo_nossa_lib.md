## Nossa primeira biblioteca de funções

O objetivo desse vídeo é construir uma gama de funções simples para que possamos exercitar tudo que aprendemos. Vamos fazer 15 funções legais de usar e que podem ajudar em muitos casos. Patiu? vem comigo.


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

### `insert()`

### `order_insert()`
