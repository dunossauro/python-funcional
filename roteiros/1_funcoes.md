# Funções

Esse vídeo vai se limitar a falar da estrutura básica das funções em python, sem entrar profundamente em cada um dos tópicos. Será uma explanação de código e abrir a cabeça para novas oportunidades de código mais pythonico

## Funções como objeto de primeira classe

Funções como objeto de primeira classe, são funções que se comportam como qualquer tipo nativo de uma determinada linguagem. Por exemplo:

```python
# uma lista

lista = [1, 'str', [1,2], (1,2), {1,2}, {1: 'um'}]
```

Todos esses exemplos são tipos de objetos de primeira classe em Python, mas no caso as funções também são, como assim? Pode-se passar funções como parâmetro de uma outra função, podemos armazenar funções em variáveis, pode-se definir funções em estruturas de dados:

```python
# Funções como objeto de primeira classe

func = lambda x: x # a função anônima, lambda, foi armazenada em uma variável

def func_2(x):
    return x + 2

lista = [func, func_2] # a variável que armazena a função foi inserida em uma estrutura, assim como uma função gerada com def

lista_2 = [lambda x: x, lambda x: x+1] # aqui as funções foram definidas dentro de uma estrutura
```

Como nota-se, em python, as funções podem ser inseridas em qualquer contexto e também geradas em tempo de execução

## Funções puras

Funções puras, são funções que não sofrem interferência do meio externo. Vamos começar pelo exemplo ruim:

```python

valor = 5

def mais_cinco(x):
    return x + valor

assert mais_cinco(5) == 10 # True

valor = 7

assert mais_cinco(5) == 10 # AssertionError
```

mais_cinco() é o exemplo claro de uma função que gera efeito colateral. Uma função pura deve funcionar como uma caixa preta, todas as vezes em que o mesmo input for dado nela, ela terá que retornar o mesmo valor. Agora vamos usar o mesmo exemplo, só alterando a linha do return

```python

valor = 5

def mais_cinco(x):
    return x + 5

assert mais_cinco(5) == 10 # True

valor = 7

assert mais_cinco(5) == 10 # True
```

Pode parecer trivial, mas muitas vezes por comodidade deixamos o meio influenciar no comportamento de uma função.

## Funções de ordem superior (HOFs)

Funções de ordem superior são funções que recebem funções como argumento(os) e/ou retornam funções como resposta. Existem muitas funções embutidas em python de ordem superior como: `map, filter, zip` e praticamente todo o módulo functools `import functools`. Porém, nada impede de criarmos novas funções de ordem superior. Um ponto a ser lembrado é que map e filter não tem mais a devida importância em python com a entrada das comprehensions, o que nos faz escolher única e exclusivamente por gosto, apesar de comprehensions serem mais legíveis. Mas não se preocupe, teremos um vídeo só para esses comparações.

Vamos lá:

```python

func = lambda x: x+2 # uma função simples, soma mais 2 a qualquer inteiro

def func_mais_2(funcao, valor):
    """
    Executa a função passada por parâmetro e retorna esse valor somado com dois

    Ou seja, é uma composição de funções:

    Dado que func(valor) é processado por func_func:
        func_mais_2(func(valor)) == f(g(x))
    """
        return funcao(valor) + 2
```

Um ponto a tocar, e o que eu acho mais bonito, é que a função vai retornar diferentes respostas para o mesmo valor, variando a entrada da função. Nesse caso, dada a entrada de um inteiro ele será somado com 2 e depois com mais dois. Mas, vamos estender este exemplo:

```python

func = lambda x: x+2 # uma função simples, soma mais 2 a qualquer inteiro

def func_mais_2(funcao, valor):
    """
    Executa a função passada por parâmetro e retorna esse valor somado com dois

    Ou seja, é uma composição de funções:

    Dado que func(valor) é processado por func_func:
        func_mais_2(func(valor)) == f(g(x))
    """
        return funcao(valor) + 2

assert func_mais_2(func, 2) == 4 # true

def func_quadrada(val):
    """
    Eleva o valor de entrada ao quadrado
    """
    return val * val

assert func_mais_2(func_quadrada, 2) == 6 # true
```

#### Um exemplo usando funções embutidas:

```python
lista_0 = [0, 1, 2]
lista_1 = [2, 1, 0]

list(zip(lista_0, lista_1)) == [(0, 2), (1, 1), (2, 0)]

```

como falaremos mais adiante, a função embutida zip itera em duas sequências e nos retorna uma lista de tuplas como os elementos que contém o mesmo index na iteração.

## `__call__`

Por que falar de classes? Lembre-se Python é uma linguagem construída em classes, e todos os objetos que podem ser chamados/invocados, implementam o método `__call__`:

Em uma função anônima:
```python
func = lambda x: x

'__call__' in dir(func) # True
```

Em funções tradicionais:
```python
def func(x):
    return x

'__call__' in dir(func) # True
```

Isso quer dizer que podemos gerar classe que se comportam como funções?

SIIIIIM. Chupa Haskell

## Funções geradoras

Embora faremos um vídeo extremamente focado em funções geradoras, não custa nada dar uma palinha, não?

Funções geradoras, são funções que nos retornam um iterável. Mas ele é lazzy, vamos só para o exemplo de uso, muitos conceitos precisam ser esclarecidos antes de entendermos profundamente o que acontece com elas, mas digo logo. São funções lindas <3

Para que uma função seja geradora, em tese, só precisamos trocar o return por yield:

```python

def gen(lista):
    for elemento in lista:
        yield elemento

gerador = gen([1, 2, 3, 4, 5])

next(gerador) # 1
next(gerador) # 2
next(gerador) # 3
next(gerador) # 4
next(gerador) # 5
next(gerador) # StopIteration
```

Passando bem por alto, uma função geradora nos retorna um iterável que é preguiçoso. Ou seja, ele só vai efetuar a computação quando for chamado. Mas no vídeo seguinte vamos discutir só, e mesmo que superficialmente, sobre iteradores 
