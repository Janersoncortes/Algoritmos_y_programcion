"""
datos de salida
Valor_1--->p--->int
Valor_2--->q--->int
"""
p=int(input("Digite el valor de p: "))
q=int(input("Digite el valor de q: "))
#Caja negra
respuesta=""
e=(p**3+q**4-2*(p**2))
if(e>680):
    print("P y Q satisfacen la expresión")
else:
    print("P y Q no satisfacen la expresion")