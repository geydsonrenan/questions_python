class HashTable:
    def __init__(self, tam):
        self.tamanho = tam
        self.hash = [None]*tam

    def listar(self, lista, MN):
        lista_cpf = list(lista)
        return self.multp(lista_cpf, MN)
    def multp(self, lista, MN):
        var = []
        tabela = HashTable(10)
        for i in lista:
            tabela.add(int(i), MN)
        for i in range(10):
            if tabela.sch(i) != None:
                try:
                    if len(tabela.sch(i)):
                        var.append(i * len(tabela.sch(i))*10)
                except:
                    var.append(i*10)
        return self.soma(var, MN)
    def soma(self, lista, MN):
        for i in range(len(lista)):
            for j in range(len(lista)):
                if i == j:
                    pass
                elif lista[i] + lista[j] == MN:
                    return 'UP'
        return 'NOT'
    def add(self, cpf, MN):
        position = cpf % self.tamanho
        if self.hash[position] == None:
            self.hash[position] = cpf
        else:
            try:
                if len(self.hash[position]):
                    self.hash[position].append(cpf)
            except:
                self.hash[position] = [self.hash[position]]
                self.hash[position].append(cpf)
    def sch(self, key):
        return self.hash[key]

qntd_entradas = int(input())
tabela = HashTable(11)
for i in range(qntd_entradas):
    entrada = input().split(' ')
    result = tabela.listar(entrada[0], int(entrada[1]))
    if result == 'UP':
        result = tabela.add(int(entrada[0]), int(entrada[1]))
        print('UP Permission')
    elif result == 'NOT':
        print('NOT Permission')