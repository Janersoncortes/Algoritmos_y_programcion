
#Entrada
Div=int(input(" "))
divd=int(input(" "))
A=int(Div/divd)
C=0
for i in range(A):
    print(Div,"-",divd,"=",Div-divd)
    Div=int(Div-divd)
    C=C+1
#Salida
print("El cociente es",C,"y el resto es",Div)