
# Closures

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

Viu? muda totalmente o modo de ver... Vamos nos explicar de maneira simples em breve, mas vamos entender as closures e fingir que classes não existem, só por alguns minutos.

Vamos imaginar que temos que guardar um valor dentro de um função. Essa função vai ser uma função que exclusivamente armazena um valor e uma função dentro do seu escopo:


```Python
def func_externa(val_1):
    """
    A função externa recebe um valor que só vai existir dentro do seu contexto
    """
    def func_interna(val_2):
        """
        A função interna recebe um valor e retorna a soma dos dois valores.

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

Como dá pra notar a função externa é atribuída a uma variável e essa variável executa a função interna. Parece complicado, mas na verdade é bem simples. Vamos recapitular algumas coisas.

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

Quando executamos a função `soma_um(n)` qualquer valor que for usado em `n` vai ser somado a ao valor fixo na função externa `func_externa(1)`, ou seja, `1`. Vale lembrar que a soma é executada porque esse é o comportamento da função interna `func_interna()`. Vamos tentar outra vez:

```Python
def diga_oi(saudacao):
    """
    A funão diga_oi armazenada a sua saudação
    """
    def nome_pessoa(nome):
        """
        A função nome_pessoa retorna a saudação somada ao nome da pessoa
        """
        return '{} {}'.format(saudacao, nome)
    return nome_pessoa

oi_pirata = diga_oi('Ahoy!') # Definição de diga_oi (função externa) fixando Arroy

oi_pirata('Eduardo') # Ahoy! Eduardo
oi_pirata('Jaber') # Ahoy! Jaber
oi_pirata('Python') # Ahoy! Python
```

Nesse contexto a função fixou uma variável `Ahoy!` que não pode ser modificada e toda vez que é chamada responde com a união do argumento fixo com a variável passada como parâmetro.

Mas vamos tentar fixar um dicionário de idiomas pra `diga_oi()`? Por exemplo, a função externa agora não vai receber nenhum argumento, mas vai ter dentro do seu escopo um dicionário com os idiomas:

```Python
dic = {'pirata': 'Ahoy', 'ingles':'Hello', 'portugues': 'Olá'}
```

Uma vantagem de definir esse dicionário dentro da função é que ele vai ficar isolado das variáveis globais, o que faz ele não gerar efeito colateral e isso é muito positivo:

```Python
def diga_oi():
    """
    Definição de uma variável (dic) no escopo local da função.
    """

    dic = {'pirata': 'Ahoy', 'ingles':'Hello', 'portugues': 'Olá'}

    def nome_pessoa(idioma, nome):
        """
        Agora a função interna ficou com a responsabilidade dos dois parâmetros

        Mas o dicionário ainda permanece imutável dentro do escopo da chamada de nome_pessoa (função interna)
        """
        return '{} {}'.format(dic[idioma], nome)
    return nome_pessoa

saudacoes = diga_oi()

saudacoes('pirata', 'Eduardo') # 'Ahoy Eduardo'
saudacoes('portugues', 'Jaber') # 'Olá Jaber'
saudacoes('ingles', 'Python') # 'Hello Python'
```

## Classes e closures


Você deve ter percebido que até agora as closures tem dois tipos de comportamento diferentes, porém a imutabilidade permanece:

- fixando parâmetros para padronização de chamadas:

Aqui você deve ter sacado o esquema de operações com dados. O dado passado a função externa permanece imutável sempre e inacessível a qualquer contexto, ou seja, o dado foi fixado e não pode ser transformado em nenhum outro valor, a não ser que seja feita outra chamada com outro valor. O que deveria ser dito sobre as classes é o que toca exatamente nesse ponto, vamos fazer uma comparação:


### classe `__call__()``

```Python
class diga_oi:
    """
    Classe do tipo função
    """
    def __init__(self, saudacao):
        """
        Inicializa a instância do objeto com saudacao
        """
        self.saudacao = saudacao

    def __call__(self, nome):
        """
        __call__ permite que o objeto aplique o operado (),
            seja chamado como função
        """
        return '{} {}'.format(self.saudacao, nome)
```

Esse trecho de código tem o mesmo comportamento da nossa closure pois funciona como uma função, mas o efeito colateral existe:

```Python
saudacao = diga_oi('Ahoy')
saudacao('eduardo') # 'Ahoy eduardo'

saudacao.saudacao = 'Olá'

saudacao('eduardo') # 'Olá eduardo'
```

Todo atributo em python é mutável, até os métodos podem ser mudados usando monkey patch. Não quero me aprofundar em orientação a objetos pois não é o assunto do curso, mas vamos só modificar essa classe para que ela não gere o efeito colateral:

```Python
class diga_oi:
    """
    Classe do tipo função
    """
    def __init__(self, saudacao):
        """
        Inicializa a instancia do objeto com saudacao sendo imutavel
        """
        object.__setattr__(self, 'saudacao', saudacao)

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __call__(self, nome):
        """
        __call__ permite que o objeto aplique o operado (),
            seja chamado como função
        """
        return '{} {}'.format(self.saudacao, nome)
```

`__setattr__()` é o método da classe que 'seta' valores em atributos, se nós quebrarmos a implementação default do Python ele não vai conseguir fazer atribuições, porém, é muito mais complicado que implementar uma closure. Nessa implementação simples para a comparação as closures tem 4 linhas e as classe 7. Pra fazer a mesma coisa, acho muito mais atrativo usar uma closure, não só porque estamos falando de programação funcional, mas pela simplicidade de código mesmo('legibilidade conta'). Mas vamos prosseguir.

- Variáveis do escopo da função podem sim ser alterados como nas classes

Tá, prometo que essa parte vou tentar ser breve, mas existe um conceito que não poderia deixar passar aqui, as variáveis livres. Um adendo que deve ser feito é que isso vale para as funções anônimas também, não só no mundo das closures. Deixei pra falar disso agora para você não ficar viciado em lambdas.


## Variáveis livres
