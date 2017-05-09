# 10. Decoradores

Agora que você e o Jaber já estão craques em closures os decoradores não apresentam medo, pois tudo em decoradores são closures. No tópico 9.5 você usou um decorador e embora eles não tenham sido devidamente explicados vamos entender tudo sobre eles agora.


## 10.1 Qual a cara de um decorador?

Um decorador nada mais é que um açúcar sintático para as closures. Viu? você já sabe tudo sobre eles, sem mesmo saber deles. Vamos entender essa composição diferente.

Uma closure é aplicada em Python assim:

```Python
closure(funcao(argumentos))
```

Invocamos a função externa como uma função e passamos como parâmetro a nossa função com seus argumentos. E os decorares?

```Python
@closure
def funcao(argumentos):
    pass
```

Ou seja, é apenas açúcar sintático. Contudo a apresentação é muito explicita, pelo menos pra mim. Fica evidente que a função `closure` decora a `funcao`.
Outro ponto importante e que difere, apenas em nível sintático, é que a função é decorada apenas quando é definida.

Com isso se tentarmos executar um código, como o código a baixo, executarimos a closure duas vezes na função:

```Python
@closure
def funcao(argumentos):
    pass

closure(funcao(argumentos)) # linha do problema
```

Agora todas as vezes que você encontrar um `@` em cima de uma definição de uma função, você já sabe do que se trata.

## 10.2 Montando nosso primeiro decorador

No tópico 8 iniciamos nossa discução sobre o uso de closures, vamos implementar closures de uma maneira mais eficiente e mais agradável visualmente.

Para iniciar vamos pensar em uma simples função que soma dois números como fizemos ao introduzir o conceito de funções nos primeiros tópicos, para ficar evidentemente simples a utilização de decoradores, mas falar é fácil. Vamos ao código:

```Python
def soma(x, y):
    """
    Função que efetivamente soma dois números
    """
    return x + y
```

Não é preciso ser um gênio como o Jaber para saber como usar essa função:

```Python
soma(1, 1) # 2
soma(2.0, 2.0) # 4.0
soma(3j + 3j) # 6j
```

Ela funciona efetivamente com todos os tipos de números em Python. Embora seja possível imaginar que nossa função usa o operador `+`. Ele faz com que nossos objetos numéricos invoquem seu método mágico interno `__add__` ou `__radd__`. O único problema é que outros objetos em Python também implementam esse método. Strings e listas podem usar o `__add__`, mas somente entre sí. Vale lembrar aqui que Python é uma linguagem fortemente tipada. Eu não vou conseguir somar uma string com um inteiro ou com uma lista por exemplo.

Vamos pensar que nossa função `soma()` só trabalha com números (complexos, inteiros e de ponte flutuante). Então a validação da entrada vai ter que ser feita, pois nós não queremos somar strings e listas.

`Jaber diz: Por que não deixamos a função receber de qualquer coisa, assim nossa função pode ser usada para somar listas com listas, strings com strings? Nossa função vai ser muito mais poderosa.`

Calma Jaber, existe um problema em não validar os valores. Se as entradas forem de tipos diferentes a função vai retornar um `TypeError` e não vai ser muito legal para quando o usuário da nossa função estiver usando. Vamos entender isso, para que fique claro:

```Python
soma('Jaber', 2)
# TypeError: must be str, not int
```

Esse comportamento não é legal, imagina quatos tipos diferentes de erros podem ocorrer por isso? Vamos resolver de uma maneira simples:


```Python
from numbers import Number

def soma(x, y):
    """
    Função que soma dois números.

    isinstance faz uma comparação e valida um valor
        é de uma determinada classe.

    Caso um deles não seja, um erro vai ser
        forçado e a mensagem vai ser exibida
    """
    if isinstance(x, Number) and isinstance(y, Number):
        return x + y
    raise TypeError('Insira somente números (int, complex, float)')
```

Tá, ficou bonito. Vamos usar:

```Python
soma(1, 1) # 2
soma(2.0, 2.0) # 4.0
soma(3j, 3j) # 6j
```

Até então tudo está exatamente igual, mas vamos tentar usar outros tipos de dados:

```Python
soma(1, [1]) # TypeError: Insira somente números (int, complex, float)
soma(1, 'Jaber') # TypeError: Insira somente números (int, complex, float)
soma((1, 2, 3), 1) # TypeError: Insira somente números (int, complex, float)
```

`Jaber diz: Hmmmmmmm. Muito bonito, falou muito e nada de decoradores`


Ok, vamos lá. Você fez tudo isso, mas agora eu vou te pedir uma função que faz multiplicação e ela também só pode receber números:

```Python
from numbers import Number

def mul(x, y):
    if isinstance(x, Number) and isinstance(y, Number):
        return x * y
    raise TypeError('Insira somente números (int, complex, float)')


mul(1, 2) # 2
mul(1, [1]) # TypeError: Insira somente números (int, complex, float)
```

Você entendeu tudo Jaber, mas esqueceu de tudo que falamos sobre closures? Agora vamos ser inteligentes e usar as closures que aprendemos:

```Python
def validate_numbers(func):
    """
    Closure que decora a função.
    """
    def _validate(x, y):
        """
        Executa a validação e retorna a execução da função.
        """
        if isinstance(x, Number) and isinstance(y, Number):
            return func(x, y)
        raise TypeError('Insira somente números (int, complex, float)')
    return _validate
```

Você concorda que só temos o código em um único lugar e podemos decorar as duas funções e executar um código simples dentro da função? Vamos validar os valores com a closure `validate_numbers` e aplicar valores na função para testar:

```Python
@validate_numbers
def soma(x, y):
    return x + y

@validate_numbers
def mul(x, y):
    return x * y

soma(1, 1) # 2
soma(2.0, 2.0) # 4.0
soma(3j + 3j) # 6j
mul(1, 1) # 2
mul(2.0, 2.0) # 4.0
mul(3j, 3j) # (-9+0j)
```

Agora `validate_numbers` além de decorar nossas funções com a closure pode ser usado para qualquer tipo de funções que recebem dois argumentos (claro a validação pode não ser a mesma, mas funciona). Mas e os erros?

```Python
soma(1, 'Jaber') # TypeError: Insira somente números (int, complex, float)
mul(1, [1]) # TypeError: Insira somente números (int, complex, float)
```

Tudo funcionou muito bem. Vamos tentar entender um pouco mais sobre a natureza dos decoradores.

## 10.2 Usando um pouco melhor a função externa

## 10.? Decoradores com parâmetros (closures de closures)

```Python
def param(args):
    def funcao_externa(func):
        def funcao_interna(*args):
            return func(*args)
        return func_args
    return real_decorator
```
