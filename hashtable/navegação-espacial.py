

class HashTable:
    def __init__(self, tam):
        self.tamanho = tam
        self.list = [None]*tam


    def sch_key(self, key):
        position = key % self.tamanho
        if self.list[position] == key:
            return position
        else:
            for i in range(self.tamanho):
                if self.list[i] == key:
                    return i
            return None
    def cap(self, position):
        if self.list[position] == None:
            return None
        else:
            return self.list[position]
    def add(self, valor):
        position = valor % self.tamanho
        if self.list[position] == None:
            self.list[position] = valor
            return position
        else:
            for i in range(self.tamanho):
                if i + position >= self.tamanho:
                    position = -i
                if self.list[i + position] == None:
                    self.list[i + position] = valor
                    return i + position
            return 'cheio'
    def check_memory(self):
        for i in range(self.tamanho):
            if self.list[i] == None:
                return None
        return 'cheio'




memoria = int(input())
tabela = HashTable(memoria)
var = int(input())
for i in range(var):
    check = tabela.check_memory()
    if check == 'cheio':
        print('Toda memoria utilizada')
        break
    entrada = input().split(' ')
    if entrada[0] == 'ADD':
        result = tabela.add(int(entrada[1]))
        if result == 'cheio':
            print('Toda memoria utilizada')
        else:
            print(f'E: {result}')
    elif entrada[0] == 'CAP':
        result = tabela.cap(int(entrada[1]))
        if result == None:
            print('D')
        else:
            print(f'A: {result}')
    elif entrada[0] == 'SCH':
        result = tabela.sch_key(int(entrada[1]))
        if result == None:
            print('NE')
        else:
            print(f'E: {result}')
                

