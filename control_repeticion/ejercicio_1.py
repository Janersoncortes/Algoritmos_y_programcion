"""
Entradas
K--> int
N--> int
Salidas
Kn--> int--> lista
"""
N=int(input("N:"))
K=int(input("K:"))
nk=N-1
while (N>K):
  lista=[N,nk]
  for i in range (K,nk):
    lista.append(i)
  lista.sort(reverse=True)
  print(lista)
  break
else:
  print("K debe ser menor que N")