import math 

""" contador=0
asd=input("Dame tu correo: ")
for i in asd:
    if (i=="@" or i=="."):
        contador=contador+1

if contador==2:
    print("La dirección de correo es válida")
else:
    print("Dirección de correo inválida") """

""" 
i=0

while i<10:
    print(f"Esta es la vuelta {i}")
    i=i+1
 """
print("programa raiz")
num=int(input("Introduce un valor para calcular la raiz: "))
intentos=1
while num<0:
    intentos=intentos+1
    if intentos==3:
        print("Has agotado el tope de intentos")
        break
    else:
        num=int(input("Introduce un valor para calcular la raiz: "))

if intentos<3:
    raiz=math.sqrt(num)
    print(f"La raiz es {raiz}")
 
