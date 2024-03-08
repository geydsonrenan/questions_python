
# classe para criar os nós
class Node():
    def __init__(self, dado, nivel):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        
#classe para criar a arvre
class Tree():
    def __init__(self):
        self.raiz = None
        self.elementos = 0
        # self para printar o nível dos nós no search
        self.contagem = 0
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
                        self.elementos += 1
                        print(var)
                        break
                    # se houver o ponteiro vira esse nó da direita e a while se repete
                    else:
                        ponteiro = ponteiro.direita
                # se o novo nó for menor que o ponteiro, ele checa se há um nó a esquerda do nó checado        
                elif str < ponteiro.dado:
                    # se não houver ele entra e adiciona o nó nessa posição
                    if ponteiro.esquerda == None:
                        ponteiro.esquerda = Node(str, var)
                        self.elementos += 1
                        print(var)
                        break
                    # se houver o ponteiro vira esse nó da esquerda e a while se repete
                    else:
                        ponteiro = ponteiro.esquerda
        # se não houver uma raiz na arvre esse else irá criar um                
        else:
            self.raiz = Node(str, 0)
            print(0)
            self.elementos += 1
    # função para teste, exibe a árvre em ordem
    def exib(self, dado=None):
        if dado == None:
            dado = self.raiz
        if dado.esquerda:
            self.exib(dado.esquerda)
        print(dado.dado)
        if dado.direita:
            self.exib(dado.direita)
    # função recursiva para o comando 'SCH', vai descendo na árvre até encontrar o nó e quando encontrar aciona outra função para rotacionar
    def search(self, dado, node=None):
        if node == None:
            #variavel para contar o nível
            self.contagem = 0
            node = self.raiz
        # se o nó atual for maior que o nó requisitado ele desce pra esquerda do nó atual
        if node.dado > dado:
            # desce um nível
            self.contagem += 1
            # se houver um nó na esquerda do nó atual, ele repete e aciona a própria função com o filho a esquerda do nó atual
            if node.esquerda:
                #aciona novamente a função com o filho a esquerda, quando o nó procurado for encontrado a variavel retorno vai receber "encontrado"
                retorno, node_sch = self.search(dado, node.esquerda)
                # se o nó procurado for encontrado a variavel retorno vai receber 'encontrado' e entrar
                #aqui a função vai estar subindo na árvre e acionando outra função para fazer as rotações nos nós atuais
                if retorno == "encontrado":
                    # lança para o def mudanca o nó atual e o nó procurado para que seja feita a rotação e elee vá subindo
                    self.mudanca(node, node_sch)
                    # retorna 'encontrado' para que o próximo nó seja modificado
                    return 'encontrado', node_sch
                else:
                    return 'error', None
            # se não houver um nó, significa que o nó procurado não se encontra na arvre
            else:
                return 'error', None
        # se o nó atual for menor que o nó requisitado ele desce pra direita do nó atual
        elif node.dado < dado:
            self.contagem += 1
            # se houver um nó na direita do nó atual, ele repete e aciona a própria função com o filho a direita do nó atual
            if node.direita:
                #aciona novamente a função com o filho a direita, quando o nó procurado for encontrado a variavel retorno vai receber "encontrado"
                retorno, node_sch = self.search(dado, node.direita)
                # se o nó procurado for encontrado, a variavel retorno vai receber 'encontrado' e entrar
                #aqui a função vai estar subindo na árvre e acionando outra função para fazer as rotações nos nós atuais
                if retorno == 'encontrado':
                    # lança para o def mudanca o nó atual e o nó procurado para que seja feita a rotação e elee vá subindo
                    self.mudanca(node, node_sch)
                    # retorna 'encontrado' para que o próximo nó seja modificado
                    return 'encontrado', node_sch
                else:
                    return 'error', None
            # se não houver um nó, significa que o nó procurado não se encontra na arvre
            else:
                return 'error', None
        # se o nó atual for o nó requisitado ele retorna que encontrou e retorna o nó requisitado
        elif node.dado == dado:
            print(self.contagem)
            return 'encontrado', node
        
    # função para efetuar as rotações na árvore
    def mudanca(self, node_atual, node_search):
        # se o nó a ser rotacionado for a raiz
        if node_atual == self.raiz:
            if self.raiz.dado < node_search.dado:
                #se houver filhos a esquerda do nó requisitado ele os adiciona na direita do nó atual e sobe o nó do search pro lugar do nó atual
                if node_search.esquerda:
                    self.raiz.direita = node_search.esquerda
                    node_search.esquerda = self.raiz
                    self.raiz = node_search
                # se não, apenas substitui o nó procurado do search pelo nó atual
                else:
                    self.raiz.direita = None
                    node_search.esquerda = self.raiz
                    self.raiz = node_search
            elif self.raiz.dado > node_search.dado:
                #se houver filhos a direita do nó requisitado ele os adiciona na esquerda do nó atual e sobe o nó do search pro lugar do nó atual
                if node_search.direita:
                    self.raiz.esquerda = node_search.direita
                    node_search.direita = self.raiz
                    self.raiz = node_search
                # se não, apenas substitui o nó procurado do search pelo nó atual
                else:
                    self.raiz.esquerda = None
                    node_search.direita = self.raiz
                    self.raiz = node_search
        # se o nó atual for menor que o nó requisitado no search
        elif node_atual.dado < node_search.dado:
            #se houver filhos a esquerda do nó requisitado ele os adiciona na direita do nó atual e sobe o nó do search pro lugar do nó atual
            if node_search.esquerda:
                node_atual.direita = node_search.esquerda
                node_search.esquerda = node_atual
            # se não, apenas substitui o nó procurado do search pelo nó atual
            else:
                node_atual.direita = None
                node_search.esquerda = node_atual
        # se o nó atual for maior que o nó requisitado no search
        elif node_atual.dado > node_search.dado:
            #se houver filhos a direita do nó requisitado ele os adiciona na esquerda do nó atual e sobe o nó do search pro lugar do nó atual
            if node_search.direita:
                node_atual.esquerda = node_search.direita
                node_search.direita = node_atual
            # se não, apenas substitui o nó procurado do search pelo nó atual
            else:
                node_atual.esquerda = None
                node_search.direita = node_atual
        



arvre = Tree()
entrada = input()
cpf_nomes = {}
# laço que vai receber os inputs
while entrada != "FIM":
    entrada = entrada.split()
    if entrada[0] == "ADD":
        cpf_nomes[entrada[2]] = entrada[1]
        arvre.add(entrada[1])
    
    elif entrada[0] == "---":
        pass

    elif entrada[1] == "disse":
        arvre.search(cpf_nomes[entrada[0]])
    
    else:
        arvre.inocente(cpf_nomes[entrada[0]])
    entrada = input()
