""" print("Esto es un bucle, escribe salir para acabar")
while True:
    texto=input("Escribe tu palabra")
    if texto.lower()=="salir":
        break """
Notas=[]
while True:
    nota=int(input("Dime la nota"))
    if nota >=0:
        Notas.append(nota)
    else:
        break
print(f"El mayor de la lista es {max(Notas)}")
print(f"El menor de la lista es {min(Notas)}")
print(f"El nº de elementos de la lista es {len(Notas)}")