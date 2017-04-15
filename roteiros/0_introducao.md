# 0. Saindo da zona de conforto

Sinta-se um vencedor, se você chegou até aqui, isso significa que quer aprender mais sobre o mundo da programação.

Aprender novos paradigmas podem te trazer muitas coisas positivas, assim como aprender linguagens diferentes, pois paradigmas e linguagens transpõem maneiras, estruturas e métodos de implementação completamente diferentes. Com isso você pode ter mais ferramentas para usar no dia a dia. Você pode aumentar sua capacidade de expressar ideias de diferentes maneiras. Eu penso que o maior limitador de um programador é a linguagem de programação em que ele tem domínimo. Quando você aprende linguagens imperativas, como C, Python, Java e etc... você se vê limitado ao escopo de criar e manipular variáveis. Não que isso seja uma coisa ruim, porém existem outras maneiras de resolver problemas e quando você tem conhecimento disso consegue avaliar quando implementar cada tipo de coisa.

Você pode me dizer que aprender diferentes tipos estruturas e maneiras de computar é uma coisa negativa pois tudo é variável nesse contexto. Mas eu penso exatamente o contrário, quanto mais você aprender da sua lingua nativa, no caso estamos falando em português, maior campo de domínio você tem sobre como se comunicar e expressar ideias. Assim como aprender outras linguas te darão mais fundamentos para expressar ideias em outros idiomas que noa são melhores que os seu, eles são diferentes e compõe estruturas diferentes e isso pode ser libertador. Não quero me expandir muito nesse assunto, mas dizer que isso pode acrecentar muito na suas habilidades conginitivas, até mesmo para usar ferramentas que você já usa no seu dia a dia.


Vamos começar fazendo uma tentativa de entender os paradigmas de programação, sem muito falatório e complicações. um exemplo muito legal é do David Mertz  em Functional Programming in Python é:

-   Usa-se programação funcional quando se programa em Lisp, Haskell, Scala, Erlang, F# etc..

-   Do mesmo modo que se usa programação imperativa quando se programada C/C++, Pascal, Java, Python etc...

-   Também quando de se programa Prolog estamos programando usando o paradigma lógico


Apesar de não ser uma definição muito elegante, talvez seja a melhor a ser dada em muitas ocasiões. Vamos tentar ser um pouco mais objetivos, em relação ao estilo de computação, embora essa discussão não tenha fim.

-   O foco de usar programação imperativa está no ato de mudar variáveis. A computação se dá pela modificação dos estados das variáveis iniciais. Sendo assim, vamos pensar que tudo é definido no início e vai se modificando até que o resultado esperado seja obtido

-   Na programação funcional, se tem a noção de que o estado deve ser substituído, no caso da avaliação, para criação de um novo 'objeto' que no caso são funções


## 0.1 Mas de onde vem a programação funcional?

O florecer da programação funcional nasce no Lisp (acronomo para List Processing) para tentar resolver alguns problemas de inteligência artificial que eram provenientes da linguistica que tinha foco em processamento de linguagem natural que por sua vez eram focados em processamento de listas em geral, isso justifica uma grande parte do conteúdo que vamos ver aqui e seus tipos de dados variam somente entre listas e átomos. E assim foi mantido o foco de processamento de listas em todas as linguagens funcionais e suas funções e abstrações para resolver problemas relativos as listas e estrutras iteráveis. Uma curiosidade é que para quem não sabe porque em lisp existem tantos parêntese é que ele é baseado em s-expression, uma coisa que temos um "equivalente" evoluido em python, que parte dos teoremas de gramaticas livres de contexto:

```clojure
(+ 4 5)
```

Sim, isso é uma soma em lisp. Diferente das linguagens imperativas como costumamos ver:

```c
4 + 5
```

Uma assertiva pode ser feita dessa maneira:

-   Funcional (ou declarativa)
```clojure
(= 4 (+ 2 2))
```

-   Imperativa
```c
(2 + 2) == 4
```

Chega de enrolação e vamos correr com essa introdução, não viemos aqui para aprender Lisp ou C. Mas acho que parte desse contexto pode nos ajudar e muito quando formos nos aprofundar em alguns tópicos. Pretendo sempre que iniciar uma nova ferramenta da programação funcional ao menos explicar em que contexto ela foi desenvolvida e para resolver cada tipo de problema.

## 0.2 Técnicas usadas por linguagens funcionais

Vamos tentar mapear o que as linguagens funcionais fazem de diferente das linguagens imperativas, mas não vamos nos aprofundar nesse tópicos agora, pois são coisas as vezes complexas sem o entedimento prévio de outros contextos, mas vamos tentar só explanar pra que você se sinta empolgado por estar aqui:

-   Funções como objetos de primeira classe
    -   São funções que podem estar em qualquer lugar (em estruras, decladas em tempo de execução)
-   Funções de ordem superior
    -   São funções que podem receber funções como argumentos e retornar funções
-   Funções puras
    -   São funções que não sofrem interferências de meios externos (variáveis de fora). Evitar efeitos colaterais
-   Recursão, como oposição aos loops
    -   Frequentemente a recursão na matemática é uma coisa mais intuítiva é só chamar tudo outra vez, no lugar de ficar voltando ao ponto inicial da iteração
-   Foco em processamento de iteráveis
    -   Como dito anteriormente, pensar em como as sequências podem nos ajudar a resolver problemas
-   O que deve ser computado, não como computar
    -   Não ser tão expressivo e aceitar que as intruções não tem necessidade de estar explicitas todas as vezes, isso ajuda em legibilidade
-   Lazy evaluation
    -   Criar sequencias infinitas sem estourar nossa memória.

## 0.3 Python é uma linguagem funcional?

#### Não. Mas é uma linguagem que implementa muitos paradigmas e porque não usar todos de uma vez?

O objetivo desse 'conjunto de vídeos' é escrever código que gere menos efeito colateral e código com menos estados. Só que isso tudo, feito na medida do possível. Pois Python não é uma linguagem funcional. Porém, podemos contar o máximo possível com as features presentes do paradigma em python.

Exemplos de funcional (básicos) em python:

```Python
# Gerar uma lista da string # Imperativo
string = 'Python'
lista = [] # estado inicial

for l in string:
    lista.append(l) # cada iteração gera um novo estado

print(lista) # ['P', 'y', 't', 'h', 'o', 'n']
```

```Python
# Gerar uma lista da string # Funcional
string = lambda x: x('Python')

lista = list(map(str, string)) # atribuição ao um novo objeto

print(lista) # ['P', 'y', 't', 'h', 'o', 'n']
```

Como você pode ver, depois de uma explanação básica das técnicas, a segunda implementação não sofre interferência do meio externo(Funções puras), evita loops e sua saída sem o contrutor de list é lazy. Mas não se assuste, vamos abordar tudo isso com calma.

## 0.4 A quem esse 'curso' é destinado?

Primeiramente gostaria de dizer que roubei essa ideia dos infinitos livros da O’Reilly, que sempre exibem esse tópico. Mas vamos ao assunto. Se você sabe o básico de Python, e quando digo básico quero dizer que consegue fazer qualquer coisa com um pouco de pesquisa na internet. O básico de programação de reduz a isso. Vamos falar sobre coisas simples e coisas mais complexas, mas pretendo manter o bom senso para que todos possam absorver o máximo de conteúdo possível.

Então, caso você venha do Pythom (OO ou procedural) você vai encontrar aqui uma introdução a programação funcional descontraída em sem uma tonelada de material difícil de entender. Caso você venha de linguagens funcionais como Haskell e Lisp. Você pode se sentir um pouco estranho com tantas declarações, mas você pode aprender a se expressar em Python. Caso você venha de linguagens funcionais modernas como Clojure e Scala, as coisas são bem parecidas por aqui.

Então, tente tirar o máximo de proveito, vamos nos divertir.

## 0.5 Apresentando o Jaber

Jaber é nosso aluno de mentira, mas vamos pensar que ele é um aluno que senta na primeira fileira e pergunta de tudo, sempre que acha necessário. Roubei essa ideia do livro de expressões regulares do Aurélio. Ele tem um personagem, Piazinho, e acho que toda interação com ele é sempre graciosa e tira dúvidas quando tudo parece impossível.

## 0.6 Sobre as referências

Não gosto muito de citar referências pois procurei não copiar texto dos livros, mas muita coisa contida nele serve de base para o entendimento de certos tópicos. Procurei não citar referências por muitos motivos e um deles é o nível de complexidade dos exemplos ou explicações que tentei reduzir ao máximo enquanto escrevia esses roteiros. Para um exemplo, você pode olhar o livro do Steven Lott, cheio de formulas e abstrações matematicas que em certo ponto acabam comprometendo o intendimento de quem não tem uma sólida base em computação teórica ou matemática.

Como um todo, as referências serviram como guia, foi o que lí quando dúvidas para explicações surgiram. Não tiro nenhum credito delas e as exponho para que todos saibam que existem muitos livros bons e que boa parte do é passado aqui, foi aprendido neles.


## 0.7 Mais sobre o histórico das linguagens funcionais

Se você pretende realmente se aprofundar no assunto enquanto acompanha esse curso, fazer uma imersão ou coisa parecida. Tudo começa com o calculo lambda mentalizado pelo incrível [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church). Caso você não o conheça, ele foi um matemático fantástico e teve uma carreira acadêmica brilhante. Foi o orientador de pessoas incríveis como Alan Turing, Raymond Smullyan etc...

Outro grande homem e que vale a pena mencionar e ser buscado é o [Haskell Curry](https://pt.wikipedia.org/wiki/Haskell_Curry), um lógico que trouxe exelentes contribuições para o que chamamos hoje de programação funcional.

A linguagem funcional 'oficial', não gosto muito de dizer isso. A primeira linguagem funcional é o Lisp (List Processing) criada pelo fenomenal [John McCarthy](https://pt.wikipedia.org/wiki/John_McCarthy) que também vale a pena ser pesquisado e estudado.

Bom, acho que está bom por agora. Vamos ver um pouco sobre os tipos de função, ou o básico disso, no tópico 1.
