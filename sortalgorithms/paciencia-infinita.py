
comps_quick = 0
trocas_quick = 0


def bubblesort(lista_bubble, actions=None):
    comps = 0
    trocas = 0
    for i in range(len(lista_bubble) - 1):
        for j in range(len(lista_bubble) - i - 1):
            if lista_bubble[j] > lista_bubble[j+1]:
                trocas += 1
                if actions is not None:
                    if comps + trocas == actions:
                        return lista_bubble
                ponteiro = lista_bubble[j]
                lista_bubble[j] = lista_bubble[j+1]
                lista_bubble[j+1] = ponteiro
            comps += 1
            if actions is not None:
                if comps + trocas == actions:
                    return lista_bubble
    return lista_bubble, comps, trocas

def selectionsort(lista_selec, actions=None):
    comps = 0
    trocas = 0
    for i in range(len(lista_selec) - 1):
        minimum = lista_selec[i]
        for j in range(i, len(lista_selec) - 1):
            if minimum > lista_selec[j+1]:
                minimum = lista_selec[j+1]
                ponteiro = j + 1
            comps += 1
            if actions is not None:
                if comps + trocas == actions:
                    return lista_selec
        if lista_selec[i] == minimum:
            ponteiro = i
        else:
            lista_selec[ponteiro] = lista_selec[i]
            lista_selec[i] = minimum
            trocas += 1
            if actions is not None:
                if comps + trocas == actions:
                    return lista_selec
    return lista_selec, comps, trocas
def insertionsort(lista_inser, actions=None):
    comps = 0
    trocas = 0
    for i in range(1, len(lista_inser)):
        ponteiro = lista_inser[i]
        position = i - 1

        while position >= 0 and ponteiro < lista_inser[position]:
            comps += 1
            if actions is not None:
                if comps + trocas == actions:
                    return lista_inser
            lista_inser[position + 1] = lista_inser[position]
            position -= 1
            trocas += 1
            if actions is not None:
                if comps + trocas == actions:
                    return lista_inser
        
        lista_inser[position + 1] = ponteiro
        if position >= 0:
            comps += 1
        if actions is not None:
            if comps + trocas == actions:
                return lista_inser
    return lista_inser, comps, trocas
def shellsort(lista_shell, actions=None):
    trocas = 0
    comps = 0
    position = len(lista_shell) // 2
    while position > 0:
        for i in range(position, len(lista_shell)):
            ponteiro = lista_shell[i]
            j = i
            while j >= position and lista_shell[j - position] > ponteiro:
                comps += 1
                if actions is not None:
                    if comps + trocas == actions:
                        return lista_shell
                lista_shell[j] = lista_shell[j - position]
                j -= position
                trocas += 1
                if actions is not None:
                    if comps + trocas == actions:
                        return lista_shell

            lista_shell[j] = ponteiro
            if j >= position:
                comps += 1
            if actions is not None:
                if comps + trocas == actions:
                    return lista_shell
        position //= 2
    return lista_shell, comps, trocas

def quicksort(A, lo, hi):
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)
    return A

def partition(A, lo, hi):
    global comps_quick
    global trocas_quick
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
        if i >= j:
            return j
        while A[i] < pivot:
            comps_quick += 1
            i += 1
        while A[j] > pivot:
            comps_quick += 1
            j -= 1
        trocas_quick += 1
        A[i], A[j] = A[j], A[i] 


lista = input().split()
lista_entrada = list(map(int, lista))
lista = lista_entrada[:]
caca_rato, comps_bubble, trocas_bubble = bubblesort(lista)
if comps_bubble + trocas_bubble > 0:
    maior = comps_bubble + trocas_bubble
    ganhador = 'Caça-Rato'
lista = lista_entrada[:]
print(f'Caça-Rato ordena a lista com {comps_bubble} comparações e {trocas_bubble} trocas.')
grafite, comps_selection, trocas_selection = selectionsort(lista)
if comps_selection + trocas_selection < maior:
    maior = comps_selection + trocas_selection
    ganhador = 'Grafite'
lista = lista_entrada[:]
print(f'Grafite ordena a lista com {comps_selection} comparações e {trocas_selection} trocas.')
lacraia, comps_insertion, trocas_insertion = insertionsort(lista)
if comps_insertion + trocas_insertion < maior:
    maior = comps_insertion + trocas_insertion
    ganhador = 'Lacraia'
lista = lista_entrada[:]
print(f'Lacraia ordena a lista com {comps_insertion} comparações e {trocas_insertion} trocas.')
rivaldo, comps_shell, trocas_shell = shellsort(lista)
if comps_shell + trocas_shell < maior:
    maior = comps_shell + trocas_shell
    ganhador = 'Rivaldo'
lista = lista_entrada[:]
print(f'Rivaldo ordena a lista com {comps_shell} comparações e {trocas_shell} trocas.')
toninho = quicksort(lista, 0, len(lista) - 1)
if comps_quick + trocas_quick  < maior:
    maior = comps_quick + trocas_quick
    ganhador = 'Toninho'
lista = lista_entrada[:]

print(f'Toninho ordena a lista com {comps_quick} comparações e {trocas_quick} trocas.')
print('-VENCEDOR DA RODADA-')
print(f'O vencedor da rodada é {ganhador}, com {maior} ações.')
print('-Toninho está a dormir...-')
print('Os outros estagiários retornam as seguintes listas com essa quantidade de ações:')

if ganhador != 'Caça-Rato':
    bubble = bubblesort(lista, maior)
    print(f'Com {maior} ações, Caça-Rato ordena a lista assim: {bubble}')
lista = lista_entrada[:]
if ganhador != 'Grafite':
    selection = selectionsort(lista, maior)
    print(f'Com {maior} ações, Grafite ordena a lista assim: {selection}')
lista = lista_entrada[:]
if ganhador != 'Lacraia':
    insertion = insertionsort(lista, maior)
    print(f'Com {maior} ações, Lacraia ordena a lista assim: {insertion}')
lista = lista_entrada[:]
if ganhador != 'Rivaldo':
    shell = shellsort(lista, maior)
    print(f'Com {maior} ações, Rivaldo ordena a lista assim: {shell}')


