import os
# with open("file.txt","r") as f:
#     contenido=f.read()
#     print(contenido)

# with open("file2.txt","a") as f:
#     f.write("\nhola guapo ")

file_name=input("Dime el nombre del archivo: ")
if os.path.exists(file_name):
    print(f"El archivo {file_name} existe")
    #os.remove(file_name)
    
else:
    print(f"ERROR: El archivo {file_name} no existe")

# with open("file.txt","r",encoding="utf-16") as f:
#     lines=f.readlines()

# for line in lines:
#     print (repr(line))
