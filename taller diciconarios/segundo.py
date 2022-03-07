diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
lista=[]
for value in diccionario.items():
    i=((value[1]))
    lista.append(i)
a=[]    
a=(set(lista))        
print(list(a))               

