

class Grafo:

    def __init__(self, ver):
        self.vertices = ver
        self.grafo = [[] for i in range(self.vertices)]
    
    def add_aresta(self, vertice_pai, vertice_filho):
        self.grafo[vertice_pai].append(vertice_filho)
    def print_grafo(self):
        print(self.grafo)
    def check_amigo(self, amigo, lista):
        for i in range(len(lista)):
            if lista[i] == amigo:
                return 'encontrado'
        return 'not encontrado'
    def publication(self, qntd_amigos, lista_amigos, id):
        for i in range(0, len(self.grafo[id])):
            for j in range(len(self.grafo[self.grafo[id][i]])):
                if qntd_amigos == 0:
                    return lista_amigos
                var = self.check_amigo(self.grafo[self.grafo[id][i]][j], lista_amigos)
                if self.grafo[self.grafo[id][i]][j] == id:
                    var = 'encontrado'
                if var == 'not encontrado':
                    lista_amigos.append(self.grafo[self.grafo[id][i]][j])
                    qntd_amigos -= 1
        if qntd_amigos > 0:
            for i in range(len(self.grafo[id])):
                var, lista_amigos = self.publication2(qntd_amigos, lista_amigos, self.grafo[id][i], id)
                if var == 'sucess':
                    return lista_amigos
    def publication2(self, qntd_amigos, lista_amigos, id, id_check):
        for i in range(0, len(self.grafo[id])):
            for j in range(len(self.grafo[self.grafo[id][i]])):
                if qntd_amigos == 0:
                    return 'sucess', lista_amigos
                var = self.check_amigo(self.grafo[self.grafo[id][i]][j], lista_amigos)
                if self.grafo[self.grafo[id][i]][j] == id_check:
                    var = 'encontrado'
                if var == 'not encontrado':
                    lista_amigos.append(self.grafo[self.grafo[id][i]][j])
                    qntd_amigos -= 1
        return 'not', lista_amigos
lista_rede = []
vertices = int(input())
id = int(input())
dindin = int(input())
grafo = Grafo(vertices)
for i in range(vertices):
    var_vertice = input().split()
    var_vertice.remove(var_vertice[1])
    var_vertice = list(map(int, var_vertice))
    for j in range(1, len(var_vertice)):
        grafo.add_aresta(var_vertice[0], var_vertice[j])
        if var_vertice[0] == id:
            lista_rede.append(var_vertice[j])
qntd_amigos = dindin//(5.25)
lista_rede = grafo.publication(qntd_amigos, lista_rede, id)
lista_rede = list(map(str, lista_rede))
print(lista_rede)

