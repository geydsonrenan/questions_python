Problem Statement

Dado uma rede social com N usuários, quando um usuário faz uma publicação, a mensagem alcança seus seguidores imediatos e, em seguida, os seguidores dos seus seguidores, ou seja, o alcance na rede é medido em largura. Para calcular quantos seguidores essa publicação pode alcançar, é necessário pagar um "boost" para chegar aos seguidores dos seguidores.

Por exemplo, se um usuário tem 3 seguidores e cada um deles tem 2 seguidores, a publicação chegará aos seus 3 seguidores diretos gratuitamente, mas para chegar aos seguidores dos seguidores será necessário pagar um "boost". O custo do "boost" é calculado por uma função que multiplica a quantidade de seguidores que deseja alcançar por R$5,25.

Se o usuário deseja alcançar mais 3 usuários fora do seu nível de seguidores, ele precisará pagar por 3 x R$5,25 = R$15,75 para que a publicação alcance esses seguidores. Caso o usuário tenha apenas R$15,00 para investir, a publicação alcançará apenas os seguidores imediatos dos seus seguidores.

O exemplo de cima de forma ilustrada:

alaaa

OBS: É proibido utilizar qualquer biblioteca.

Input

N - Onde N é o número de usuários na rede social

U - Onde U é o id do user

B - Onde B é o valor investido em boost

Em seguida: Várias linhas com a representação da relação de seguidores dos usuários da rede social:

ID s[] - ID do usuário + ID dos seguidores

Output

[Usuários atingidos] - Lista com o ID dos seguidores alcançados

Examples

Case: 1

Input

17
0
16
0 : 6 8 4
1 : 5 4 14 9 0 3 2
2 : 6 5 4 12 14 1 11 8
3 : 1 14 16 9 3 15
4 : 3 6 16
5 : 14 8 5
6 : 15 13 4 0
7 : 5 4 16 13 2
8 : 5 14 1 10 0 3 11 7
9 : 4 12 1 10 0 3 11 8 2 7
10 : 4 12 1 3 8 7
11 : 5 14 1 0 3 8
12 : 9 2 7
13 : 5 4 12 14 1 10 16 0 15 11
14 : 4 13 9 3 15 8 7
15 : 6 5 14 1 9 0 3 7
16 : 5 4 1 16 13 3 7

Output

['6', '8', '4', '15', '13', '5']
