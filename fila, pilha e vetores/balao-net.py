
#classe responsável pela criação dos dados dentro dos nós
class Dados():
    def __init__(self, numb):
        self.dado = numb
        #self que direciona o próximo número da lista
        self.prox = None
        #self que direciona o número antecessor a esse da lista
        self.last = None
#classe responsável pela criação da lista, adição de elementos, remoção e exibição
class Fila():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def add_last(self, string):
        if self.primeiro:
            ponteiro = self.ultimo
            self.ultimo = Dados(string)
            ponteiro.prox = self.ultimo
            self.ultimo.last = ponteiro
        else:
            self.primeiro = Dados(string)
            self.ultimo = self.primeiro
    def add(self, string):
        #if que checa se há ou não um primeiro termo, se há adiciona um novo termo ligando-o ao antecessor
        if self.primeiro:
            ponteiro = self.primeiro
            while ponteiro.prox:
                ponteiro = ponteiro.prox
            ponteiro.prox = Dados(string)
            ponteiro.prox.last = ponteiro
            self.ultimo = ponteiro.prox

        else:
            self.primeiro = Dados(string)
            self.ultimo = self.primeiro

    def exib(self):
        #checa cada número a partir do self.last de cada número afim de printa-los
        ponteiro = self.ultimo
        print(ponteiro.dado)
        while(ponteiro.last):
            ponteiro = ponteiro.last
            print(ponteiro.dado)

    def remove(self, string):
        ponteiro = self.primeiro
        pause = True
        #if para checar se o primeiro termo é o termo escolhido para remoção
        if ponteiro.dado == string:
            if ponteiro.prox == None:
                self.ultimo = None
            self.primeiro = ponteiro.prox
            self.primeiro.last = None
            del ponteiro
        else:
            while pause:
                ponteiro = ponteiro.prox
                #if que só é acionado se for o último termo da lista
                if ponteiro.prox == None:
                    ponteiro.last.prox = None
                    self.ultimo = ponteiro.last
                    del ponteiro
                    pause = False
                #if acionado pra qualquer termo da lista, menos o último
                elif ponteiro.dado == string:
                    ponteiro.last.prox = ponteiro.prox
                    ponteiro.prox.last = ponteiro.last
                    del ponteiro
                    pause = False

lista = Fila()
pause = True

while pause is True:
    entrada = input().split()
    if entrada[0] == 'END':
        pause = False
    elif entrada[0] == 'ADD':
        lista.add(entrada[1])
    elif entrada[0] == "FIND":
        lista.remove(entrada[1])
        lista.add_last(entrada[1])
    elif entrada[0] == 'REM':
        lista.remove(entrada[1])
    elif entrada[0] == "EXIB":
        lista.exib()



        