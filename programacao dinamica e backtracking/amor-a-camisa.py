

class Sector():
    def __init__(self, n, setores):
        self.lista_valores = [0]*n
        self.value = 0
        
    def pd(self, setores, n=-2, valor=0):
        peso = valor
        if n+2 < len(setores):
            if self.lista_valores[n+2] != 0:
                peso += self.lista_valores[n+2]
            else:
                peso += self.pd(setores, n+2, setores[n+2])
            if peso-valor > self.lista_valores[n+2]:
                self.lista_valores[n+2] = peso-valor
        if n+3 < len(setores):
            if self.lista_valores[n+3] != 0:
                peso1 = self.lista_valores[n+3]
            else:
                peso1 = self.pd(setores, n+3, setores[n+3])
            if peso1+valor > peso:
                peso = peso1+valor
            if peso1 > self.lista_valores[n+3]:
                self.lista_valores[n+3] = peso1
        if valor > self.value:
                self.value = valor
        return peso
    def print_valor(self):
        print(self.value)

n = int(input())
setores = input().split()
setores = list(map(int, setores))

result = Sector(n, setores)
print(result.pd(setores))
print(result.print_valor())
