Problem Statement

Um funcionário de uma papelaria em uma pequena cidade no interior de Essuatíni tem um problema. Ao receber a mais nova remessa de páginas de um caderno inteligente chamado Manual de Como Sobreviver em um País Que Ninguém Conhece, ele percebeu que as pilhas estavam bagunçadas, em ordens aparentemente caóticas. Por ser um caderno diferente, customizado para as necessidades de cada cliente, isso não seria estranho, pois as partes dos cadernos são muitas vezes sobrepostas, com capítulos dentro de outros, numa formatação bastante única para cada edição.

Infelizmente, o responsável pelo carregamento do produto perdeu a mão em uma curva e algumas pilhas se misturaram, causando uma grande confusão, e por isso as pilhas não são confiáveis. Agora, é responsabilidade desse funcionário conferir cada um dos cadernos para ver se eles estão com as capas na ordem correta, e, se não, onde está a primeira capa errada.

As capas têm dois tipos: frentes e versos, que funcionam como separadores e não são diferentes de um capítulo para outro. A única regra é que toda frente precisa ter um verso depois dela, não necessariamente imediatamente após, mas eventualmente. Para isso, nenhum verso pode aparecer sem que uma frente tenha o antecedido em algum momento. Se ao fim da pilha alguma frente não tiver o seu verso, esse também é um indicativo de que o caderno foi comprometido.

Resumo do problema: Confira se todas as frentes (F) tem seus devidos versos (V) em uma ordem satisfatória. Toda frente precisa ter um verso depois dela, não necessariamente imediatamente após, mas eventualmente. Nenhum verso pode aparecer sem que uma frente tenha o antecedido em algum momento. E, atenção, uma pilha que tem a mesma quantidade de frentes e versos NÃO está necessariamente correta.

OBS: Strings vazias devem ser consideradas corretas.

Input

A única linha de entrada é composta por uma string, que corresponde a pilha de capas manuseada pelo funcionário. A string é uma sequência de letras sem espaços ou vírgulas então elas, como VFVFFFVVFVFV.

Output

Você deve produzir uma única linha de saída com a expressão “Correto.” caso a pilha seja bem formada, e “Incorreto, devido a capa na posição X.” caso contrário, onde X é a posição da primeira capa que interfere na integridade do caderno.

Examples

Case: 1

Input

FFFVVV

Output

Correto.
