Problem Statement

Chegada a segunda-feira, cinco estagiários da biblioteca imaginária do CIn foram encarregados de ordenar os novos livros disponibilizados pela reitoria do campus para decorar as prateleiras da instituição com infinito conhecimento.

Sendo cada um deles uma entidade incorpórea, uma inteligência artificial, um figmento de insônia, eles resolvem criar uma competição que analisa qual o método mais eficiente para ordenar cada pilha, através de algoritmos diferentes que foram estudados na matéria IF969.

O primeiro estagiário, Caça-Rato, irá executar o método Bubble Sort.
O segundo estagiário, Grafite, irá executar o método Selection Sort.
O terceiro estagiário, Lacraia, irá executar o método Insertion Sort.
O quarto estagiário, Rivaldo, irá executar o método Shell Sort.
O quinto estagiário, Toninho, irá executar o método Quicksort (Hoare partition).
Para cada rodada da competição, os estagiários devem ordenar a mesma pilha de livros com o método delegado a eles, contando a quantidade de vezes que eles fazem uma comparação entre dois livros e a quantidade de vezes que eles trocam a posição de dois livros. Ao final da rodada, é definido o vencedor da rodada de acordo com a quantidade total de ações realizadas (comparações + trocas) para ordenar a pilha.

Após isso, os estagiários mais lentos tentam novamente ordenar a pilha, mas executando apenas a quantidade de ações que foram necessárias para o vencedor concluir a tarefa. Toninho, no entanto, não estava muito disposto a participar dessa etapa, então decidiu ficar de fora.

DESAFIO EXTRA: Injete ânimo no estagiário Toninho e faça com que ele participe da segunda etapa da competição.

Input

Para facilitar minha vida, os livros serão representados por números inteiros.

O código terá apenas uma linha de input, uma string de números únicos (sem repetições) separados por um espaço.

Exemplo: 4 5 8 7 14 2 3 6 21 32 52 0 2156 23

Output

Na primeira etapa, deve ser retornado o resultado da ordenação da seguinte maneira para cada um dos estagiários:

<nomeEstagiário> ordena a lista com <númeroComp> comparações e <númeroTrocas> trocas.

Após os cinco estagiários realizarem suas tarefas, devem ser retornado o nome do vencedor:

"-VENCEDOR DA RODADA-"

O vencedor da rodada é <nomeEstagiário>, com <númeroAções> ações.

Para a segunda etapa, lembre-se que Toninho não irá participar, então:

Os outros estagiários retornam as seguintes listas com essa quantidade de ações:

-Toninho está a dormir...-

Com <númeroAções> ações <nomeEstagiário> ordena a lista assim: <listaInterrompida> para cada um dos outros 4 estagiários (menos o vencedor, caso ele esteja entre os quatro).

Examples

Case: 1

Input

863 399 632 305 599 943 244 859 893 564

Output

Caça-Rato ordena a lista com 45 comparações e 22 trocas.
Grafite ordena a lista com 45 comparações e 6 trocas.
Lacraia ordena a lista com 28 comparações e 22 trocas.
Rivaldo ordena a lista com 32 comparações e 16 trocas.
Toninho ordena a lista com 27 comparações e 17 trocas.
-VENCEDOR DA RODADA-
O vencedor da rodada é Toninho, com 44 ações.
-Toninho está a dormir...-
Os outros estagiários retornam as seguintes listas com essa quantidade de ações:
Com 44 ações, Caça-Rato ordena a lista assim: [305, 399, 244, 599, 632, 859, 564, 863, 893, 943]
Com 44 ações, Grafite ordena a lista assim: [244, 305, 399, 564, 599, 632, 863, 859, 893, 943]
Com 44 ações, Lacraia ordena a lista assim: [244, 305, 399, 599, 632, 859, 863, 863, 893, 943]
Com 44 ações, Rivaldo ordena a lista assim: [244, 305, 399, 564, 599, 632, 863, 859, 893, 943]
