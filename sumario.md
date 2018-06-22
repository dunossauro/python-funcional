## 0 [Saindo da zona de conforto](roteiros/00_introducao.md)
### 0.1 Mas de onde vem a programação funcional?
### 0.2 Técnicas usadas por linguagens funcionais
### 0.3 Python é uma linguagem funcional?
### 0.4 A quem esse 'curso' é destinado?
### 0.5 Apresentando o Jaber
### 0.6 Sobre as referências
### 0.7 Mais sobre o histórico das linguagens funcionais
## 1 [Funções](roteiros/01_funcoes.md)
### 1.1 Funções como objeto de primeira classe
### 1.2 Funções puras
### 1.3 Funções de ordem superior (HOFs)
#### 1.3.1 Um exemplo usando funções embutidas
### 1.4 `__call__`
### 1.5 Funções geradoras
### 1.6 Funções anônimas (lambda)
## 2 [Iteráveis e iteradores](roteiros/02_iteraveis_iteradores.md)
### 2.1 `__getitem__`
### 2.2 `__iter__`
## 3 [Consumindo iteráveis](roteiros/03_consumindo_iteraveis.md)
## 4 [Funções de redução/mapeamento](roteiros/04_funcoes_reducao_mapeamento.md)
### 4.1 Funções de redução
#### 4.1.1 `any()`
#### 4.1.2 `all()`
#### 4.1.3 `len()`
#### 4.1.4 sum()
### 4.2 Funções de mapeamento
#### 4.2.1 `zip()` e `reversed()`
#### 4.2.2 `enumerate()`
#### 4.2.3 `map()`
## 5 [Funções de ordem superior](roteiros/05_hofs.md)
### 5.1 `map()`
### 5.2 `max()`
### 5.3 `min()`
### 5.4 `iter()`
### 5.5 `sorted()`
### 5.7 `filter()`
## 6 [Funções de ordem superior Parte 2](roteiros/06_funcoes_geradoras_e_hofs_p2.md)
### 6.1 Funções que aceitam funções
### 6.2 Funções geradoras
### 6.3 Escrevendo nossas próprias HOFs
## 7 [Nossa primeira biblioteca de funções](roteiros/07_construindo_nossa_lib.md)
### 7.1 `tail()`
### 7.2 `head()`
### 7.3 `take()`
### 7.4 `drop()`
### 7.5 `pipe()`
### 7.6 `twice()`
### Conclusões
## 8 [Closures e contexto de variáveis](roteiros/08_closures_1_escopo.md)
### 8.1 Classes vs closures
### 8.2 Mutação das variáveis de uma closure
## 9 [Usos variados de closures](roteiros/09_closures_2.md)
### 9.1 Closures e lambdas
### 9.2 Métodos em closures
### 9.3 Interagindo com valores `nonlocal`
### 9.4 Closures que recebem funções (ou quase isso)
### 9.5 Decorar funções com closures
## 10 [Decoradores](roteiros/10_decoradores.md)
### 10.1 Qual a cara de um decorador?
### 10.2 Montando nosso primeiro decorador
### 10.3 Decoradores com parâmetros (closures de closures)
### 10.4 Identidade das funções decoradas
### 10.5 Decorando decoradores
