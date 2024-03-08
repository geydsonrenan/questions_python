
ponteiro_folhas = None
def max_heapify(sequencia,k):
    global ponteiro_folhas
    l = 2 * k + 1
    r = 2 * k + 2
    if l < len(sequencia) and sequencia[l] > sequencia[k]:
        ponteiro = l
    else:
        ponteiro = k
    if r < len(sequencia) and sequencia[r] > sequencia[ponteiro]:
        ponteiro = r
    if ponteiro != k:
        sequencia[k], sequencia[ponteiro] = sequencia[ponteiro], sequencia[k]
        max_heapify(sequencia, ponteiro)
        

def build_max_heap(sequencia):
    global ponteiro_folhas
    n = int((len(sequencia)//2)-1)
    ponteiro_folhas = n + 1
    for k in range(n, -1, -1):
        max_heapify(sequencia,k)
def min(lista, k):
    ponteiro = lista[k]
    for i in range(k, len(lista)):
        if lista[i] < ponteiro:
            ponteiro = lista[i]
    return ponteiro
            
sequencia = input().split()
sequencia = list(map(int, sequencia))
build_max_heap(sequencia)
x = int(input())
i = 0

while True:
    if len(sequencia) == 0:
        break
    z = min(sequencia, ponteiro_folhas)*x
    if z < 0:
        z = z*-1
    k = sequencia[0] - z
    if k > 0:
        sequencia.append(k)
        build_max_heap(sequencia)
    sequencia.remove(sequencia[0])
    build_max_heap(sequencia)
    i += 1
print(f'{i} rodadas, partindo para a próxima!')
