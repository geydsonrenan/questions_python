class Node():
    def __init__(self, dado, nivel):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.nivel = nivel
        self.pai = None
        self.fb = 0
        
#classe para criar a arvre
class Tree():
    def __init__(self):
        self.raiz = None
        self.altura = 0
        self.contagem_esq = 0
        self.contagem_dir = 0
        self.dado_balancear = None
        self.lista = []
    # função para adicionar novos nós na arvre
    def add(self, str):
        # se houver raiz ele entra
        if self.raiz:
            ponteiro = self.raiz
            # variavel para contar o nível dentro do laço abaixo
            var = 0
            # laço para mover o ponteiro até um lugar adequado para adicionar o novo nó
            while True:
                var += 1
                # se o novo nó for maior que o ponteiro, ele checa se há um nó a direita do nó checado
                if str > ponteiro.dado:
                    # se não houver ele entra e adiciona o nó nessa posição
                    if ponteiro.direita == None:
                        ponteiro.direita = Node(str, var)
                        ponteiro.direita.pai = ponteiro
                        break
                    # se houver o ponteiro vira esse nó da direita e a while se repete
                    else:
                        ponteiro = ponteiro.direita
                # se o novo nó for menor que o ponteiro, ele checa se há um nó a esquerda do nó checado        
                elif str < ponteiro.dado:
                    # se não houver ele entra e adiciona o nó nessa posição
                    if ponteiro.esquerda == None:
                        ponteiro.esquerda = Node(str, var)
                        ponteiro.esquerda.pai = ponteiro
                        break
                    # se houver o ponteiro vira esse nó da esquerda e a while se repete
                    else:
                        ponteiro = ponteiro.esquerda
                elif str == ponteiro.dado:
                    return 'presente'
            self.varredura()
            if self.dado_balancear != None:
                self.balanceada(self.dado_balancear)
            self.dado_balancear = None
            return 'adicionado'
        # se não houver uma raiz na arvre esse else irá criar um                
        else:
            self.raiz = Node(str, 0)
            return 'adicionado'
    def exib(self, dado=None):
        if dado == None:
            dado = self.raiz
            self.lista = []
        if self.raiz == None:
            return
        if dado.esquerda:
            self.exib(dado.esquerda)
        self.lista.append(dado.dado)
        if dado.direita:
            self.exib(dado.direita)
    def exibir(self, dado=None):
        if dado == None:
            dado = self.raiz
        if dado.esquerda and dado.direita:
            print(f'{dado.dado} ajuda {dado.esquerda.dado} e {dado.direita.dado}')
        elif dado.esquerda:
            print(f'{dado.dado} ajuda {dado.esquerda.dado}')
        elif dado.direita:
            print(f'{dado.dado} ajuda {dado.direita.dado}')
        else:
            print(f'{dado.dado} não ajuda ninguém')
        if dado.esquerda:
            self.exibir(dado.esquerda)
        if dado.direita:
            self.exibir(dado.direita)
    def sch(self, str, dado=None):
        if dado == None:
            dado = self.raiz
        if dado.esquerda:
            self.sch(str, dado.esquerda)
        if str == dado.dado:
            self.exibir(dado)
            return
        if dado.direita:
            self.sch(str, dado.direita)
          
    def max(self, dado=None):
        if self.raiz is None:
            return 'vazia'
        if dado == None:
            ponteiro = self.raiz
        else:
            ponteiro = dado
        while True:
            if ponteiro.direita:
                ponteiro = ponteiro.direita                
            else:
                return ponteiro
    def min(self, dado=None):
        if self.raiz is None:
            return 'vazia'
        if dado == None:
            ponteiro = self.raiz
        else:
            ponteiro = dado
        while True:
            if ponteiro.esquerda:
                ponteiro = ponteiro.esquerda                
            else:
                return ponteiro
    def rem(self, no_rem, dado=None):
        if dado == None:
            dado = self.raiz
        if self.raiz == None:
            return ''
        if no_rem == dado.dado:
            if self.raiz.dado == no_rem:
                if dado.esquerda is None and dado.direita is None:
                    self.raiz = None
                elif (dado.esquerda is None and dado.direita != None) or (dado.direita is None and dado.esquerda != None):
                    if dado.esquerda:
                        self.raiz = dado.esquerda
                    else:
                        self.raiz = dado.direita
                    self.raiz.pai = None
                elif dado.esquerda != None and dado.direita != None:
                    no_subs = self.min(dado.direita)
                    if no_subs.pai.esquerda == no_subs:
                        no_subs.pai.esquerda = no_subs.direita
                    
                    
                    no_subs.esquerda = dado.esquerda
                    if dado.direita != no_subs:
                        no_subs.direita = dado.direita
                    if no_subs.esquerda:
                        no_subs.esquerda.pai = no_subs
                    if no_subs.direita:
                        no_subs.direita.pai = no_subs 
                    self.raiz = no_subs
            elif dado.esquerda is None and dado.direita is None:
                if dado.pai.esquerda == dado:
                    dado.pai.esquerda = None
                else:
                    dado.pai.direita = None
            elif (dado.esquerda is None and dado.direita != None) or (dado.direita is None and dado.esquerda != None):
                if dado.esquerda:
                    if dado.pai.esquerda == dado:
                        dado.pai.esquerda = dado.esquerda
                    else:
                        dado.pai.direita = dado.esquerda
                    dado.esquerda.pai = dado.pai
                else:
                    if dado.pai.esquerda == dado:
                        dado.pai.esquerda = dado.direita
                    else:
                        dado.pai.direita = dado.direita
                    dado.direita.pai = dado.pai
            elif dado.esquerda != None and dado.direita != None:
                no_subs = self.min(dado.direita)
                if no_subs.pai.esquerda == no_subs:
                    no_subs.pai.esquerda = no_subs.direita

                if dado.pai.esquerda == dado:
                    dado.pai.esquerda = no_subs

                else:
                    dado.pai.direita = no_subs
                no_subs.pai = dado.pai
                no_subs.esquerda = dado.esquerda
                if dado.direita != no_subs:
                    no_subs.direita = dado.direita
                if no_subs.esquerda:
                    no_subs.esquerda.pai = no_subs
                if no_subs.direita:
                    no_subs.direita.pai = no_subs 
            self.varredura()
            if self.dado_balancear != None:
                self.balanceada(self.dado_balancear)
            self.dado_balancear = None
            return 'sucess'
        elif no_rem < dado.dado:
            if dado.esquerda:
                return self.rem(no_rem, dado.esquerda)
            else:
                return 'error'
        elif no_rem > dado.dado:
            if dado.direita:
                return self.rem(no_rem, dado.direita)
            else:
                return 'error'
    def varredura(self, dado=None):
        if dado == None:
            dado = self.raiz
        if self.raiz == None:
            return
        if dado.esquerda:
            self.check_esquerda(dado.esquerda)
        if dado.direita:
            self.check_direita(dado.direita)
        Fb = self.contagem_dir - self.contagem_esq
        dado.fb = Fb
        if Fb < -1 or Fb > 1:
            self.dado_balancear = dado
        self.contagem_dir = 0
        self.contagem_esq = 0
        if dado.esquerda:
            self.varredura(dado.esquerda)
        if dado.direita:
            self.varredura(dado.direita)
    def check_esquerda(self, dado, i=1):
        if dado.esquerda:
            self.check_esquerda(dado.esquerda, i + 1)
        if dado.direita:
            self.check_esquerda(dado.direita, i + 1)
        if i > self.contagem_esq:
            self.contagem_esq = i
    def check_direita(self, dado, i=1):
        if dado.esquerda:
            self.check_direita(dado.esquerda, i + 1)
        if dado.direita:
            self.check_direita(dado.direita, i + 1)
        if i > self.contagem_dir:
            self.contagem_dir = i
    def balanceada(self, dado):
        if dado.fb < -1:
            if dado.esquerda.fb < 0:
                self.rotacao_simples_direita(dado)
            else:
                self.rotacao_simples_esquerda(dado.esquerda)
                self.rotacao_simples_direita(dado)
        elif dado.fb > 1:
            if dado.direita.fb > 0:
                self.rotacao_simples_esquerda(dado)
            else:
                self.rotacao_simples_direita(dado.direita)
                self.rotacao_simples_esquerda(dado)
    def rotacao_simples_esquerda(self, no):
        dado_pulo = no.direita
        no.direita = dado_pulo.esquerda
        if dado_pulo.esquerda != None:
            no.direita.pai = no
        dado_pulo.esquerda = no
        if no == self.raiz:
            self.raiz = dado_pulo
        elif no.pai.esquerda == no:
            no.pai.esquerda = dado_pulo
            dado_pulo.pai = no.pai
        elif no.pai.direita == no:
            no.pai.direita = dado_pulo
            dado_pulo.pai = no.pai
        no.pai = dado_pulo
    def rotacao_simples_direita(self, no):
        dado_pulo = no.esquerda
        no.esquerda = dado_pulo.direita
        if dado_pulo.direita != None:
            no.esquerda.pai = no
        dado_pulo.direita = no
        if no == self.raiz:
            self.raiz = dado_pulo
        elif no.pai.direita == no:
            no.pai.direita = dado_pulo
            dado_pulo.pai = no.pai
        elif no.pai.esquerda == no:
            no.pai.esquerda = dado_pulo
            dado_pulo.pai = no.pai
        no.pai = dado_pulo

    def alt(self, dado=None, i=0):
        if dado == None:
            dado = self.raiz
        if self.raiz is None:
            self.altura = 0
        if dado.esquerda:
            self.alt(dado.esquerda, i + 1)
        if dado.direita:
            self.alt(dado.direita, i + 1)
        if i > self.altura:
            self.altura = i
    def alt_print(self):
        return self.altura
    def print_lista(self):
        return self.lista
arvre = Tree()

while True:
    entrada = input().split(' ')
    if entrada[0] == 'DELETAR':
        result = arvre.rem(entrada[1])
        if result == 'error' or result == '':
            print(f'{entrada[1]} NAO ENCONTRADO')
        elif result == 'sucess':
            print(f'{entrada[1]} DELETADO')
    elif entrada[0] == 'INSERIR':
        result = arvre.add(entrada[1])
        if result == 'adicionado':
            print(f'{entrada[1]} INSERIDO')
        else:
            print(f'{entrada[1]} JA EXISTE')
    elif entrada[0] == 'MAXIMO':
        result = arvre.max()
        if result == 'vazia':
            print('ARVORE VAZIA')
        else:
            print(f'MAIOR: {result.dado}')
    elif entrada[0] == 'MINIMO':
        result = arvre.min()
        if result == 'vazia':
            print('ARVORE VAZIA')
        else:
            print(f'MENOR: {result.dado}')
    elif entrada[0] == 'ALTURA':
        arvre.alt()
        result = arvre.alt_print()
        print(f'ALTURA: {result + 1}')
    elif entrada[0] == 'FIM':
        arvre.exib()
        result = arvre.print_lista()
        if result == []:
            print('ARVORE VAZIA')
        else:
            print(*result)
        break
    elif entrada[0] == 'VER':
        if len(entrada) == 2:
            arvre.sch(entrada[1])
        else:
            arvre.exibir()
