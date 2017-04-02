
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

## 9.3 closures que recebem funções (ou quase isso)

Esse, embora seja um exemplo óbivo do que vimos até agora, pode ser que não tenha passado na cabeça de ninguém até agora, mas vamos lá:

```Python
def diga_oi(saudacao, func):
    """
    Função diga_oi, nossa velha de gerra com um lambda interno
    """
    return func

ahoy = diga_oi('Ahoy', lambda nome: '{} {}'.format(saudacao, nome))
ahoy('Jaber') # NameError: name 'saudacao' is not defined
```

Jaber diz: `Mas isso faz todo sentido de funcioar, por que não funciona????`

Lembra de todo aquele caso do escopo das variáveis? `saudacao` está definida dentro de `diga_oi()` e isso faz com que ela não exista fora desse contexto que é onde a função `lambda` está sendo definida. Então para esse casos passar funções como argumento que usam valores `nonlocal` não funcionam. Passar funções como argumento que não compartilham atributos é como fazer uma método estático em classes, não serve de muita coisa, só agrega funções em um mesmo lugar.

## 9.4 ler parcialmente variáveis `nonlocal`


## 9.5 decorar funções com closures
