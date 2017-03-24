# Programação funcional com python

Programação funcional não é um bicho de sete cabeças. Dito isso, sente-se no sofá e vamos aproveitar essa introdução. Eu juro, não vai ser tão longa assim.

Vamos começar fazendo uma tentativa de entender os paradigmas de programação. um exemplo muito legal é do David Mertz (Functional Programming in Python):

- Usa-se programação funcional quando se programa em Lisp, Haskell, Scala, Erlang, F# etc..

- Do mesmo modo que se usa programação imperativa quando se programada C/C++, Pascal, Java, Python etc...

- Também quando de se programa Prolog estamos programando usando o paradigma lógico

Apesar de não ser uma definição muito elegante, talvez seja a melhor a ser dada em muitas ocasiões. Vamos tentar ser um pouco mais objetivos, em relação ao estilo de computação, embora essa discussão não tenha fim.

- O foco de usar programação imperativa está no ato de mudar variáveis. A computação se dá pela modificação dos estados das variáveis iniciais. Sendo assim, vamos pensar que tudo é definido no início e vai se modificando até que o resultado esperado seja obtido

- Na programação funcional, se tem a noção de que o estado deve ser substituído, no caso da avaliação, para criação de um novo 'objeto' que no caso são funções

Exemplos em python:

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

O objetivo desse 'conjunto de vídeos' é escrever código que gere menos efeito colateral e código com menos estados. Só que isso tudo, feito na medida do possível. Pois Python não é uma linguagem funcional. Porém, podemos contar o máximo possível com as features presentes do paradigma em python.
