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


## 10.? Decoradores com parâmetros (closures de closures)

```Python
def param(args):
    def funcao_externa(func):
        def funcao_interna(*args):
            return func(*args)
        return func_args
    return real_decorator
```
