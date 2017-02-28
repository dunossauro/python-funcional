### Programação funcional

- Definição do paradigma (Mertz)
    - usa-se programação funcional quando se programa em Lisp, Haskell, Scala, Erlang, F# etc..
    - Do mesmo modo que se usa programação imperativa quando se programada C/C++, Pascal, Java, Python etc...
    - Também quando de se programa Prolog estamos programando usando o paradigma lógico

    - O foco de usar programação imperativa está no ato de mudar variáveis, a computação de dá pela modificação das variáveis iniciais, até o que resultado seja computado, com a modificação da variável, até que a saída seja a pretendida (Baseado em estados (armazenamento))

    - Na programação funcional, se tem a noção de que o estado deve ser substituído, no caso da avaliação, para criação de um novo 'objeto' que no caso são funções

    - Exemplos:

```Python
# Gerar uma lista da string #imperativo
string = 'Python'
lista = [] # estado inicial

for l in string:
    lista.append(l) # cada iteração gera um novo estado

print(lista) # ['P', 'y', 't', 'h', 'o', 'n']
```

```Python
# Gerar uma lista da string # Funcional
string = lambda x: x

lista = list(map(str, string('Python'))) # atribuição ao um novo objeto

print(lista) # ['P', 'y', 't', 'h', 'o', 'n']
```

- Vamos pensar em não usar definições complexas, ao menos quando elas forem necessárias (Matemática ... functors, monads, f(g(x)))

## Técnicas usadas por linguagens funcionais

- Funções como objetos de primeira classe
- Funções de ordem superior
- Funções puras
- Recursão, como oposição aos loops
- Foco em processamento de iteráveis
- Evitam efeitos colaterais
- O que deve ser computado, não como computar
- Lazy evaluation

## Python é uma linguagem funcional?

#### Não. Mas é uma linguagem que implementa muitos paradigmas e porque não usar todos de uma vez?

O objetivo desses videos são escrever código que gere menos efeito colateral, código com menos estados. Só que isso tudo, e feito na medida do possível. Pois Python não é uma linguagem funcional. Porém, podemos contar o máximo possível com as fetures presentes do paradigma em python
