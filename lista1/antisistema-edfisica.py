

pilha = input().split(',')
locacao = int(input())

def pilhaImaculada(pilha, i):
    if pilha[i] < pilha[i + 1]:
        if i == len(pilha) - 1:
            return 'sucesso'
        else:
            return pilhaImaculada(pilha, i + 1)
    else:
        return 'caos'
def novaLocacao(pilha, cod, i):
    if pilha[i] < cod:
        return novaLocacao(pilha, cod, i + 1)
    else:
        pilha.insert(i, cod)
        return pilha
ordem = pilhaImaculada(pilha, 0)

if ordem == 'caos':
    print('A pilha está um caos.')
elif ordem == 'sucesso':
    pilha = novaLocacao(pilha, locacao, 0)
    print(pilha)
