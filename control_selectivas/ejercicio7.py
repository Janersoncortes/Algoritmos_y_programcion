"""
Datos de entrada
distancia recorrida--->dr--->int
"""
#entrada
dr=int(input("Digite la distacia reccorida en Km: "))
#caja negra
if(dr<=300):
    pag=50000    
elif(dr>300 and dr<=1000):
    pag=70000+(30000*(dr-300))
elif(dr>1000):
    pag=150000+(9000*(dr-1000)+(30000*(dr-300)))
#Salida
print("El cliente debe pagar: ", pag)