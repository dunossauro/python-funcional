## Funções de ordem superior

Você deve acha que esquecemos muitas funções embutidas no vídeo passado, não? funções como

- map()
- max()
- min()
- iter()
- sorted()
- filter()

Porém, essas funções têm características especiais. Como assim? Elas podem receber além do iterável, uma outra função como argumento. Vamos lá. Você já foi introduzido ao map no vídeo passado

### map()

A função `map()`, fazendo um gancho com o vídeo anterior, é uma função de mapeamento, contudo, ela recebe o iterável em conjunto a uma função, a que fará o mapeamento. Vamos lá:

```Python
def func(x):
    """
    exemplo do vídeo passado
    """
    return x +2

list(map(func, [1,2,3])) # [3, 4, 5]
```

A função que chamamos de `func()` é uma função extremamente simples, retorna a entrada somada com 2, simples assim. Um ponto que vale a pena ser tocado é que as funções usadas por map só podem receber um argumento. Por que? A função map vai pegar um elemento da sequência e aplicar a função. Só isso seŕio.

Agora vamos complicar as coisas um pouco mais....

```Python
# Uma lista de listas, isso em python também é um matriz
lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]

def func(x):
    """
    Retorna a mesma coisa que entrou
    """
    return x

list(map(func, lista))
```

Você concorda comigo que a entrada não é exatamente um elemento único, mas uma sequência?

Então, como temos uma lista agora, podemos fazer coisas de lista? aplicar outras funções de iteráveis? Vamos lá:

```Python
# Uma lista de listas, isso em python também é um matriz
lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]

def func_rev(x):
    """
    Retorna a lista que entrou, porém invertida
    """
    return list(reversed(x))

list(map(func_rev, lista)) # [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]]
```

Isso, isso, isso. Olha como a coisa está ficando linda? O que fizemos agora é uma composição de funções, mas dentro de um map. A notação matemática disso, caso você tenha curiosidade em saber é:

```
uma função comum = f(x)

composição de funções = f(g(x))
```
 Bom, agora você aprendeu o poder do `map()`, podemos viajar entre a outra gama de funções de ordem superior que o python oferece. Porém, fica o adendo teórico:


 ```
Funções de ordem superior são funções que recebem, como argumento, ou retornam outra funções
 ```

Viu, foi simples.

### max()

A função max é uma função de redução, e sem a função como parâmetro, ela vai ter o comportamento das funções que vimos no outro vídeo.

```Python

max([1, 2, 3, 4, 5]) # 5
```

Só que... (e .... lá vem)


Se ela lista for uma lista de listas, como prosseguir?


```Python
lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]

max(lista) # [5, 6]
```

É, ainda está funcionando.

```Python
lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

max(lista) # [7, 2]
```

`[7, 2]` é um bom resultado, mas vamos pensar que o que eu queria eram as somas dois dois elementos, nesse caso o resultado veio errado. `7 + 2 = 9` quando `5 + 6 = 11`. Vamos tentar outra vez.


```Python
lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

def func(x):
    return x[0] + x[1]

max(lista, key=func) # [5,6]
```

Viu, esse argumento `key` pode ser uma mão na roda em muitos dias tristes em que você está sem vontade de cantar uma bela canção.

```Python
lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

max(lista, key=sum) # [5, 6]
```

Como você já sabe compor funções, e vamos imaginar que nossa sequência de entrada poderia ser maior que dois elementos, uma maneira bonita de fazer isso seria usar o `sum()`. Fica muito mais elegante.


### min()

Agora que já entendemos o conceito das HOFs, tudo fica mais simples. A função `min()` é a função equivalente a `max()`. Quando a max pega o maior item da sequência, mim pega o menor.

```Python
lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

min(lista, key=sum) # [5, 3]
```

Não temos muito mais o que falar sobre min, é só um complemento

### iter()


A função embutida `iter()` tem duas formas, a primeira devolve o iterável de uma sequência.


```Python
lista = [1, 2, 3, 4, 5]

iter(lista) # <list_iterator at xpto>
```

Ele faz a chamada do método `__iter__()` do objeto. Até então nenhuma novidade. Vamos supor que isso seja um facilitador para transformar nossos objetos em sequências imutáveis e preguiçosas.

Porém, a segunda forma é bem interessante.


```Python
"""
Exemplo roubado do Steven Lott
"""
lista = [1, 2, 3, 4, 5]

list(iter(lista.pop, 3)) #[5, 4]
```

Vamos por partes que agora vem muita informação pra pouca linha de código.

vamos dar um `help()` em iter:

```python
help(iter)

iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
```

Então, quer dizer que o callable é chamado até que o retorno seja o sentinela. Como passamos como callable `pop` e se pop for chamado sem argumentos, ele retorna o último elemento da lista e retira ele da mesma. Nesse caso o sentinela é 3. Então ele vai desmontando a lista e gerando um novo iterável de tudo que foi removido da lista anterior.

Ou seja, vamos fazer um mapinha básico:

(1) lista = [1, 2, 3, 4, 5]
(2) saida = []
(3) saida.append(lista.pop())
(4) print(saida) # [5]

Agora que o pop_append ficou claro. Deu pra entender o que faz a segunda forma da função `iter()`? Sim, deu.


Então vamos explorar um exemplo mais eficiente, o da documentação:

```Python
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line) # só essa linha foi modificada
```

o método readline, quando passado sem parâmetros efetua a leitura de um único caracter. Nesse caso ele printaria uma letra do arquivo por linha. Mas, como usamos `iter(fp.readline, '')` ele vai nos retornar uma sequência de strings até que o sentinela no caso é vazio apareça.


### sorted()


### filter()
