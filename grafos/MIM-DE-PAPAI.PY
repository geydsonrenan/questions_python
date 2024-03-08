

class Grafo:

    def __init__(self, ver):
        self.vertices = ver
        self.grafo = [[0]*ver for i in range(self.vertices)]
        #for i in range(ver):
            #self.grafo[i][i] = 1

    def add(self, vertice, vertice_filho):
        self.grafo[vertice-1][vertice_filho-1] = 1
        self.grafo[vertice_filho-1][vertice-1] = 1

    def print(self):
        print(self.grafo)

    def contagem(self):
        contagem = 0
        lista_busca = []
        check = True
        vertices = []
        for i in range(len(self.grafo)):
            vertices.append(i)
            for j in range(len(self.grafo)):
                if self.grafo[i][j] == 1:
                    var, vertices = self.busca(vertices, j)
                    contagem += var
            contagem += 1
            lista_busca.append(contagem)
            contagem = 0
            vertices = []
        return lista_busca


    def busca(self, vertices, vertice_filho, contagem=1):
        check = True
        for i in vertices:
            if i == vertice_filho:
                contagem = 0
                return contagem, vertice_filho
        for i in range(len(self.grafo)):
            for j in vertices:
                if i == j:
                    check = False 
            if self.grafo[vertice_filho][i] == 1 and check == True:
                vertices.append(vertice_filho)
                contagem, vertices = self.busca(vertices, i, contagem+1)
            check = True
        vertices.append(vertice_filho)
        return contagem, vertices

entrada = input().split()
entrada = list(map(int, entrada))
grafo = Grafo(entrada[0])
for i in range(entrada[1]):
    conections = input().split()
    conections = list(map(int, conections))
    grafo.add(conections[0], conections[1])
lista_busca = grafo.contagem()
for i in range(len(lista_busca)):
    if i != len(lista_busca)-1:
        print(lista_busca[i], end= ' ')
    else:
        print(lista_busca[i])


