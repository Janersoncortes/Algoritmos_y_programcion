"""
Datos de entrada
variable1--->a--->int
variable2--->b--->int
variable3--->c--->int
variable4--->d--->int
Datos de salida
"""
#entrada
a=int(input("digite variable 1: "))
b=int(input("digite variable 2: "))
c=int(input("digite variable 3: "))
d=int(input("digite variable 4: "))
#caja negra
if (d==0):
    re=(a-c)**2
elif(d>0):    
    re=((a-b)**3)/d
    print("el valor es: ", re)