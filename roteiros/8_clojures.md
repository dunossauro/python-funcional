
# Clojures

Já passamos funções como argumento, já retornamos funções e até já mudamos o comportamento das mesmas. Mas tem uma coisa que ainda não fizemos: Definir uma função no corpo de outra função:


```Python
def func_0():
    def func_1():
        pass
    pass
```

Jaber diz: `Mas isso é uma classe! eu sabia que programação funcional era legal, mas realmente tudo é orientação a objetos.`

Tá Jaber, eu entendo seu ponto de vista, mas vou usar uma definição muito boa do livro do Mertz:

"Uma classe são dados com operações anexadas (...) Uma Clojure são operações com dados anexados"

Viu? muda totalmente o modo de ver... Vamos nos explicar de maneira simples em breve, mas vamos entender as clojures e figir que classes não existem, só por alguns minutos.

Vamos imaginar que temos que guardar um valor dentro de um função. Essa função vai ser uma função que exclusivamente armazena um valor e uma função dentro do seu escopo:


```Python
def func_externa(val_1):
    """
    A função externa recebe um valor que só vai existir dentro do seu contexto
    """
    def func_interna(val_2):
        """
        A função interna recebe um valor e retona a soma dos dois valores.

        val_1 está no contexto da função interna, mas val 2 não está no
            contexto da função externa
        """
        return val_1 + val_2
    # aqui quando a função externa for chamada ela retorna a função interna e compartilha seus valores
    return func_interna
```

Vamos usar esse código antes de qualquer explicação mirabolante:

```Python
var_func = func_externa(5)

var_func(5) # 10
```

Como dá pra notar a função externa é atribuida a uma variável e essa variável executa a função interna. Parece complicado, mas na verdade é bem simples. Vamos recaptular algumas coisas.

Como em python as funções podem ser definidas em qualquer contexto e armazenada em qualquer lugar imagine que a `func_externa()` está sendo atribuída a uma variável. Em um contexto totalmente normal, como fizemos com as funções anônimas até agora. A diferença é um valor, ou uma quantidade `n` de valores, vão ser passadas no momento da atribuição. Esses valores vão ficar armazenados na função de maneira imutável, vamos reaproveitar o código com alguns exemplos:

```Python
soma_um = func_externa(1)
soma_dois = func_externa(2)
soma_tres = func_externa(3)
soma_quarto = func_externa(4)
soma_cinco = func_externa(5)

# vamos somar tudo com 0
soma_um(0) # 1
soma_dois(0) # 2
soma_tres(0) # 3
soma_quarto(0) # 4
soma_cinco(0) # 5
```

Bom, agora imagino que tenha ficado um pouco mais claro. Fixamos valores na `func_externa()` e armazenamos em variáveis (`soma_um()`, `soma_dois()`, `soma_tres()` ...) cada respectiva função mostra  valor inicial da função.

Quando executamos a função `soma_um(n)` qualquer valor que for usado em `n` vai ser somado a ao valor fixo na função externa `func_externa(1)`, ou seja, `1`. Vale lembrar que a soma é executa porque esse é o comportamente da função interna `func_interna()`. Vamos tentar outra vez:
