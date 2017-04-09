
# 9. Usos variados de closures

Vamos entender um pouco mais sobre closures e variar o uso com diversas coisas? Vamos tentar trazer alguns exemplos mais práticos do uso de closures. Mas vamos ver alguns modos diferentes dos vistos antes agora.

## 9.1 closures e lambdas

Todas as closures que criamos até agora podem ser substituidas por lambdas, pois as funções internas não passam de simples expressões:

```Python
def diga_oi(saudacao):
    """
    Função diga_oi, nossa velha de gerra com um lambda interno
    """
    return lambda nome: '{} {}'.format(saudacao, nome)

ahoy = diga_oi('Ahoy')
ahoy('Jaber') # 'Ahoy Jaber'
```

Uma coisa legal de usar funções `lambda`, e ao mesmo tempo um ponto negativo desse tipo de utilização, é que não há uma maneira de sobreescrever a variável local usando `nonlocal` pois o lambda só aceita uma expressão de uma linha. Para closures como essa em que o valor deve ser só lido isso pode funcionar bem.

## 9.2 métodos em closures

Sim, agora estamos falando de Python e as coisas em que mundo Pythonico nos oferece:

```Python
def diga_oi(saudacao):
    """
    Função diga_oi, nossa velha de gerra com um lambda interno
    """
    def mudar_saudacao(nova_saudacao):
        nonlocal saudacao
        saudacao = nova_saudacao

    diga_oi.mudar_saudacao = mudar_saudacao
    return lambda nome: '{} {}'.format(saudacao, nome)

ahoy = diga_oi('Ahoy')
ahoy('Jaber') # 'Ahoy Jaber'
ahoy.mudar_saudacao('Olá')
ahoy('Jaber') # 'Olá Jaber'
```

Em tempo de execução é possível fazer monkey patch em qualquer tipo de objeto em python e isso permite que `n` funções possam caber dentro de uma closure e como tudo pode ser modificado, foi criado um método interno. Manipular closures dessa maneira é mais eficiente do que usar classes, mas não vamos falar sobre isso agora. O podemos absorver disso é que sem classes ninguém vai começar a pirar, pelo menos em Python não.

## 9.3 interagindo com valores `nonlocal`

Nós já fizemos isso com coposições de funções, mas como as closures são exatamente o inverso as composições, vamos fazer aqui também. Caso você tenha perdido o momento em que parcialmente consumimos iteráveis, isso foi feito no tópico 7.

Vamos imaginar que nossa closure contém um iterável infinito, ele armazena uma contágem, vamos usar nosso mesmo contador Fail do tópico 8:

```Python
def contador(inicio):
    var = inicio
    def retorno():
        nonlocal var # implementação de nonlocal
        var += 1
        return var
    return retorno

c = contador(0)
c() # 1
c() # 2
c() # 3
c() # 4
c() # 5
```

Já fizemos isso, mas vamos tentar incrementar a closure para que ela possa ser consumida lentamente, ou preguiçosamente, e que o retorno possa ser um range de valores que acrecentam a contagem de formas diferentes:

```Python
def contador(inicio, continuo=False):
    """
    inicia nossa closure

    Args:
        - inicio: Define qual o valor de incio da contagem
        - continuo: Define se os valores serãm continuados ou não
    """
    var = inicio
    def retorno(quantidade):
        """
        Retorna uma quantidade x de valores contínuos apartir do último usado

        Caso seja continua, e aquantidade for (> 1) o retorno vai variar e armazenar o ultimo valor do range,
        Caso contrario, retornará um range, mas não alterará o valor inicial
        """
        nonlocal var # implementação de nonlocal
        yield from range(var, var + quantidade) # aqui fica a escolha de retornar um gerador

        if not continuo:
            var += 1
        else:
            var += quantidade
    return retorno
```

Isso faz com que o comportamento da closure seja diferente e temos duas maneiras de utilizar a o reu retorno, mas vale lembrar que ele é sempre lazy e a resposta trá de ser contruída ou iterada:

Modo 1:
```Python
c = contador(0)
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
# Independente de quantas vezes for chamado, a computação só será feita na construção do objeto
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
list(c(2)) # [0, 1]
list(c(2)) # [1, 2]
list(c(2)) # [2, 3]
```

Modo 2:
```Python
c = contador(0, True)
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
# Independente de quantas vezes for chamado, a computação só será feita na construção do objeto
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
c(2) # <generator object contador.<locals>.retorno at 0x0000000>
list(c(2)) # [0, 1]
list(c(2)) # [2, 3]
list(c(2)) # [4, 5]
list(c(2)) # [6, 7]
```

Como você pode ter notado, uma definição na função externa pode sim alterar todo o comportamento da função interna e o uso de nonlocal de fez suficiente para uma única variável, não sendo necessário o uso para as duas.

Jaber diz: `Mas eu poderia criar um método para gerenciar aquele boolean em tempo de execução?`

Sim e isso torna tudo mais lindo, mas eu vou deixar você tentar fazer isso sozinho.

## 9.4 closures que recebem funções (ou quase isso)

Esse, embora seja um exemplo óbivo do que vimos até agora, pode ser que não tenha passado na cabeça de ninguém até agora, mas vamos lá:

```Python
def diga_oi(saudacao, func):
    """
    Função diga_oi, nossa velha de gera com um lambda interno
    """
    return func

ahoy = diga_oi('Ahoy', lambda nome: '{} {}'.format(saudacao, nome))
ahoy('Jaber') # NameError: name 'saudacao' is not defined
```

Jaber diz: `Mas isso faz todo sentido de funcionar, por que não funciona????`

Lembra de todo aquele caso do escopo das variáveis? `saudacao` está definida dentro de `diga_oi()` e isso faz com que ela não exista fora desse contexto que é onde a função `lambda` está sendo definida. Então para esse casos passar funções como argumento que usam valores `nonlocal` não funcionam. Passar funções como argumento que não compartilham atributos é como fazer uma método estático em classes, não serve de muita coisa, só agrega funções em um mesmo lugar.

Vamos entender melhor esse tipo de atribuição ao falar dos decoradores, onde vamos decorar funções. Isso é só um problema de escopo de que precisava ficar nítido agora, nós vamos entender ele agora.

## 9.5 decorar funções com closures
