# 0. Programação funcional com python

Programação funcional não é um bicho de sete cabeças. Dito isso, sente-se no sofá e vamos aproveitar essa introdução. Eu juro, não vai ser tão longa assim. Se você chegou até aqui, sinta-se um vencedor, você saiu da zona de conforto e está tentando aprender mais sobre o mundo pythonico.

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

## 0.1 Técnicas usadas por linguagens funcionais

- Funções como objetos de primeira classe
- Funções de ordem superior
- Funções puras
- Recursão, como oposição aos loops
- Foco em processamento de iteráveis
- Evitam efeitos colaterais
- O que deve ser computado, não como computar
- Lazy evaluation

## 0.2 Python é uma linguagem funcional?

#### Não. Mas é uma linguagem que implementa muitos paradigmas e porque não usar todos de uma vez?

O objetivo desse 'conjunto de vídeos' é escrever código que gere menos efeito colateral e código com menos estados. Só que isso tudo, feito na medida do possível. Pois Python não é uma linguagem funcional. Porém, podemos contar o máximo possível com as features presentes do paradigma em python.

## 0.3 A quem esse 'curso' é destinado?

Primeiramente gostaria de dizer que roubei essa ideia dos infinitos livros da O’Reilly, que sempre exibem esse tópico. Mas vamos ao assunto. Se você sabe o básico de Python, e quando digo básico quero dizer que consegue fazer qualquer coisa com um pouco de pesquisa na internet. O básico de programação de reduz a isso. Vamos falar sobre coisas simples e coisas mais complexas, mas pretendo manter o bom senso para que todos possam absorver o máximo de conteúdo possível.

Então, caso você venha do Pythom (OO ou procedural) você vai encontrar aqui uma introdução a programação funcional descontraída em sem uma tonelada de material difícil de entender. Caso você venha de linguagens funcionais como Haskell e Lisp. Você pode se sentir um pouco estranho com tantas declarações, mas você pode aprender a se expressar em Python. Caso você venha de linguagens funcionais modernas como Clojure e Scala, as coisas são bem parecidas por aqui.

Então, tente tirar o máximo de proveito, vamos nos divertir.

## 0.4 Apresentando o Jaber

Jaber é nosso aluno de mentira, mas vamos pensar que ele é um aluno que senta na primeira fileira e pergunta de tudo, sempre que acha necessário. Roubei essa ideia do livro de expressões regulares do Aurélio. Ele tem um personagem, Piazinho, e acho que toda interação com ele é sempre graciosa e tira dúvidas quando tudo parece impossível.

## 0.5 Sobre as referências

Não gosto muito de citar referências pois procurei não copiar texto dos livros, mas muita coisa contida nele serve de base para o entendimento de certos tópicos. Procurei não citar referências por muitos motivos e um deles é o nível de complexidade dos exemplos ou explicações que tentei reduzir ao máximo enquanto escrevia esses roteiros. Para um exemplo, você pode olhar o livro do Steven Lott, cheio de formulas e abstrações matematicas que em certo ponto acabam comprometendo o intendimento de quem não tem uma sólida base em computação teórica ou matemática.

Como um todo, as referências serviram como guia, foi o que lí quando dúvidas para explicações surgiram. Não tiro nenhum credito delas e as exponho para que todos saibam que existem muitos livros bons e que boa parte do é passado aqui, foi aprendido neles.


## 0.6 Sobre o histórico das linguagens funcionais

Se você pretende realmente se aprofundar no assunto enquanto acompanha esse curso, fazer uma imersão ou coisa parecida. Tudo começa com o calculo lambda mentalizado pelo incrível [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church). Caso você não o conheça, ele foi um matemático fantástico e teve uma carreira acadêmica brilhante. Foi o orientador de pessoas incríveis como Alan Turing, Raymond Smullyan etc...

Outro grande homem e que vale a pena mencionar e ser buscado é o [Haskell Curry](https://pt.wikipedia.org/wiki/Haskell_Curry), um lógico que trouxe exelentes contribuições para o que chamamos hoje de programação funcional.

A linguagem funcional 'oficial', não gosto muito de dizer isso. A primeira linguagem funcional é o Lisp (List Processing) criada pelo fenomenal [John McCarthy](https://pt.wikipedia.org/wiki/John_McCarthy) que também vale a pena ser pesquisado e estudado.

Bom, acho que está bom por agora. Vamos ver um pouco sobre os tipos de função no tópico 1.
