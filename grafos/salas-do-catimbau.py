salas = []


while True:
  sala = input().split()
  salas.append(sala)
  if sala[0] == 'Tesouro':
      break
    
def find_tesouro(salas, chaves=[1], stage=0):
    if stage > len(chaves)-1:
        return False
    if chaves[stage] == len(salas):
        return True
    if chaves[stage] > len(salas):
        return find_tesouro(salas, chaves, stage=stage+1)
    for chave in salas[chaves[stage]-1]:
        if int(chave) not in chaves:
          chaves.append(int(chave))
    return find_tesouro(salas, chaves, stage=stage+1)
    
    
    
    
resultado = find_tesouro(salas)

if resultado == True:
    print("TESOURO :)")
    
else:
    print("SEM TESOURO :(")
