"""
Datos de entrada
variable_uno-->a-->str
variable_dos-->b-->str
variable_tres-->c-->str
variable_cuatro-->d-->str
Datos de salida
numero_redondeado-->nr-->int
"""
#Entradas
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
d=int(input("Ingrese el cuarto número: "))
#Caja negra
resultado=""
if(b>4):
    a=a+1
    b=0
    c=0
    d=0
    
elif(b>=5):
    b=0
    c=0
    d=0    
elif(c<9):
    b=b+1
    c=0
    d=0
#Salida
print("El resultado redondeado es: ", str(a)+str(b)+str(c)+str(d))
