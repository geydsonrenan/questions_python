
class Dado():
    def __init__(self, nome, valor):
        self.nome = nome
        self.caixa = valor
        self.prox = None
class Fila():
    def __init__(self, fila):
        self.fila = fila
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
        self.dinheiro = 0
    
    def entrar(self, nome, valor, rep):
        if self.primeiro:
            ponteiro = self.primeiro
            while ponteiro.prox:
                ponteiro = ponteiro.prox
            ponteiro.prox = Dado(nome, valor)
            self.ultimo = ponteiro.prox
            print(f'{nome} entrou na fila {self.fila}')

        else:
            self.primeiro = Dado(nome, valor)
            self.ultimo = self.primeiro
            print(f'{nome} entrou na fila {self.fila}')
        self.tamanho += 1
    def add(self, nome, valor):
        if self.primeiro:
            ponteiro = self.primeiro
            while ponteiro.prox:
                ponteiro = ponteiro.prox
            ponteiro.prox = Dado(nome, valor)
            self.ultimo = ponteiro.prox

        else:
            self.primeiro = Dado(nome, valor)
            self.ultimo = self.primeiro
        self.tamanho += 1
    def rem(self, elem):
        ponteiro = self.primeiro
        pause = True
        if ponteiro.nome == elem:
            if self.tamanho == 1:
                self.primeiro = None
                self.ultimo = None
            else:
                self.primeiro = ponteiro.prox
            del ponteiro
        else:
            while pause:
                #if que só é acionado se for o último termo da lista
                if ponteiro.prox == self.ultimo:
                    self.ultimo = ponteiro
                    self.ultimo.prox = None
                    del ponteiro.prox
                    pause = False
                    break
                ponteiro = ponteiro.prox
        self.tamanho -= 1
    def exib(self):
        ponteiro = self.primeiro
        print(self.ultimo.nome)
        print(ponteiro.nome)
        while ponteiro.prox:
            ponteiro = ponteiro.prox
            print(ponteiro.nome)
    def proximo(self):
        ponteiro = self.primeiro
        if self.tamanho == 0:
            if self.fila == 1:
                fila2.mudanca()
                ponteiro = self.primeiro
                print(f'{ponteiro.nome} foi chamado para o caixa {self.fila}')
                self.dinheiro += float(ponteiro.caixa)
                fila1.rem(ponteiro.nome)
                
            else:
                fila1.mudanca()
                ponteiro = self.primeiro
                print(f'{ponteiro.nome} foi chamado para o caixa {self.fila}')
                self.dinheiro += float(ponteiro.caixa)
                fila2.rem(ponteiro.nome)
                
        else:
            if self.fila == 1:
                ponteiro = self.primeiro
                print(f'{ponteiro.nome} foi chamado para o caixa {self.fila}')
                self.dinheiro += float(ponteiro.caixa)
                fila1.rem(ponteiro.nome)
                
            else:
                ponteiro = self.primeiro
                print(f'{ponteiro.nome} foi chamado para o caixa {self.fila}')
                self.dinheiro += float(ponteiro.caixa)
                fila2.rem(ponteiro.nome)


    def mudanca(self):
        ponteiro = self.primeiro
        if self.tamanho == 1:
            if self.fila == 1:
                fila2.add(self.ultimo.nome, self.ultimo.caixa)
                fila1.rem(ponteiro.nome)
            else:
                fila1.add(self.ultimo.nome, self.ultimo.caixa)
                fila2.rem(ponteiro.nome)
        elif self.tamanho%2 == 0:
            qntd = int(self.tamanho/2)
            for i in range(qntd):
                ponteiro = self.primeiro
                while True:
                    if ponteiro.prox == self.ultimo:
                        if self.fila == 1:
                            fila2.add(self.ultimo.nome, self.ultimo.caixa)
                            fila1.rem(self.ultimo.nome)
                        else:
                            fila1.add(self.ultimo.nome, self.ultimo.caixa)
                            fila2.rem(self.ultimo.nome)
                        break
                    ponteiro = ponteiro.prox
        elif self.tamanho%2 == 1:
            qntd = int(self.tamanho//2)
            for i in range(qntd):
                ponteiro = self.primeiro
                while True:
                    if ponteiro.prox == self.ultimo:
                        if self.fila == 1:
                            fila2.add(self.ultimo.nome, self.ultimo.caixa)
                            fila1.rem(self.ultimo.nome)
                        else:
                            fila1.add(self.ultimo.nome, self.ultimo.caixa)
                            fila2.rem(self.ultimo.nome)
                        break
                    ponteiro = ponteiro.prox

                

            

fila1 = Fila(1)
fila2 = Fila(2)
pause = True

while pause is True:
    entrada = input().split()
    if entrada[0] == 'FIM':
        pause = False
    elif entrada[0] == 'ENTROU:':
        if entrada[2] == '1':
            fila1.entrar(entrada[1], entrada[-1], False)
        else:
            fila2.entrar(entrada[1], entrada[-1], False)
    elif entrada[0] == 'PROXIMO:':
        if entrada[1] == '1':
            fila1.proximo()
        else:
            fila2.proximo()


print(f"Caixa 1: R${fila1.dinheiro: .2f}, Caixa 2: R${fila2.dinheiro: .2f}")



