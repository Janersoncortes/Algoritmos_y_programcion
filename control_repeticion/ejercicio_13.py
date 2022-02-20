listaa=[]
listab=[]
listac=[]
estudiantes=int(input("Ingrese la cantidad de estudiantes: "))
estu=int(input("digite un numero para agregar nombres y puntajes: "))
for i in range(0, estudiantes):
    est=input("ingrese nombre, puntaje: ")
    if(estu==1):
        s=(nombre, puntaje)=est.split(" ")
        nombre=str(nombre)
        puntaje=int(puntaje)
        listab.append(nombre)
        listaa.append(puntaje)
        listac.append(s)
        promedio=sum(listaa)/len(listaa)
        n=[i for i in listaa if i>promedio]       
        inf=(len(n)*100)/len(listaa)
        s=[i for i in listaa if i<promedio]
        sup=(len(s)*100)/len(listaa)
    elif(estu==2):
        break
print("El estudiante con el puntaje más alto es: ", (listac[listaa.index(max(listaa))]))
print("El estudiante con el puntaje más bajo es: ", (listac[listaa.index(min(listaa))]))
print("El puntaje maximo es: ", max(listaa))
print("El puntaje maximo es: ", min(listaa))
print("Promedio de puntajes: ", promedio)
print(f"Porcentaje de estudiantes que estan bajo el promedio: {inf}%")
print(f"Porcentaje de estudiantes que estan sobre el promedio: {sup}%")