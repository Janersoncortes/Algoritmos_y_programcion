"""
datos de entrada
parcial1--->p1--->float
parcial2--->p2--->float
parcial3--->p3--->float
examen--->e--->float
trabajo--->t--->float
datos de salida
nota--->n--->float
"""
#entrada
p1=float(input("digite nota del parcial 1: "))
p2=float(input("digite nota del parcial 2: "))
p3=float(input("digite nota del parcial 3: "))
e=float(input("digite nota del examen: "))
t=float(input("digite nota del trabajo: "))
#caja negra
n=((p1+p2+p3)/3)*0.55+0.3*e+0.15*t
print("nota final:", n)

