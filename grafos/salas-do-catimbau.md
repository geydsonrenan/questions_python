Problem Statement

Juninho, audacioso historiador brasileiro, decidiu explorar novos mistérios pelo mundo em virtude dos seus gostos peculiares. Ao visitar o vale do catimbau à procura de novas estruturas antigas curiosas, ele encontra uma caverna que apresenta diversas portas numeradas e algumas chaves também numeradas dentro, com diversas ilustrações na parede apontando que na porta final haverá um grande tesouro. Juninho logo percebe que os números escritos nas chaves correspondem à porta que a determinada chave pode abrir. As chaves das portas só poderão ser recolhidas se as portas estiverem ou forem abertas. A primeira porta já se encontra aberta com algumas chaves dispostas nela. As portas poderão ser abertas fora de ordem caso Juninho tenha pego a chave, ou seja, com a chave 3 eu posso abrir a porta 3 sem abrir a porta 2. Sedento por cobiça, Juninho decide pedir a sua ajuda para saber se é ou não possível chegar no tesouro.

Input

O input será N linhas que possuem números dentro seguindo esse formato:

Input:

2 10 5

4 3

8 3

Tesouro

As N linhas representam as salas e os números representam uma chave com aquele número escrito.

A primeira linha representa a sala 1, a segunda a sala 2 e assim por diante.

A sala 1 já está aberta.

A sala final terá a string "Tesouro" e será a última da sequência.

Output

Terá apenas duas opções de output:

Será TESOURO :) se for possível chegar até a sala final

Será SEM TESOURO :( se NÃO for possível chegar até a sala final

Examples

Case: 1

Input

4 5
1
10 8
6
2
Tesouro

Output

TESOURO :)
