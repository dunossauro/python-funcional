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

Funções geradoras 'trocam' o `return` por `yield`. Você só precisa disso para que sua função seja um gerador e retorne lazy como as funções embutidas do python. Só que existe um ponto, as funções retornam iteráveis, ou seja, teremos que usar os mesmos construtores (`list`, `tuple`, etc..) de objetos que usamos antes:

```Python
map_clone(lambda x: x**2, [1, 2, 3]) # <generator object map_clone at 0x7faee9511e60>

# chamando o construtor list()
list(map_clone(lambda x: x**2, [1, 2, 3])) # [1, 4, 9]
```

Vamos explanar mais a ideia de funções geradoras. No nosso exemplo com yield usamos um laço for, mas vamos tentar outra abordagem:

```Python

def f_geradora():
    yield 1
    yield 2
    yield 3
    yield 4

gen = f_geradora()

next(gen) # 1
next(gen) # 2
next(gen) # 3
next(gen) # 4
next(gen) # StopIteration

gen = f_geradora()
list(gen) # [1, 2, 3, 4]
```

A função se transforma em um iterável, um comportamento diferente de todas as funções que vimos até agora.

Vamos tentar entender... yield funciona como um break. Tá, vamos tentar de novo. É como se a execução da função tivesse um pause. Vamos explorar mais o último exemplo:

```Python

def f_geradora():
    print('aqui vai o primeiro valor')
    yield 1
    print('Segundo chegando')
    yield 2
    print('Terceiro, tá quase acando')
    yield 3
    print('Quarto e último')
    yield 4

gen = f_geradora()

next(gen)
# aqui vai o primeiro valor
# 1
next(gen)
# Segundo chegando
# 2
next(gen)
# Terceiro, tá quase acando
# 3
next(gen)
# Quarto e último
# 4
next(gen)
# StopIteration

gen = f_geradora()
list(gen)
# aqui vai o primeiro valor
# Segundo chegando
# Terceiro, tá quase acando
# Quarto e último
# [1, 2, 3, 4]

```

Deu pra sacar agora? A função geradora executa tudo que tem que ser executado até o yield e para. Ultimo, eu juro, aí vamos um pouco mais fundo e voltamos as HOFs:

```Python
def gen_test():
    for x in [1, 2, 3]:
        print(x)

    yield 'primeiro laço'

    for x in [4, 5, 6]:
        print(x)

    yield 'segundo laço'
list(gen_test())
# 1
# 2
# 3
# 4
# 5
# 6
#['primeiro laço', 'segundo laço']
```

A função executa exatamente o que tem ser executado e nos retorna apenas o valor do yield. Esse tipo de implementação é a base pra entender as co-rotinas em python, mas isso é assunto pra outra hora e nem vamos falar sobre isso, pois foge do nosso escopo. Porém, você está avisado, pode pesquisar depois sobre a relação de `contextmanager` e `yield`.

Você está o bixão do mundo python já, então vamos complicar esse `yield` usando mais um amiguinho dele chamado `yield from`. Tá, tava tudo legal, mas você vai aprender o que é uma monad agora. Eu juro.

```Python
def gen():
    for el in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        yield el

def gen_flat():
    for el in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        yield from el

list(gen()) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
Seu coração vai chorar agora
"""
list(gen_flat()) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

CARACAS, como assim? o que aconteceu aqui? Vamos pensar que um map normal faria o que `gen()` faz. Mas um flatmap faria o que `gen_flat()` faz.

Quando usamos yield em um laço, ele retorna cada valor contido em uma sequência, de maneira preguiçosa. Só que a sequência contém outra sequência, ele vai retorna a sequência, pois cada uma é um elemento independente da sequência, mesmo sendo uma sequência. o `yield from` vai retornar um iterável preguiçoso dessa nova sequência, a contida na sequência anterior. Ou seja, ele vai nos retornar uma única sequência. Por isso nome 'flat', é como se a sequência de sequências fosse comprimida em uma única sequência. Para entender isso vou deixar como referência um [vídeo do funfunfunctions](https://www.youtube.com/watch?v=9QveBbn7t_c&t=167s) que fala exatamente sobre isso. Vale a pena.


Agora que você já conhece mais um tipo de função, vamos voltar as nossas HOFs

## Escrevendo nossas próprias HOFs


Como já sabemos e já foi dito exaustivamente. Funções são objetos de primeira classe em Python. Já sabemos. Ok.

Então como já entendemos tudo isso, vamos só usar alguns exemplos de funções que recebem funções.

Vamos trabalhar em outra frente então:

1. Mapear sequências mais complexas

Vamos supor, que temos uma lista de tuplas:

```python
# Sim, já vimos algo parecido no vídeo anterior

# Hora, minuto, segundo
tempo = [(12, 17, 50),
         (17, 28, 51),
         (23, 27, 26)]
```

E vamos trabalhar nessa sequência que é um pouco mais complexa do que as que usamos até agora.

Vamos supor que esse horário que está no padrão que vai de 00:00:00 até 24:59:59. E a resposta que nós esperamos é um horário am/pm que vai de 01:00:00 até 12:59:59. Só que a saída terá que ser uma nova tupla, com quatro elementos `(H, M, S, (am ou pm))`. Para isso, a nossa função de mapeamento terá que ser um pouco mais iteligente

```Python
tempo = [(13, 17, 50),
         (17, 28, 51),
         (23, 27, 26)]


hora = lambda x: (x[0] % 12, 'am') if x[0] > 12 else (x[0] % 12, 'pm')

print(list(map(hora, tempo)))
```
