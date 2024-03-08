
class Dado():
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Lista_f():
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
    
    def add(self, dado):
        if self.primeiro:
            ponteiro = self.primeiro
            while ponteiro.prox:
                ponteiro = ponteiro.prox
            ponteiro.prox = Dado(dado)

        else:
            self.primeiro = Dado(dado)
        self.tamanho += 1
    def rem(self):
        ponteiro = self.primeiro
        self.primeiro = ponteiro.prox
        self.tamanho -= 1
        del ponteiro
    def check(self):
        if self.tamanho > 0:
            lista.rem()
            return 'sucess'
        else:
            return 'fail'
    def return_primeiro(self):
        return self.primeiro

lista = Lista_f()
pause = True
entrada = list(input())
for i in range(len(entrada)):
    if entrada[i] == 'F':
        lista.add(i + 1)
    elif entrada[i] == 'V':
        resposta = lista.check()
        if resposta == 'fail':
            print(f'Incorreto, devido a capa na posição {i + 1}.')
            break
if len(entrada) == 0:
    print('Correto.')
elif resposta == 'sucess':
    result = lista.return_primeiro()
    if result == None:
        print(f'Correto.')
    else:
        print(f'Incorreto, devido a capa na posição {result.dado}.')
    
