nameWorkers=["Juan","Luis","Ana","Fran"]

MovieTuple=[("Example1",2010),
("Example2",2008),
("Example3",2012)
]

print(nameWorkers)
print("El primer elemento del array es "+nameWorkers[0])
nameWorkers.append("Teresa")
nameWorkers.insert(0,"Francisco")
print(nameWorkers)
nameWorkers.remove("Luis")
print("Hemos espedido a Luis")
print(nameWorkers[len(nameWorkers)-1]) 
print(id(nameWorkers))


''' #Trabajamos con tuplas
print(MovieTuple)
print(MovieTuple[0])
#print("La película "+ MovieTuple[0][0] + " fue publicada en el año "+ str(MovieTuple[0][1]))
#Si no queremos hacer casting usamos un F-string
print(f"La película  {MovieTuple[0][0]} fue publicada en el año {MovieTuple[0][1]}")
nameFilm=input("Dime la pelicula: ")
year=input("Dime el año: ")
newFilmTuple=[nameFilm,year]
print(f"La pelicula {newFilmTuple[0]} fue publicada en el año {newFilmTuple[1]}") '''




