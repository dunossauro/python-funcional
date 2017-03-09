## Funções de ordem superior p.2

Segundo Steven Lott, podemos criar três tipos de HOFs diferentes

1. Funções que aceitam funções como argumento
2. Funções que retornam uma função ou uma classe com `__call__`
3. Funções que aceitam e retornam funções (Geralmente são decoradores)

Contudo, vamos exercitar o fato de criar funções de ordem superior, apenas. Vamos tentar copiar algumas do escopo, vamos nos divertir. Pronto?


### Funções que aceitam funções

Essa vocês já estão matando no peito, eu sei. Vamos ao código então:

```Python
def map_clone(func, sequencia):
    """
    Função geradora clone do map

    Args:
        - func: Função que será aplicada a cada elemento da sequência
        - sequencia: Iterável a ser consumido pela função
    """
    for el in sequencia:
        yield func(el)
```

Olha, eu sei que parecia que já tinhamos falado sobre tudo, mas esse foi o melhor momento para falar sobre as funções geradoras.

#### funções geradoras

Funções geradoras 'trocam' o `return` por `yield`. Você só precisa disso para que sua função seja um gerador e retorne lazy como as funções embutidas do python. Só que existe um ponto, as funções retornam iteráveis, ou seja, teremos que usar o mesmo construtor de objetos que usamos antes:

```Python
map_clone(lambda x: x**2, [1, 2, 3]) # <generator object map_clone at 0x7faee9511e60>

list(map_clone(lambda x: x**2, [1, 2, 3])) # [1, 4, 9]
```
