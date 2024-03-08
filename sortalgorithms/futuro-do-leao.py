

def Merge(direita, esquerda):
        lista = direita+esquerda
        lista_direita = direita
        lista_esquerda = esquerda
        var_direita, var_esquerda = 0, 0
        for i in range(len(lista)):
            if var_esquerda > len(lista_esquerda) - 1:
                lista[i] = lista_direita[var_direita]
                var_direita += 1
            elif var_direita > len(lista_direita) - 1:
                lista[i] = lista_esquerda[var_esquerda]
                var_esquerda += 1 
            elif lista_esquerda[var_esquerda] >= lista_direita[var_direita]:
                lista[i] = lista_direita[var_direita]
                var_direita += 1
            elif lista_esquerda[var_esquerda] <= lista_direita[var_direita]:
                lista[i] = lista_esquerda[var_esquerda]
                var_esquerda += 1
        return lista
def mediana(lista):
    tamanho = len(lista)
    if tamanho%2 == 1:
        return int(lista[tamanho//2])
    else:
        return (int(lista[tamanho//2]) + (int(lista[tamanho//2 - 1]))) / 2
salario_sport = input().split()
salario_clube = input().split()
salario_sport = list(map(int, salario_sport))
salario_clube = list(map(int, salario_clube))
salario = Merge(salario_sport, salario_clube)
print(f'O salário sugerido por Juba na primeira negociação será de {mediana(salario):.2f} mil reais.')

