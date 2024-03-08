Problem Statement

Uma lotérica muito movimentada pretende implementar uma nova mecânica às filas dos seus caixas de atendimento. A lotérica possui 2 caixas, e a mecânica proposta é a seguinte: Sempre que um dos caixas estiver sem fila e chamar o próximo, a metade (arredondando para cima) traseira da fila do outro caixa será realocada para ele na ordem inversa à que ela se encontra (Os últimos serão os primeiros).

Você foi então contratado para desenvolver um sistema para registrar as movimentações das filas nos caixas, bem como calcular o valor total arrecadado por cada um dos caixas.

OBS: Não é permitido o uso de bibliotecas que forneça a função do algoritmo.

Input

O seu programa deverá iniciar no momento em que o supermercado abrir (com todas as filas vazias) e sua interface de comunicação seguirá o seguinte padrão:

ENTROU: N C P → Insere o cliente de nome N que irá pagar um total de P reais na fila do caixa C

PROXIMO: C → Chama o próximo cliente ao caixa C considerando e mecânica mencionada acima

FIM → Finaliza o programa.

Comando 1

Comando 2

...

Comando N

Output

Após o comando ENTROU, imprimir: "N entrou na fila C" onde N é o nome do cliente que entrou e C o número do caixa da fila em que ele entrou

Após o comando PROXIMO, imprimir: "N foi chamado para o caixa C", onde N é o nome do cliente chamado e C o número do caixa no qual ele foi atendido

Após o comando FIM, imprimir: "Caixa 1: R$ T1, Caixa 2: R$ T2", onde T1 é o valor total arrecadado pelo caixa 1, e T2 o valor total arrecadado pelo caixa 2, ambos impressos com 2 casas decimais.

Examples

Case: 1

Input

ENTROU: Matheus 1 100.00
ENTROU: Isabelle 1 5000.00
ENTROU: Valter 2 350.50
PROXIMO: 2
PROXIMO: 2
PROXIMO: 1
FIM

Output

Matheus entrou na fila 1
Isabelle entrou na fila 1
Valter entrou na fila 2
Valter foi chamado para o caixa 2
Isabelle foi chamado para o caixa 2
Matheus foi chamado para o caixa 1
Caixa 1: R$ 100.00, Caixa 2: R$ 5350.50
