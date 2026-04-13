""" users=["lparra","Admin","invitado"]

current_user=input("Dime tu usuario:")
if current_user in users:
    print ("Usuario permitido")
else:
    print("Usuario no permitido") """

Numbers=[10,2,200,27,45]
max_number=max(Numbers)
print(f"El mayor de la lista es {max_number}")

if max_number<50:
    print("Pequeño")
elif max_number<100:
    print("Mediano")
else:
    print("grande")
    