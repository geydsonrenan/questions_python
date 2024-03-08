class Back():
    def __init__(self):
        pass
    def backtrack(self, n, resto, fila=[]):
        if len(fila) > 1:
            if fila[-2] > fila[-1]:
                return
        if sum(fila) == n:
            print(fila)
            return
        for i in range(1, resto+1):
            fila.append(i)
            if (resto - i >= i) or (resto - i == 0):
                self.backtrack(n, resto-i, fila)
            del fila[-1]


n = int(input())


print(f'Uma sessão com {n} pessoas pode ter sua audiência nos seguintes subgrupos:')
result = Back()
result.backtrack(n, n)